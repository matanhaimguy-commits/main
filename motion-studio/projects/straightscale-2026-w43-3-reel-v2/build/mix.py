# Sound for the 22:47 race: VO master (the timeline), music ducked under it, SFX on the overlay's event times.
# All audio is ElevenLabs (see ../CREDITS.md). Output: master.wav at -14 LUFS, true peak -1.5 dBTP.
import subprocess, json, sys
S='/home/user/ss/'
EV={'swoosh':[0.30,0.90,1.50,37.20,47.40],'buzz':[4.55,5.85,19.30],'ping':[8.20,12.00,32.05,34.60,40.40,49.65]}
GAIN={'swoosh':-9,'buzz':-24,'ping':-3}
def measure(f, extra=''):
    r=subprocess.run(['ffmpeg','-hide_banner','-nostats','-i',f,'-af',(extra+',' if extra else '')+'loudnorm=print_format=json','-f','null','-'],capture_output=True,text=True).stderr
    return json.loads(r[r.rindex('{'):r.rindex('}')+1])
music=sys.argv[1] if len(sys.argv)>1 else 'music1'
m=measure(S+f'sfx/{music}.mp3','atrim=0:60')
mg=-27-float(m['input_i'])   # music bed at -27 LUFS before ducking
inputs=['-i',S+'vo/vo_master.wav','-i',S+f'sfx/{music}.mp3']
fc=[f"[1:a]atrim=0:60,asetpts=PTS-STARTPTS,volume={mg:.2f}dB,afade=t=in:st=0:d=0.3,afade=t=out:st=58.6:d=1.4,aformat=sample_rates=48000:channel_layouts=stereo[mus]",
    "[0:a]aformat=sample_rates=48000:channel_layouts=stereo,asplit=2[vo][sc]",
    "[mus][sc]sidechaincompress=threshold=0.02:ratio=8:attack=20:release=350:makeup=1[duck]"]
idx=2; labels=['[vo]','[duck]']
for k,ts in EV.items():
    inputs+=['-i',S+f'sfx/{k}.mp3']
    fc.append(f"[{idx}:a]aformat=sample_rates=48000:channel_layouts=stereo,volume={GAIN[k]}dB,asplit={len(ts)}"+''.join(f'[{k}{i}]' for i in range(len(ts))))
    for i,t in enumerate(ts):
        d=int(round(t*1000)); fc.append(f"[{k}{i}]adelay={d}|{d}[{k}d{i}]"); labels.append(f'[{k}d{i}]')
    idx+=1
fc.append(''.join(labels)+f"amix=inputs={len(labels)}:normalize=0:duration=first,atrim=0:60[pre]")
open('fc.txt','w').write(';\n'.join(fc))
subprocess.run(['ffmpeg','-y','-v','error',*inputs,'-filter_complex_script','fc.txt','-map','[pre]','-c:a','pcm_s24le','pre.wav'],check=True)
p=measure('pre.wav')
ln=(f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={p['input_i']}:measured_TP={p['input_tp']}:measured_LRA={p['input_lra']}"
    f":measured_thresh={p['input_thresh']}:offset={p['target_offset']}:linear=true")
subprocess.run(['ffmpeg','-y','-v','error','-i','pre.wav','-af',ln+',aresample=48000,aformat=sample_fmts=s16:channel_layouts=stereo','-ac','2','-c:a','pcm_s16le','master.wav'],check=True)
f=measure('master.wav'); print('music gain',round(mg,2),'pre',p['input_i'],'final I',f['input_i'],'TP',f['input_tp'],'LRA',f['input_lra'])
# then: ffmpeg -i base.mp4 -framerate 24 -i frames/f%05d.png -i master.wav
#   -filter_complex "[0:v][1:v]overlay=0:0:format=auto,format=yuv420p" -c:v libx264 -preset slow -crf 20 -c:a aac -b:a 256k -movflags +faststart reel.mp4
