"""Download YouTube transcript via yt-dlp and output clean text.

Usage: python yt-download.py <youtube-url>

Outputs a file at YouTube/yt-transcript-<id>.txt with format:
    TITLE: ...
    CHANNEL: ...
    DURATION: ...
    URL: ...
    ---
    [MM:SS] text
    [MM:SS] text
    ...
"""

import subprocess
import sys
import re
import html
from pathlib import Path

if len(sys.argv) < 2:
    print("Usage: python yt-download.py <youtube-url>", file=sys.stderr)
    sys.exit(1)

url = sys.argv[1]

# Extract video ID for unique filenames
video_id = None
if "v=" in url:
    video_id = url.split("v=")[1].split("&")[0]
elif "youtu.be/" in url:
    video_id = url.split("youtu.be/")[1].split("?")[0]
if not video_id:
    print("Cannot extract video ID from URL", file=sys.stderr)
    sys.exit(1)

work_dir = Path("YouTube")
temp_base = f"yt-temp-{video_id}"
output_file = work_dir / f"yt-transcript-{video_id}.txt"

# Clean up any previous temp files for this video
for f in work_dir.glob(f"yt-temp-{video_id}.*"):
    f.unlink()

# Get metadata
meta = subprocess.run(
    [
        "yt-dlp",
        "--js-runtimes", "node",
        "--remote-components", "ejs:github",
        "--skip-download",
        "--print", "title",
        "--print", "channel",
        "--print", "duration_string",
        url,
    ],
    capture_output=True,
    text=True,
)

lines = meta.stdout.strip().split("\n")
title = lines[0] if len(lines) > 0 else "Unknown"
channel = lines[1] if len(lines) > 1 else "Unknown"
duration = lines[2] if len(lines) > 2 else "Unknown"

# Download transcript
result = subprocess.run(
    [
        "yt-dlp",
        "--js-runtimes", "node",
        "--remote-components", "ejs:github",
        "--write-auto-sub",
        "--sub-lang", "en",
        "--sub-format", "srv1",
        "--skip-download",
        "-o", temp_base,
        url,
    ],
    capture_output=True,
    text=True,
    cwd=str(work_dir),
)

if result.returncode != 0:
    print(f"yt-dlp failed: {result.stderr}", file=sys.stderr)
    sys.exit(1)

# Find the subtitle file
sub_files = list(work_dir.glob(f"{temp_base}.*.srv1"))
if not sub_files:
    # Try manual subs
    result2 = subprocess.run(
        [
            "yt-dlp",
            "--js-runtimes", "node",
            "--remote-components", "ejs:github",
            "--write-sub",
            "--sub-lang", "en",
            "--sub-format", "srv1",
            "--skip-download",
            "-o", temp_base,
            url,
        ],
        capture_output=True,
        text=True,
        cwd=str(work_dir),
    )
    sub_files = list(work_dir.glob(f"{temp_base}.*.srv1"))

if not sub_files:
    print("No transcript available for this video.", file=sys.stderr)
    sys.exit(1)

# Parse XML transcript
raw = sub_files[0].read_text(encoding="utf-8")

# Extract text segments with timestamps
segments = re.findall(r'<text start="([^"]+)"[^>]*>(.*?)</text>', raw, re.DOTALL)

# Group by ~30 second intervals and format
transcript_lines = []
current_group_start = None
current_texts = []

for start_str, text in segments:
    start = float(start_str)
    text = html.unescape(html.unescape(re.sub(r"<[^>]+>", "", text))).strip()
    if not text:
        continue

    group_key = int(start) // 30

    if current_group_start is None:
        current_group_start = start
        current_texts = [text]
    elif group_key != int(current_group_start) // 30:
        minutes = int(current_group_start) // 60
        seconds = int(current_group_start) % 60
        timestamp = f"{minutes:02d}:{seconds:02d}"
        transcript_lines.append(f"[{timestamp}] {' '.join(current_texts)}")
        current_group_start = start
        current_texts = [text]
    else:
        current_texts.append(text)

# Flush last group
if current_texts and current_group_start is not None:
    minutes = int(current_group_start) // 60
    seconds = int(current_group_start) % 60
    timestamp = f"{minutes:02d}:{seconds:02d}"
    transcript_lines.append(f"[{timestamp}] {' '.join(current_texts)}")

# Write output
with open(output_file, "w", encoding="utf-8") as f:
    f.write(f"TITLE: {title}\n")
    f.write(f"CHANNEL: {channel}\n")
    f.write(f"DURATION: {duration}\n")
    f.write(f"URL: {url}\n")
    f.write("---\n")
    f.write("\n".join(transcript_lines))

# Clean up temp files
for f in work_dir.glob(f"{temp_base}.*"):
    f.unlink()

print(f"Transcript saved to {output_file}")
