from pathlib import Path
import click
from convo_map.mapping import map_out
from convo_map.transcribe import transcribe


def run(audio_file: Path):
    transcription = transcribe(audio_file)
    diagram = map_out(transcription)
    print(diagram)


@click.command()
@click.option("--audio-file", type=str, required=True)
def _run(audio_file: str):
    run(Path(audio_file))


if __name__ == "__main__":
    _run()
