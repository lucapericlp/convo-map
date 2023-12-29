from pathlib import Path
import click
from convo_map.mapping import map_out
from convo_map.transcribe import transcribe


def run(audio_file: Path, whisper_size: str = "tiny"):
    #  transcription = transcribe(audio_file, whisper_size)
    transcription = Path("./resources/whisper-large.txt").read_text()
    diagram = map_out(transcription)
    #  print(diagram)


@click.command()
@click.option("--audio-file", type=str, required=True)
@click.option("--whisper-size", type=str, required=True)
def _run(audio_file: str, whisper_size: str):
    run(Path(audio_file), whisper_size)


if __name__ == "__main__":
    _run()
