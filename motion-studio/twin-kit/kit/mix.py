"""The sound mix: voice, an effect on every move, the music bed ducked under the voice, then a two-pass loudnorm.

Pass 0 builds the premix and two stems (the voice, and the music as it enters the mix after gain and ducking, which
tools/audio_qa.py compares). Pass 1 measures the premix with loudnorm; pass 2 applies the measured values (linear
mode) to land on -14 LUFS with the true peak under the ceiling.
"""
import json
import re
import subprocess

SR = 48000
TARGET_I, TARGET_TP, TARGET_LRA = -14.0, -2.0, 11.0   # -2 dBTP leaves room for the AAC encode (house: <= -1.5)
DUCK = "threshold=0.03:ratio=4:attack=15:release=350:knee=4"   # about 6-8 dB of dip under the voice


def premix_graph(cues, voice_start, music, duration):
    """(input files, filter_complex) for the premix. Outputs [mix], [vostem], [mstem]."""
    inputs, parts = [], []
    inputs.append(music["src"] if music else None)
    vo_ms = int(round(voice_start * 1000))
    parts.append(f"[0:a]aresample={SR},aformat=channel_layouts=stereo,adelay={vo_ms}:all=1,"
                 f"apad,atrim=0:{duration:.3f},asplit=3[vo][vosc][vostem]")
    mix_in = ["[vo]"]
    if music:
        g = float(music.get("gain_db", -16))
        fade_out = max(0.0, duration - float(music.get("fade_out", 1.2)))
        parts.append(f"[1:a]aresample={SR},aformat=channel_layouts=stereo,"
                     f"atrim={float(music.get('offset', 0)):.3f}:{float(music.get('offset', 0)) + duration:.3f},"
                     f"asetpts=PTS-STARTPTS,apad,atrim=0:{duration:.3f},volume={g}dB,"
                     f"afade=t=in:st=0:d={float(music.get('fade_in', 0.4)):.2f},"
                     f"afade=t=out:st={fade_out:.3f}:d={float(music.get('fade_out', 1.2)):.2f}[mraw]")
        parts.append(f"[mraw][vosc]sidechaincompress={DUCK}[mduck]")
        parts.append("[mduck]asplit=2[m][mstem]")
        mix_in.append("[m]")
    else:
        parts.append("[vosc]anullsink")
    base = 2
    for i, c in enumerate(cues):
        ms = int(round(c["t"] * 1000))
        parts.append(f"[{base + i}:a]aresample={SR},aformat=channel_layouts=stereo,volume={c['gain_db']}dB,"
                     f"adelay={ms}:all=1[s{i}]")
        mix_in.append(f"[s{i}]")
    parts.append(f"{''.join(mix_in)}amix=inputs={len(mix_in)}:normalize=0:dropout_transition=0,"
                 f"atrim=0:{duration:.3f}[mix]")
    return inputs, ";".join(parts)


def premix(voice, voice_start, music, cues, duration, out_mix, out_vo, out_music):
    music_inputs, graph = premix_graph(cues, voice_start, music, duration)
    cmd = ["ffmpeg", "-v", "error", "-y", "-i", str(voice)]
    if music:
        cmd += ["-i", str(music["src"])]
    else:
        cmd += ["-f", "lavfi", "-t", "0.1", "-i", "anullsrc"]
    for c in cues:
        cmd += ["-i", c["file"]]
    cmd += ["-filter_complex", graph, "-map", "[mix]", "-ar", str(SR), str(out_mix),
            "-map", "[vostem]", "-ar", str(SR), str(out_vo)]
    if music:
        cmd += ["-map", "[mstem]", "-ar", str(SR), str(out_music)]
    subprocess.run(cmd, check=True)


def parse_loudnorm(stderr):
    """The JSON block loudnorm prints in pass 1."""
    m = re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", stderr, re.S)
    if not m:
        raise ValueError("loudnorm printed no measurement")
    return json.loads(m.group(0))


def loudnorm_filter(measured=None):
    f = f"loudnorm=I={TARGET_I}:TP={TARGET_TP}:LRA={TARGET_LRA}"
    if measured:
        f += (f":measured_I={measured['input_i']}:measured_TP={measured['input_tp']}"
              f":measured_LRA={measured['input_lra']}:measured_thresh={measured['input_thresh']}"
              f":offset={measured['target_offset']}:linear=true")
    return f + ":print_format=json"


def master(premix_wav, out_wav):
    """Two-pass loudnorm. Returns (pass-1 measurement, pass-2 report)."""
    p1 = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(premix_wav), "-af", loudnorm_filter(),
                         "-f", "null", "-"], capture_output=True, text=True, check=True)
    measured = parse_loudnorm(p1.stderr)
    p2 = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-y", "-i", str(premix_wav), "-af",
                         loudnorm_filter(measured) + f",aresample={SR}", "-ar", str(SR), str(out_wav)],
                        capture_output=True, text=True, check=True)
    return measured, parse_loudnorm(p2.stderr)


def mux(video, audio, out):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(video), "-i", str(audio), "-map", "0:v:0", "-map", "1:a:0",
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", "-ar", str(SR), "-shortest",
                    "-movflags", "+faststart", str(out)], check=True)
