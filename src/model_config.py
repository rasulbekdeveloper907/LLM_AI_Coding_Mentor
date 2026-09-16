from dataclasses import dataclass, asdict

import yaml


@dataclass
class ModelConfig:

    vocab_size: int = 8000


    block_size: int = 256


    n_embd: int = 384


    n_layer: int = 6


    n_head: int = 6

  
    dropout: float = 0.1

    # The feed-forward layer is this many times wider than n_embd.
    # 4 is the classic GPT-2 choice.
    ffn_mult: int = 4

    # Reuse the embedding table as the output layer. Free quality, and it
    # saves vocab_size * n_embd parameters.
    tie_weights: bool = True

    def head_dim(self):        
        return self.n_embd // self.n_head
    def check(self):
        
        if self.n_embd % self.n_head != 0:
            raise ValueError(
                "n_embd ({}) must divide evenly by n_head ({})".format(
                    self.n_embd, self.n_head)
            )
        if self.vocab_size > 65536:
            raise ValueError(
                
            )

    def estimate_parameters(self):
        """A rough parameter count. Deliberately rough.

        Non-embedding parameters, per transformer block, come out at about
        12 * n_embd^2:

            attention  Q, K, V and the output projection  ->  4 * n_embd^2
            feed-forward  n_embd -> 4*n_embd -> n_embd    ->  8 * n_embd^2

        so the stack of blocks is roughly 12 * n_layer * n_embd^2. Biases and
        normalisation layers add a few thousand more; at this scale they do
        not change any decision, so we ignore them.

        The embedding table is a separate cost: vocab_size * n_embd. With
        tie_weights=True the output layer reuses it, so we count it once.
        """
        non_embedding = 12 * self.n_layer * self.n_embd ** 2
        embedding = self.vocab_size * self.n_embd
        position = self.block_size * self.n_embd   # learned position embeddings

        total = non_embedding + embedding + position
        if not self.tie_weights:
            total += self.vocab_size * self.n_embd   # a separate output layer

        return {
            "non_embedding": non_embedding,
            "embedding": embedding,
            "position": position,
            "total": total,
        }

    def estimate_training_memory_mb(self):
        """Very rough GPU memory for the weights during training.

        Each parameter is stored four times over: the weight itself, its
        gradient, and the two running averages AdamW keeps. At 4 bytes each
        that is 16 bytes per parameter.

        Activations cost more on top of this and depend on batch size, so treat
        this as a floor, not a budget.
        """
        total = self.estimate_parameters()["total"]
        return total * 16 / (1024 ** 2)

    def to_dict(self):
        return asdict(self)


def load_config(path):
    """Read a ModelConfig from a YAML file.

    The config lives in a file and not inside a .py file for one reason: six
    weeks from now, the only question that matters is "which settings produced
    this checkpoint?", and a filename can answer it.
    """
    with open(path, "r", encoding="utf-8") as f:
        values = yaml.safe_load(f)

    config = ModelConfig(**values)
    config.check()
    return config
