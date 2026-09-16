from pathlib import Path
import json
import hashlib
import re


# ============================================================
# PATHS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

INPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "filtered"
    / "magicoder_filtered.jsonl"
)

FINAL_DIR = (
    PROJECT_ROOT
    / "data"
    / "final"
)

OUTPUT_FILE = (
    FINAL_DIR
    / "magicoder_final.jsonl"
)


# ============================================================
# CREATE OUTPUT DIRECTORY
# ============================================================

FINAL_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# ============================================================
# NORMALIZE TEXT
# ============================================================

def normalize_text(text: str) -> str:
    """
    Normalize text before calculating hash.
    """

    text = text.lower()

    # Normalize whitespace
    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


# ============================================================
# DOCUMENT HASH
# ============================================================

def document_hash(
    instruction: str,
    response: str
) -> str:

    combined_text = (
        normalize_text(instruction)
        + "\n"
        + normalize_text(response)
    )

    return hashlib.sha256(
        combined_text.encode("utf-8")
    ).hexdigest()


# ============================================================
# DEDUPLICATION
# ============================================================

def deduplicate_dataset():

    print("=" * 70)
    print("AI CODING MENTOR - DEDUPLICATION")
    print("=" * 70)

    print(f"\nInput:")
    print(INPUT_FILE)

    print(f"\nOutput:")
    print(OUTPUT_FILE)

    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Filtered dataset not found:\n{INPUT_FILE}"
        )

    seen_hashes = set()

    input_count = 0
    output_count = 0
    duplicate_count = 0
    invalid_count = 0

    # --------------------------------------------------------
    # READ / WRITE
    # --------------------------------------------------------

    with open(
        INPUT_FILE,
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
                invalid_count += 1
                continue

            instruction = item.get(
                "instruction",
                ""
            )

            response = item.get(
                "response",
                ""
            )

            # ------------------------------------------------
            # Create unique hash
            # ------------------------------------------------

            doc_hash = document_hash(
                instruction,
                response
            )

            # ------------------------------------------------
            # Check duplicate
            # ------------------------------------------------

            if doc_hash in seen_hashes:

                duplicate_count += 1

                continue

            # ------------------------------------------------
            # New document
            # ------------------------------------------------

            seen_hashes.add(doc_hash)

            output_file.write(
                json.dumps(
                    {
                        "instruction": instruction,
                        "response": response
                    },
                    ensure_ascii=False
                )
                + "\n"
            )

            output_count += 1

    # ========================================================
    # RESULTS
    # ========================================================

    print("\n" + "=" * 70)
    print("DEDUPLICATION COMPLETED")
    print("=" * 70)

    print(
        f"\nInput records       : {input_count:,}"
    )

    print(
        f"Duplicates removed  : {duplicate_count:,}"
    )

    print(
        f"Invalid JSON         : {invalid_count:,}"
    )

    print(
        f"Unique records       : {output_count:,}"
    )

    print(
        f"\nOutput file:"
    )

    print(OUTPUT_FILE)

    print(
        f"\nFile exists         : "
        f"{OUTPUT_FILE.exists()}"
    )

    # --------------------------------------------------------
    # Duplicate percentage
    # --------------------------------------------------------

    if input_count > 0:

        duplicate_percentage = (
            duplicate_count
            / input_count
            * 100
        )

        print(
            f"\nDuplicate percentage : "
            f"{duplicate_percentage:.2f}%"
        )


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    deduplicate_dataset()                