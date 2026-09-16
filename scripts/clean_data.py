from pathlib import Path
import json
import re


# ============================================================
# PATHS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_FILE = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "magicoder_evol_instruct_110k.jsonl"
)

CLEANED_DIR = PROJECT_ROOT / "data" / "cleaned"

OUTPUT_FILE = (
    CLEANED_DIR
    / "magicoder_cleaned.jsonl"
)


# ============================================================
# CREATE OUTPUT DIRECTORY
# ============================================================

CLEANED_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# ============================================================
# TEXT CLEANING
# ============================================================

def clean_text(text: str) -> str:
    """
    Clean a single text field.
    """

    if not isinstance(text, str):
        return ""

    # Normalize line endings
    text = text.replace("\r\n", "\n")
    text = text.replace("\r", "\n")

    # Remove null characters
    text = text.replace("\x00", "")

    # Remove excessive spaces/tabs
    text = re.sub(r"[ \t]+", " ", text)

    # Remove excessive empty lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Remove spaces at the beginning/end
    text = text.strip()

    return text


# ============================================================
# DATASET CLEANING
# ============================================================

def clean_dataset():

    print("=" * 70)
    print("AI CODING MENTOR - DATA CLEANING")
    print("=" * 70)

    print(f"\nInput file:")
    print(RAW_FILE)

    print(f"\nOutput file:")
    print(OUTPUT_FILE)

    if not RAW_FILE.exists():
        raise FileNotFoundError(
            f"Raw dataset not found:\n{RAW_FILE}"
        )

    input_count = 0
    output_count = 0
    empty_removed = 0
    invalid_removed = 0

    with open(
        RAW_FILE,
        "r",
        encoding="utf-8"
    ) as input_file, open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as output_file:

        for line in input_file:

            input_count += 1

            # ------------------------------------------------
            # Parse JSON
            # ------------------------------------------------

            try:
                item = json.loads(line)

            except json.JSONDecodeError:
                invalid_removed += 1
                continue

            # ------------------------------------------------
            # Get fields
            # ------------------------------------------------

            instruction = clean_text(
                item.get("instruction", "")
            )

            response = clean_text(
                item.get("response", "")
            )

            # ------------------------------------------------
            # Remove empty samples
            # ------------------------------------------------

            if not instruction or not response:
                empty_removed += 1
                continue

            # ------------------------------------------------
            # Create clean record
            # ------------------------------------------------

            clean_record = {
                "instruction": instruction,
                "response": response
            }

            # ------------------------------------------------
            # Save JSONL
            # ------------------------------------------------

            output_file.write(
                json.dumps(
                    clean_record,
                    ensure_ascii=False
                )
                + "\n"
            )

            output_count += 1

    # ========================================================
    # STATISTICS
    # ========================================================

    print("\n" + "=" * 70)
    print("CLEANING COMPLETED")
    print("=" * 70)

    print(f"\nInput records       : {input_count:,}")
    print(f"Output records      : {output_count:,}")
    print(f"Empty removed       : {empty_removed:,}")
    print(f"Invalid JSON removed: {invalid_removed:,}")

    print(
        f"\nRecords removed     : "
        f"{input_count - output_count:,}"
    )

    print(f"\nOutput file:")
    print(OUTPUT_FILE)

    print(
        f"\nFile exists         : "
        f"{OUTPUT_FILE.exists()}"
    )


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    clean_dataset()