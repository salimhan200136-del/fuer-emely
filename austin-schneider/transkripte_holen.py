"""Lädt die Transkripte aller Videos aus videos.csv in den Ordner transkripte/.

Auf deinem eigenen Rechner ausführen (YouTube blockiert Cloud-Server):
    pip install youtube-transcript-api
    python transkripte_holen.py

Schon vorhandene Transkripte werden übersprungen, du kannst das Skript also
jederzeit abbrechen und später weiterlaufen lassen.
"""
import csv
import time
from pathlib import Path

from youtube_transcript_api import YouTubeTranscriptApi

HIER = Path(__file__).parent
ZIEL = HIER / "transkripte"
ZIEL.mkdir(exist_ok=True)

api = YouTubeTranscriptApi()
with open(HIER / "videos.csv", encoding="utf-8") as f:
    videos = list(csv.DictReader(f))

fehler = []
for v in videos:
    datei = ZIEL / f"{int(v['nr']):03d}_{v['video_id']}.txt"
    if datei.exists():
        continue
    try:
        t = api.fetch(v["video_id"], languages=["en", "de"])
        zeilen = [f"[{int(s.start // 60):02d}:{int(s.start % 60):02d}] {s.text}" for s in t.snippets]
        datei.write_text(f"{v['titel']}\n{v['url']}\n\n" + "\n".join(zeilen), encoding="utf-8")
        print(f"OK   {v['nr']:>3}  {v['titel']}")
    except Exception as e:
        fehler.append(v["nr"])
        print(f"FEHL {v['nr']:>3}  {v['titel']}  ({type(e).__name__})")
    time.sleep(2)  # nicht zu schnell, sonst sperrt YouTube

print(f"\nFertig. {len(videos) - len(fehler)} ok, {len(fehler)} fehlgeschlagen: {fehler}")
