from pathlib import Path
import sys
import json

import yaml


PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(PROJECT_ROOT))


from src.tokenizer import CodingTokenizer


# ============================================================
# PROJECT PATHS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

CONFIG_FILE = (
    PROJECT_ROOT
    / "configs"
    / "run_01.yaml"
)

DATA_DIR = (
    PROJECT_ROOT
    / "data"
    / "final"
)

TOKENIZER_DIR = (
    PROJECT_ROOT
    / "tokenizer"
)

TOKENIZER_FILE = (
    TOKENIZER_DIR
    / "tokenizer.json"
)

TRAIN_FILE = (
    DATA_DIR
    / "train.jsonl"
)


# ============================================================
# LOAD CONFIG
# ============================================================

def load_config():

    with open(
        CONFIG_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return yaml.safe_load(file)


# ============================================================
# PREPARE TRAINING TEXT
# ============================================================

def prepare_text_file():

    """
    train.jsonl ichidagi:

        instruction
        response

    maydonlarini tokenizer training uchun
    oddiy text faylga aylantiradi.
    """

    text_file = (
        TOKENIZER_DIR
        / "tokenizer_training.txt"
    )

    print("\nPreparing tokenizer training data...")

    record_count = 0

    with open(
        TRAIN_FILE,
        "r",
        encoding="utf-8"
    ) as input_file, \
    open(
        text_file,
        "w",
        encoding="utf-8"
    ) as output_file:

        for line in input_file:

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

            if not instruction and not response:
                continue

            # ------------------------------------------------
            # Coding instruction format
            # ------------------------------------------------

            text = (
                "<bos>\n"
                "### Instruction:\n"
                f"{instruction}\n\n"
                "### Response:\n"
                f"{response}\n"
                "<eos>\n"
            )

            output_file.write(text)

            record_count += 1

    print(
        f"Training records: {record_count:,}"
    )

    print(
        f"Training text file: {text_file}"
    )

    return text_file


# ============================================================
# TRAIN TOKENIZER
# ============================================================

def train_tokenizer():

    print("=" * 70)
    print("AI CODING MENTOR - TOKENIZER TRAINING")
    print("=" * 70)

    # --------------------------------------------------------
    # Check files
    # --------------------------------------------------------

    if not CONFIG_FILE.exists():
        raise FileNotFoundError(
            f"Config file not found:\n{CONFIG_FILE}"
        )

    if not TRAIN_FILE.exists():
        raise FileNotFoundError(
            f"Train dataset not found:\n{TRAIN_FILE}"
        )

    # --------------------------------------------------------
    # Load configuration
    # --------------------------------------------------------

    config = load_config()

    vocab_size = int(
        config["vocab_size"]
    )

    print(
        f"\nVocabulary size: {vocab_size}"
    )

    # --------------------------------------------------------
    # Prepare training text
    # --------------------------------------------------------

    training_text_file = (
        prepare_text_file()
    )

    # --------------------------------------------------------
    # Create tokenizer
    # --------------------------------------------------------

    tokenizer = CodingTokenizer(
        vocab_size=vocab_size
    )

    # --------------------------------------------------------
    # Train
    # --------------------------------------------------------

    print("\nTraining Byte-Level BPE tokenizer...")

    tokenizer.train(
        files=[
            str(training_text_file)
        ]
    )

    # --------------------------------------------------------
    # Save
    # --------------------------------------------------------

    TOKENIZER_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    tokenizer.save(
        TOKENIZER_FILE
    )

    # --------------------------------------------------------
    # Results
    # --------------------------------------------------------

    actual_vocab_size = (
        tokenizer.get_vocab_size()
    )

    print("\n" + "=" * 70)
    print("TOKENIZER TRAINING COMPLETED")
    print("=" * 70)

    print(
        f"\nRequested vocab size : {vocab_size}"
    )

    print(
        f"Actual vocab size    : {actual_vocab_size}"
    )

    print(
        f"Tokenizer file       : {TOKENIZER_FILE}"
    )

    print(
        f"File exists          : {TOKENIZER_FILE.exists()}"
    )


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    train_tokenizer()