from pathlib import Path
import json

from datasets import load_dataset


# ============================================================
# PROJECT PATHS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DIR = PROJECT_ROOT / "data" / "raw"
CLEANED_DIR = PROJECT_ROOT / "data" / "cleaned"
FILTERED_DIR = PROJECT_ROOT / "data" / "filtered"
FINAL_DIR = PROJECT_ROOT / "data" / "final"


# ============================================================
# DATASET CONFIG
# ============================================================

DATASET_NAME = "ise-uiuc/Magicoder-Evol-Instruct-110K"
SPLIT = "train"

RAW_FILE = RAW_DIR / "magicoder_evol_instruct_110k.jsonl"


# ============================================================
# CREATE DIRECTORIES
# ============================================================

RAW_DIR.mkdir(parents=True, exist_ok=True)
CLEANED_DIR.mkdir(parents=True, exist_ok=True)
FILTERED_DIR.mkdir(parents=True, exist_ok=True)
FINAL_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# DOWNLOAD DATASET
# ============================================================

def download_dataset():

    print("=" * 60)
    print("AI CODING MENTOR - DATASET DOWNLOAD")
    print("=" * 60)

    print(f"\nDataset: {DATASET_NAME}")
    print(f"Split:   {SPLIT}")

    print("\n[1/3] Loading dataset from Hugging Face...")

    dataset = load_dataset(
        DATASET_NAME,
        split=SPLIT
    )

    print("Dataset loaded successfully!")
    print(f"Number of records: {len(dataset)}")

    print("\n[2/3] Dataset columns:")
    print(dataset.column_names)

    print("\n[3/3] Saving dataset to:")
    print(RAW_FILE)

    with open(
        RAW_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        for item in dataset:

            record = {
                "instruction": item.get("instruction", ""),
                "response": item.get("response", "")
            }

            f.write(
                json.dumps(
                    record,
                    ensure_ascii=False
                ) + "\n"
            )

    print("\n" + "=" * 60)
    print("DOWNLOAD COMPLETED")
    print("=" * 60)

    print(f"\nSaved records : {len(dataset):,}")
    print(f"Output file   : {RAW_FILE}")
    print(f"File exists   : {RAW_FILE.exists()}")


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    download_dataset()