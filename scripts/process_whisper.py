import json
from pathlib import Path

script = json.loads(
    Path("./resources/diarized-whisper-large-v2-cordial-curiosity.json").read_text()
)

new_script = []
for sentence in script:
    _sentence = {"text": "", "speaker": sentence["speaker"]}
    for word in sentence["words"]:
        _sentence["text"] += f'{word["word"]} '
    new_script.append(_sentence)

Path("./resources/processed.json").write_text(json.dumps(new_script, indent=4))
