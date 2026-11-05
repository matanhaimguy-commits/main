# One-encode splice: the 4-subframe render with re-rendered windows dropped in frame-exactly (no generation loss).
# python3 tools/splice.py RAW OUT start:end:file [start:end:file ...]   (seconds, 60 fps, ascending, non-overlapping)
import subprocess, sys
FPS = 60
raw, out, wins = sys.argv[1], sys.argv[2], [w.split(':') for w in sys.argv[3:]]
wins = [(round(float(a) * FPS), round(float(b) * FPS), f) for a, b, f in wins]
n = len(wins)
inputs = ['-i', raw] + sum((['-i', f] for _, _, f in wins), [])
flt = [f"[0:v]split={n + 1}" + ''.join(f'[s{i}]' for i in range(n + 1))]
labels, prev = [], 0
for k, (fa, fb, _) in enumerate(wins, 1):
    flt.append(f"[s{k - 1}]trim=start_frame={prev}:end_frame={fa},setpts=PTS-STARTPTS[k{k}]")
    flt.append(f"[{k}:v]trim=start_frame=0:end_frame={fb - fa},setpts=PTS-STARTPTS[p{k}]")
    labels += [f'[k{k}]', f'[p{k}]']; prev = fb
flt.append(f"[s{n}]trim=start_frame={prev},setpts=PTS-STARTPTS[tail]")
flt.append(''.join(labels) + f"[tail]concat=n={2 * n + 1}:v=1:a=0,format=yuv420p[v]")
subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', *inputs, '-filter_complex', ';'.join(flt), '-map', '[v]', '-r', str(FPS),
                '-c:v', 'libx264', '-crf', '16', '-preset', 'medium', out], check=True)
print(subprocess.run(['ffprobe', '-v', 'error', '-count_frames', '-select_streams', 'v:0', '-show_entries',
                      'stream=nb_read_frames,width,height,r_frame_rate', '-of', 'csv=p=0', out], capture_output=True, text=True).stdout.strip())
