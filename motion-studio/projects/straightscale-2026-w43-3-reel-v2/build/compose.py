# Base picture per the EDL (master time, 24 fps, 1080x1920). Each segment: source clip, source start, push zoom, focus, look.
# Clips are the MiniMax H3 2K renders (1440x2560, 24 fps) listed in ../CREDITS.md; run in the Higgsfield sandbox.
import subprocess, sys
FPS=24
C='/home/user/ss/clips/'
# (start, end, clip, src_start, z0, z1, fx, fy, look, speed)  speed = master seconds per source second (>1 slows)
S=[
 (0.00, 4.05,'k1',0.00,1.00,1.07,.5,.45,'',1),
 (4.05, 5.30,'k2',0.45,1.04,1.10,.5,.5,'',1),
 (5.30, 6.45,'k3',0.90,1.04,1.10,.5,.5,'',1),
 (6.45,11.55,'k4',0.30,1.00,1.22,.28,.80,'',1.047),
 (11.55,13.40,'k5',0.40,1.02,1.08,.5,.5,'',1),
 (13.40,15.25,'k6',0.20,1.02,1.08,.5,.5,'',1),
 (15.25,18.90,'k1',1.20,1.10,1.16,.5,.5,'blur',1),
 (18.90,21.25,'k7',0.60,1.00,1.07,.5,.55,'',1),
 (21.25,22.45,'k2',2.60,1.06,1.12,.5,.5,'',1),
 (22.45,25.95,'k8',0.30,1.00,1.08,.5,.5,'',1),
 (25.95,31.40,'k4',0.00,1.00,1.60,.28,.80,'',1.06),
 (31.40,40.05,'k4',0.00,1.25,1.35,.28,.80,'heavy',1.70),
 (40.05,45.54,'k10',0.00,1.00,1.08,.5,.45,'',1.063),
 (45.54,60.00,'t1b',0.00,1.00,1.04,.5,.4,'',1),
]
def seg(i,s):
    a,b,clip,ss,z0,z1,fx,fy,look,sp=s
    n=round(b*FPS)-round(a*FPS); d=n/FPS
    z=f"({z0}+({z1}-{z0})*min(t/{d},1))"
    vf=[f"setpts=(PTS-STARTPTS)*{sp}", f"fps={FPS}",
        f"scale=w='2*trunc(540*{z})':h='2*trunc(960*{z})':eval=frame:flags=lanczos",
        f"crop=1080:1920:'(iw-1080)*{fx}':'(ih-1920)*{fy}'"]
    if look=='blur': vf+=["gblur=sigma=26","eq=brightness=-0.16:saturation=0.75"]
    if look=='heavy': vf+=["gblur=sigma=36","eq=brightness=-0.10:saturation=0.85"]
    vf+=["tpad=stop_mode=clone:stop_duration=2","format=yuv420p"]
    out=f"seg{i:02d}.mp4"
    cmd=['ffmpeg','-y','-v','error','-ss',str(ss),'-i',C+clip+'.mp4','-an','-vf',','.join(vf),'-frames:v',str(n),
         '-c:v','libx264','-preset','veryfast','-crf','12','-r',str(FPS),out]
    subprocess.run(cmd,check=True); return out,n
if __name__=='__main__':
    idx=[int(x) for x in sys.argv[1:]] or range(len(S))
    for i in idx:
        o,n=seg(i,S[i]); print(o,n,flush=True)
# then: concat seg00..seg13 (concat demuxer, -c copy) -> base.mp4 (1440 frames)
