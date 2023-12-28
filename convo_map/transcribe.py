from pathlib import Path
from convo_map import whisper

def transcribe(audio_file: Path) -> str:
    return whisper.transcribe(str(audio_file))["text"]
