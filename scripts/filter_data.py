from pathlib import Path
import json
import re


# ============================================================
# PATHS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

INPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "cleaned"
    / "magicoder_cleaned.jsonl"
)

FILTERED_DIR = (
    PROJECT_ROOT
    / "data"
    / "filtered"
)

OUTPUT_FILE = (
    FILTERED_DIR
    / "magicoder_filtered.jsonl"
)


# ============================================================
# FILTER CONFIG
# ============================================================

MIN_INSTRUCTION_CHARS = 10
MAX_INSTRUCTION_CHARS = 10000

MIN_RESPONSE_CHARS = 20
MAX_RESPONSE_CHARS = 30000

MIN_TOTAL_CHARS = 50
MAX_TOTAL_CHARS = 40000

MIN_ALPHA_RATIO = 0.20

MAX_REPEATED_LINE_RATIO = 0.70


# ============================================================
# CREATE DIRECTORY
# ============================================================

FILTERED_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def alpha_ratio(text: str) -> float:
    """
    Calculate ratio of alphabetic characters.
    """

    if not text:
        return 0.0

    alpha_count = sum(
        1 for char in text
        if char.isalpha()
    )

    return alpha_count / len(text)


def repeated_line_ratio(text: str) -> float:
    """
    Detect highly repetitive lines.
    """

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    if len(lines) < 3:
        return 0.0

    counts = {}

    for line in lines:
        counts[line] = counts.get(line, 0) + 1

    max_count = max(counts.values())

    return max_count / len(lines)


def should_keep(instruction: str, response: str) -> bool:
    """
    Determine whether a sample passes quality filters.
    """

    instruction_len = len(instruction)
    response_len = len(response)

    total_len = instruction_len + response_len

    # --------------------------------------------------------
    # Instruction length
    # --------------------------------------------------------

    if instruction_len < MIN_INSTRUCTION_CHARS:
        return False

    if instruction_len > MAX_INSTRUCTION_CHARS:
        return False

    # --------------------------------------------------------
    # Response length
    # --------------------------------------------------------

    if response_len < MIN_RESPONSE_CHARS:
        return False

    if response_len > MAX_RESPONSE_CHARS:
        return False

    # --------------------------------------------------------
    # Total length
    # --------------------------------------------------------

    if total_len < MIN_TOTAL_CHARS:
        return False

    if total_len > MAX_TOTAL_CHARS:
        return False

    # --------------------------------------------------------
    # Alpha ratio
    # --------------------------------------------------------

    combined_text = instruction + " " + response

    if alpha_ratio(combined_text) < MIN_ALPHA_RATIO:
        return False

    # --------------------------------------------------------
    # Repeated lines
    # --------------------------------------------------------

    if repeated_line_ratio(response) > MAX_REPEATED_LINE_RATIO:
        return False

    return True


# ============================================================
# FILTER DATASET
# ============================================================

def filter_dataset():

    print("=" * 70)
    print("AI CODING MENTOR - DATA FILTERING")
    print("=" * 70)

    print(f"\nInput:")
    print(INPUT_FILE)

    print(f"\nOutput:")
    print(OUTPUT_FILE)

    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Cleaned dataset not found:\n{INPUT_FILE}"
        )

    # --------------------------------------------------------
    # Statistics
    # --------------------------------------------------------

    input_count = 0
    output_count = 0

    short_instruction = 0
    long_instruction = 0

    short_response = 0
    long_response = 0

    short_total = 0
    long_total = 0

    low_alpha = 0
    repetitive = 0

    # --------------------------------------------------------
    # Read / Write
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

            try:
                item = json.loads(line)
            except json.JSONDecodeError:
                continue

            instruction = item.get(
                "instruction",
                ""
            )

            response = item.get(
                "response",
                ""
            )

            instruction_len = len(instruction)
            response_len = len(response)
            total_len = instruction_len + response_len

            combined_text = instruction + " " + response

            # ------------------------------------------------
            # Individual filter statistics
            # ------------------------------------------------

            if instruction_len < MIN_INSTRUCTION_CHARS:
                short_instruction += 1
                continue

            if instruction_len > MAX_INSTRUCTION_CHARS:
                long_instruction += 1
                continue

            if response_len < MIN_RESPONSE_CHARS:
                short_response += 1
                continue

            if response_len > MAX_RESPONSE_CHARS:
                long_response += 1
                continue

            if total_len < MIN_TOTAL_CHARS:
                short_total += 1
                continue

            if total_len > MAX_TOTAL_CHARS:
                long_total += 1
                continue

            if alpha_ratio(combined_text) < MIN_ALPHA_RATIO:
                low_alpha += 1
                continue

            if repeated_line_ratio(response) > MAX_REPEATED_LINE_RATIO:
                repetitive += 1
                continue

            # ------------------------------------------------
            # Keep record
            # ------------------------------------------------

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

    removed = input_count - output_count

    print("\n" + "=" * 70)
    print("FILTERING COMPLETED")
    print("=" * 70)

    print(f"\nInput records       : {input_count:,}")
    print(f"Output records      : {output_count:,}")
    print(f"Removed records     : {removed:,}")

    print("\nFilter statistics:")

    print(
        f"Short instruction   : {short_instruction:,}"
    )

    print(
        f"Long instruction    : {long_instruction:,}"
    )

    print(
        f"Short response      : {short_response:,}"
    )

    print(
        f"Long response       : {long_response:,}"
    )

    print(
        f"Short total         : {short_total:,}"
    )

    print(
        f"Long total          : {long_total:,}"
    )

    print(
        f"Low alpha ratio     : {low_alpha:,}"
    )

    print(
        f"Repetitive response : {repetitive:,}"
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
    filter_dataset()