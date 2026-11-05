# Seam check for a segment-rendered film: frame-to-frame change at each join vs its neighbours.
# python3 tools/seams.py out/silent.mp4 9 18
import subprocess, sys, numpy as np
path, joins = sys.argv[1], [float(x) for x in sys.argv[2:]]
fps = 60
for j in joins:
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{j - 4 / fps:.4f}', '-i', path, '-frames:v', '8', '-vf', 'scale=270:-1',
                          '-f', 'rawvideo', '-pix_fmt', 'gray', '-'], capture_output=True, check=True).stdout
    f = np.frombuffer(raw, np.uint8).reshape(8, -1).astype(np.float32)
    d = [float(np.abs(f[i] - f[i - 1]).mean()) for i in range(1, 8)]
    seam = d[3]; other = max(d[:3] + d[4:])
    print(f'join {j:5.2f}s  steps {" ".join(f"{x:.2f}" for x in d)}  seam {seam:.2f} vs max other {other:.2f}  {"PASS" if seam <= other * 1.6 + 0.3 else "CHECK"}')
