from dataclasses import dataclass

import mlx.core as mx

from convo_map.phi2.phi2 import load_model, generate

#  class Mapper:
#      def __init__(self, model_path: str):
#          self.model_path = model_path

#      def run(self, prompt: str) -> str:
#          ...

@dataclass
class InferenceArgs:
    seed: int = 42
    prompt: str = "Summarise the following: "
    model_path = "./convo_map/phi2/mlx_model"
    temp: float = 0.0
    max_tokens: int = 100


def map_out(transcription: str, args: InferenceArgs = InferenceArgs()) -> str:
    mx.random.seed(args.seed)

    model, tokenizer = load_model(args.model_path)

    prompt = tokenizer(
        args.prompt,
        return_tensors="np",
        return_attention_mask=False,
    )["input_ids"]

    prompt = mx.array(prompt)

    print("[INFO] Generating with Phi-2...", flush=True)
    print(args.prompt, end="", flush=True)

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
            tokens = []
            if eos_index is not None:
                break

    mx.eval(tokens)
    s = tokenizer.decode([t.item() for t in tokens])

    return s
