from pathlib import Path
import json
import numpy as np

from src.tokenizer import CodingTokenizer


class BinaryDatasetBuilder:
    """
    JSONL datasetni tokenizer orqali token ID'lariga aylantiradi
    va uint16 formatida .bin faylga yozadi.
    """

    def __init__(
        self,
        tokenizer_path,
        vocab_size,
        block_size
    ):
        self.tokenizer_path = Path(tokenizer_path)
        self.vocab_size = vocab_size
        self.block_size = block_size

        # Load tokenizer
        self.tokenizer = CodingTokenizer(
            vocab_size=vocab_size
        )

        self.tokenizer.load(
            self.tokenizer_path
        )

    def format_record(
        self,
        instruction,
        response
    ):
        """
        Instruction + response ni model training formatiga
        aylantiradi.
        """

        return (
            "<bos>\n"
            "### Instruction:\n"
            f"{instruction}\n\n"
            "### Response:\n"
            f"{response}\n"
            "<eos>"
        )

    def tokenize_file(
        self,
        input_file,
        output_file
    ):
        """
        JSONL -> token IDs -> uint16 .bin
        """

        input_file = Path(input_file)
        output_file = Path(output_file)

        if not input_file.exists():
            raise FileNotFoundError(
                f"Input file not found:\n{input_file}"
            )

        output_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        token_count = 0
        record_count = 0
        max_token_id = 0

        # Binary output
        with open(
            input_file,
            "r",
            encoding="utf-8"
        ) as input_f, \
        open(
            output_file,
            "wb"
        ) as output_f:

            for line in input_f:

                line = line.strip()

                if not line:
                    continue

                try:
                    item = json.loads(line)

                except json.JSONDecodeError:
                    continue

                instruction = item.get(
                    "instruction",
                    ""
                ).strip()

                response = item.get(
                    "response",
                    ""
                ).strip()

                if not instruction or not response:
                    continue

                # --------------------------------------------
                # Create training text
                # --------------------------------------------

                text = self.format_record(
                    instruction,
                    response
                )

                # --------------------------------------------
                # Tokenize
                # --------------------------------------------

                token_ids = self.tokenizer.encode(
                    text
                )

                if not token_ids:
                    continue

                # --------------------------------------------
                # Check token IDs
                # --------------------------------------------

                current_max = max(token_ids)

                if current_max >= self.vocab_size:
                    raise ValueError(
                        f"Token ID {current_max} exceeds "
                        f"vocab size {self.vocab_size}"
                    )

                max_token_id = max(
                    max_token_id,
                    current_max
                )

                # --------------------------------------------
                # uint16 conversion
                # --------------------------------------------

                tokens = np.asarray(
                    token_ids,
                    dtype=np.uint16
                )

                # --------------------------------------------
                # Write binary data
                # --------------------------------------------

                output_f.write(
                    tokens.tobytes()
                )

                token_count += len(token_ids)
                record_count += 1

        return {
            "records": record_count,
            "tokens": token_count,
            "max_token_id": max_token_id,
            "output_file": str(output_file)
        }