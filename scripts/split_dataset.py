from pathlib import Path
import json
import random


# ============================================================
# PROJECT PATHS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

INPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "final"
    / "magicoder_final.jsonl"
)

OUTPUT_DIR = PROJECT_ROOT / "data" / "final"


# ============================================================
# SPLIT CONFIGURATION
# ============================================================

TRAIN_RATIO = 0.90
VALIDATION_RATIO = 0.05
TEST_RATIO = 0.05

RANDOM_SEED = 42


# ============================================================
# VALIDATE CONFIGURATION
# ============================================================

if abs(
    TRAIN_RATIO
    + VALIDATION_RATIO
    + TEST_RATIO
    - 1.0
) > 1e-9:
    raise ValueError(
        "TRAIN + VALIDATION + TEST ratios must equal 1.0"
    )


# ============================================================
# OUTPUT FILES
# ============================================================

TRAIN_FILE = OUTPUT_DIR / "train.jsonl"
VALIDATION_FILE = OUTPUT_DIR / "validation.jsonl"
TEST_FILE = OUTPUT_DIR / "test.jsonl"


# ============================================================
# SPLIT DATASET
# ============================================================

def split_dataset():

    print("=" * 70)
    print("AI CODING MENTOR - DATASET SPLIT")
    print("=" * 70)

    print(f"\nInput file:")
    print(INPUT_FILE)

    print(f"\nOutput directory:")
    print(OUTPUT_DIR)

    # --------------------------------------------------------
    # Check input file
    # --------------------------------------------------------

    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"\nFinal dataset not found:\n{INPUT_FILE}"
        )

    # --------------------------------------------------------
    # Create output directory
    # --------------------------------------------------------

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    # --------------------------------------------------------
    # Counters
    # --------------------------------------------------------

    train_count = 0
    validation_count = 0
    test_count = 0
    invalid_count = 0

    # --------------------------------------------------------
    # Random generator
    # --------------------------------------------------------

    rng = random.Random(RANDOM_SEED)

    # --------------------------------------------------------
    # Open files
    # --------------------------------------------------------

    with open(
        INPUT_FILE,
        "r",
        encoding="utf-8"
    ) as input_file, \
    open(
        TRAIN_FILE,
        "w",
        encoding="utf-8"
    ) as train_file, \
    open(
        VALIDATION_FILE,
        "w",
        encoding="utf-8"
    ) as validation_file, \
    open(
        TEST_FILE,
        "w",
        encoding="utf-8"
    ) as test_file:

        # ----------------------------------------------------
        # Process each record
        # ----------------------------------------------------

        for line in input_file:

            line = line.strip()

            if not line:
                continue

            try:
                item = json.loads(line)

            except json.JSONDecodeError:
                invalid_count += 1
                continue

            # ------------------------------------------------
            # Keep only required fields
            # ------------------------------------------------

            record = {
                "instruction": item.get(
                    "instruction",
                    ""
                ),
                "response": item.get(
                    "response",
                    ""
                )
            }

            record_json = json.dumps(
                record,
                ensure_ascii=False
            ) + "\n"

            # ------------------------------------------------
            # Random split
            # ------------------------------------------------

            random_value = rng.random()

            if random_value < TRAIN_RATIO:

                train_file.write(record_json)
                train_count += 1

            elif random_value < (
                TRAIN_RATIO + VALIDATION_RATIO
            ):

                validation_file.write(record_json)
                validation_count += 1

            else:

                test_file.write(record_json)
                test_count += 1

    # ========================================================
    # RESULTS
    # ========================================================

    total_count = (
        train_count
        + validation_count
        + test_count
    )

    print("\n" + "=" * 70)
    print("DATASET SPLIT COMPLETED")
    print("=" * 70)

    print(f"\nTotal records       : {total_count:,}")
    print(f"Train records      : {train_count:,}")
    print(f"Validation records : {validation_count:,}")
    print(f"Test records       : {test_count:,}")
    print(f"Invalid JSON       : {invalid_count:,}")

    if total_count > 0:

        print("\nActual split:")

        print(
            f"Train       : "
            f"{train_count / total_count * 100:.2f}%"
        )

        print(
            f"Validation  : "
            f"{validation_count / total_count * 100:.2f}%"
        )

        print(
            f"Test        : "
            f"{test_count / total_count * 100:.2f}%"
        )

    print("\nOutput files:")

    print(f"Train      : {TRAIN_FILE}")
    print(f"Validation : {VALIDATION_FILE}")
    print(f"Test       : {TEST_FILE}")

    print("\nFile status:")

    print(
        f"train.jsonl       : "
        f"{TRAIN_FILE.exists()}"
    )

    print(
        f"validation.jsonl  : "
        f"{VALIDATION_FILE.exists()}"
    )

    print(
        f"test.jsonl        : "
        f"{TEST_FILE.exists()}"
    )


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    split_dataset()