from pathlib import Path
from convo_map import whisper

def transcribe(audio_file: Path, model_size: str) -> str:
    return whisper.transcribe(str(audio_file), model=model_size)["text"]
