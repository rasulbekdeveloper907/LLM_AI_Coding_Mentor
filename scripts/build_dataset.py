from pathlib import Path
import sys
import json

import yaml


# ============================================================
# PROJECT ROOT
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(PROJECT_ROOT))


from src.dataset_builder import BinaryDatasetBuilder


# ============================================================
# PATHS
# ============================================================

CONFIG_FILE = (
    PROJECT_ROOT
    / "configs"
    / "run_01.yaml"
)

TOKENIZER_FILE = (
    PROJECT_ROOT
    / "tokenizer"
    / "tokenizer.json"
)

DATA_DIR = (
    PROJECT_ROOT
    / "data"
    / "final"
)

OUTPUT_DIR = (
    PROJECT_ROOT
    / "dataset"
)


# ============================================================
# DATASET SPLITS
# ============================================================

DATASETS = {
    "train": {
        "input": DATA_DIR / "train.jsonl",
        "output": OUTPUT_DIR / "train.bin",
    },

    "validation": {
        "input": DATA_DIR / "validation.jsonl",
        "output": OUTPUT_DIR / "validation.bin",
    },

    "test": {
        "input": DATA_DIR / "test.jsonl",
        "output": OUTPUT_DIR / "test.bin",
    },
}


# ============================================================
# LOAD CONFIG
# ============================================================

def load_config():

    if not CONFIG_FILE.exists():
        raise FileNotFoundError(
            f"Config file not found:\n{CONFIG_FILE}"
        )

    with open(
        CONFIG_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return yaml.safe_load(file)


# ============================================================
# BUILD DATASET
# ============================================================

def build_datasets():

    print("=" * 70)
    print("AI CODING MENTOR - BINARY DATASET BUILDER")
    print("=" * 70)

    # --------------------------------------------------------
    # Check tokenizer
    # --------------------------------------------------------

    if not TOKENIZER_FILE.exists():
        raise FileNotFoundError(
            f"Tokenizer not found:\n{TOKENIZER_FILE}"
        )

    # --------------------------------------------------------
    # Load configuration
    # --------------------------------------------------------

    config = load_config()

    vocab_size = int(
        config["vocab_size"]
    )

    block_size = int(
        config["block_size"]
    )

    print(f"\nVocabulary size : {vocab_size}")
    print(f"Block size      : {block_size}")
    print(f"Tokenizer       : {TOKENIZER_FILE}")

    # --------------------------------------------------------
    # Create output directory
    # --------------------------------------------------------

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    # --------------------------------------------------------
    # Create builder
    # --------------------------------------------------------

    builder = BinaryDatasetBuilder(
        tokenizer_path=TOKENIZER_FILE,
        vocab_size=vocab_size,
        block_size=block_size
    )

    results = {}

    # ========================================================
    # PROCESS EACH SPLIT
    # ========================================================

    for split_name, paths in DATASETS.items():

        input_file = paths["input"]
        output_file = paths["output"]

        print("\n")
        print("=" * 70)
        print(f"PROCESSING: {split_name.upper()}")
        print("=" * 70)

        print(f"Input : {input_file}")
        print(f"Output: {output_file}")

        # ----------------------------------------------------
        # Check input
        # ----------------------------------------------------

        if not input_file.exists():

            raise FileNotFoundError(
                f"\nInput dataset not found:\n{input_file}"
            )

        # ----------------------------------------------------
        # Remove old output
        # ----------------------------------------------------

        if output_file.exists():

            print("\nRemoving old binary file...")

            output_file.unlink()

        # ----------------------------------------------------
        # Tokenize
        # ----------------------------------------------------

        result = builder.tokenize_file(
            input_file=input_file,
            output_file=output_file
        )

        results[split_name] = result

        print("\nCompleted:")

        print(
            f"Records      : "
            f"{result['records']:,}"
        )

        print(
            f"Tokens       : "
            f"{result['tokens']:,}"
        )

        print(
            f"Max token ID : "
            f"{result['max_token_id']}"
        )

        print(
            f"File exists  : "
            f"{output_file.exists()}"
        )

    # ========================================================
    # CREATE META.JSON
    # ========================================================

    metadata = {
        "vocab_size": vocab_size,
        "block_size": block_size,
        "dtype": "uint16",
        "tokenizer": "tokenizer/tokenizer.json",
        "splits": {}
    }

    for split_name, result in results.items():

        output_file = Path(
            result["output_file"]
        )

        metadata["splits"][split_name] = {
            "records": result["records"],
            "tokens": result["tokens"],
            "file": str(
                output_file.relative_to(
                    PROJECT_ROOT
                )
            )
        }

    metadata_file = (
        OUTPUT_DIR / "meta.json"
    )

    with open(
        metadata_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            metadata,
            file,
            indent=2,
            ensure_ascii=False
        )

    # ========================================================
    # FINAL RESULT
    # ========================================================

    print("\n")
    print("=" * 70)
    print("BINARY DATASET BUILD COMPLETED")
    print("=" * 70)

    print("\nGenerated files:")

    print(
        f"train.bin      : "
        f"{(OUTPUT_DIR / 'train.bin').exists()}"
    )

    print(
        f"validation.bin : "
        f"{(OUTPUT_DIR / 'validation.bin').exists()}"
    )

    print(
        f"test.bin       : "
        f"{(OUTPUT_DIR / 'test.bin').exists()}"
    )

    print(
        f"meta.json      : "
        f"{metadata_file.exists()}"
    )

    print("\nDataset directory:")
    print(OUTPUT_DIR)


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    build_datasets()