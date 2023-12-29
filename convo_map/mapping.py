import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

import mlx.core as mx

from convo_map.phi2.phi2 import load_model, generate
from convo_map.prompts import get_undiarized_prompt

#  class Mapper:
#      def __init__(self, model_path: str):
#          self.model_path = model_path

#      def run(self, prompt: str) -> str:
#          ...

@dataclass
class InferenceArgs:
    seed: int = 42
    get_prompt: Callable[[str], str] = get_undiarized_prompt
    model_path: str = "./convo_map/phi2/mlx_model"
    temp: float = 0.0
    max_tokens: int = 100


def map_out(transcription: str, args: InferenceArgs = InferenceArgs()) -> str:
    mx.random.seed(args.seed)

    model, tokenizer = load_model(args.model_path)

    text_prompt = args.get_prompt(transcription)
    prompt = tokenizer(
        text_prompt,
        return_tensors="np",
        return_attention_mask=False,
    )["input_ids"]

    prompt = mx.array(prompt)

    print("[INFO] Generating with Phi-2...", flush=True)
    print(args.get_prompt("x"), end="", flush=True)
    unique_output_dir =  Path(f"./outputs/{uuid.uuid4()}")
    unique_output_dir.mkdir(parents=True, exist_ok=True)

    used_prompt =  unique_output_dir / "used_prompt.txt"
    used_prompt.write_text(text_prompt)

    full_output = []
    tokens = []
    for token, _ in zip(generate(prompt, model, args.temp), range(args.max_tokens)):
        tokens.append(token)

        if (len(tokens) % 10) == 0:
            mx.eval(tokens)
            eos_index = next(
                (i for i, t in enumerate(tokens) if t.item() == tokenizer.eos_token_id),
                None,
            )

            if eos_index is not None:
                tokens = tokens[:eos_index]

            s = tokenizer.decode([t.item() for t in tokens])
            print(s, end="", flush=True)
            full_output.append(s)
            tokens = []
            if eos_index is not None:
                break

    # for the remaining tokens
    mx.eval(tokens)
    s = tokenizer.decode([t.item() for t in tokens])
    full_output.append(s)

    combined_output = " ".join(full_output)
    result = unique_output_dir / "output.txt"
    result.write_text(combined_output)

    return combined_output
