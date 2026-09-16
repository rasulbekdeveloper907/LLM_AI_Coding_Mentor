from pathlib import Path

from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.pre_tokenizers import ByteLevel
from tokenizers.decoders import ByteLevel as ByteLevelDecoder
from tokenizers.trainers import BpeTrainer
from tokenizers.normalizers import Sequence, NFKC


class CodingTokenizer:
    """
    AI Coding Mentor uchun Byte-Level BPE tokenizer.

    Vazifalari:
    - coding datasetdan tokenizer o'qitish
    - text -> token IDs
    - token IDs -> text
    - tokenizer.json faylini saqlash
    """

    SPECIAL_TOKENS = [
        "<pad>",
        "<unk>",
        "<bos>",
        "<eos>",
    ]

    def __init__(self, vocab_size: int = 8000):
        self.vocab_size = vocab_size

        self.tokenizer = Tokenizer(
            BPE(
                unk_token="<unk>"
            )
        )

        # Unicode normalization
        self.tokenizer.normalizer = Sequence([
            NFKC()
        ])

        # Byte-Level preprocessing
        self.tokenizer.pre_tokenizer = ByteLevel(
            add_prefix_space=False
        )

        # Byte-Level decoding
        self.tokenizer.decoder = ByteLevelDecoder()

    def train(self, files):
        """
        Berilgan JSONL/text fayllardan tokenizer o'qitadi.
        """

        trainer = BpeTrainer(
            vocab_size=self.vocab_size,
            min_frequency=2,
            special_tokens=self.SPECIAL_TOKENS,
            show_progress=True,
        )

        self.tokenizer.train(
            files=files,
            trainer=trainer
        )

    def save(self, output_file):
        """
        Tokenizerni tokenizer.json sifatida saqlaydi.
        """

        output_file = Path(output_file)
        output_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        self.tokenizer.save(
            str(output_file)
        )

    def encode(self, text: str):
        """
        Text -> token IDs
        """

        encoded = self.tokenizer.encode(text)

        return encoded.ids

    def decode(self, token_ids):
        """
        Token IDs -> text
        """

        return self.tokenizer.decode(
            token_ids
        )

    def encode_with_tokens(self, text: str):
        """
        Text -> token IDs + tokenlar
        """

        encoded = self.tokenizer.encode(text)

        return {
            "ids": encoded.ids,
            "tokens": encoded.tokens
        }

    def token_to_id(self, token: str):
        """
        Token -> ID
        """

        return self.tokenizer.token_to_id(token)

    def id_to_token(self, token_id: int):
        """
        ID -> Token
        """

        return self.tokenizer.id_to_token(
            token_id
        )

    def get_vocab_size(self):
        """
        Vocabulary size.
        """

        return self.tokenizer.get_vocab_size()

    def load(self, tokenizer_file):
        """
        Mavjud tokenizer.json ni yuklaydi.
        """

        tokenizer_file = Path(
            tokenizer_file
        )

        if not tokenizer_file.exists():
            raise FileNotFoundError(
                f"Tokenizer not found:\n{tokenizer_file}"
            )

        self.tokenizer = Tokenizer.from_file(
            str(tokenizer_file)
        )