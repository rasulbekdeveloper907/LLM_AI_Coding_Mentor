# 📊 Dataset Card — AI Coding Mentor

## 1. Dataset Overview

**Project:** AI Coding Mentor

**Purpose:** Programming-oriented Local Large Language Model

**Primary Dataset:**

`ise-uiuc/Magicoder-Evol-Instruct-110K`

**Source:** Hugging Face

**Dataset URL:**

https://huggingface.co/datasets/ise-uiuc/Magicoder-Evol-Instruct-110K

**Task:** Code generation, programming instruction following, code problem solving

**Intended use:** Supervised Fine-Tuning (SFT) of the AI Coding Mentor model

---

# 2. Dataset Purpose

AI Coding Mentor foydalanuvchilarga programming bo‘yicha mentorlik qilishga mo‘ljallangan.

Dataset modelga quyidagi qobiliyatlarni o‘rgatish uchun ishlatiladi:

* Code generation
* Code explanation
* Programming problem solving
* Code completion
* Algorithm implementation
* Debugging-oriented reasoning
* Instruction following
* Programming question answering

Datasetdan foydalanish orqali model:

```text
Programming Instruction
        ↓
Understanding
        ↓
Code / Explanation
        ↓
Useful Response
```

jarayonini o‘rganadi.

---

# 3. Dataset Source

Dataset Hugging Face platformasidan olinadi.

**Dataset ID:**

```text
ise-uiuc/Magicoder-Evol-Instruct-110K
```

**Dataset name:**

```text
Magicoder-Evol-Instruct-110K
```

**Source organization:**

```text
ise-uiuc
```

**Platform:**

```text
Hugging Face Datasets
```

---

# 4. Dataset Size

Dataset taxminan:

```text
Examples: ~111K
Size: ~255 MB
```

Datasetdagi aniq sample soni va hajmi dataset versiyasiga qarab farq qilishi mumkin.

Datasetni loyihaga yuklashdan oldin metadata tekshiriladi.

Example:

```python
from datasets import load_dataset

dataset = load_dataset(
    "ise-uiuc/Magicoder-Evol-Instruct-110K"
)

print(dataset)
```

---

# 5. Dataset Structure

Datasetning asosiy ma'lumotlari instruction va response ko‘rinishida beriladi.

Asosiy concept:

```text
instruction
    ↓
response
```

Masalan:

```json
{
  "instruction": "Write a Python function to check whether a number is prime.",
  "response": "def is_prime(n): ..."
}
```

Bu format AI Coding Mentor uchun qulay, chunki:

```text
User Question
      ↓
instruction
      ↓
Model
      ↓
response
      ↓
Assistant Answer
```

ko‘rinishiga oson transformatsiya qilinadi.

---

# 6. Data Format

Raw dataset Hugging Face `datasets` formatida olinadi.

Project ichida esa dataset JSONL formatiga o'tkazilishi mumkin.

Final record quyidagi formatda bo‘ladi:

```json
{
  "instruction": "...",
  "response": "..."
}
```

SFT uchun kerak bo‘lsa quyidagi chat formatiga ham transformatsiya qilinadi:

```json
{
  "messages": [
    {
      "role": "user",
      "content": "..."
    },
    {
      "role": "assistant",
      "content": "..."
    }
  ]
}
```

---

# 7. Dataset License

Dataset sahifasida **Apache-2.0** license ko‘rsatilgan.

License:

```text
Apache License 2.0
```

Source:

https://huggingface.co/datasets/ise-uiuc/Magicoder-Evol-Instruct-110K

Apache-2.0 license odatda datasetdan foydalanish, modification va redistribution uchun shartlarni belgilaydi.

Projectda datasetdan foydalanishda:

* original source'ni ko‘rsatish;
* license shartlariga rioya qilish;
* datasetning o‘z license talablarini project code license'idan alohida ko‘rish

kerak.

> **Important:** Dataset license'i project source-code license'i bilan bir xil narsa emas. Projectning `LICENSE` fayli va datasetning license shartlari alohida boshqariladi.

---

# 8. Intended Use

Dataset quyidagi maqsadlarda ishlatiladi:

### Primary Use

```text
AI Coding Mentor
       ↓
Supervised Fine-Tuning
       ↓
Programming Assistant
```

### Supported tasks

* Python code generation
* General programming
* Algorithm problems
* Code explanation
* Programming instruction following
* Code transformation
* Programming problem solving

---

# 9. Out-of-Scope Use

Dataset va undan o‘qitilgan model quyidagi maqsadlar uchun maxsus ishlab chiqilmagan:

* Autonomous production software deployment
* Security-critical software generation without review
* Financial decision systems
* Medical decision systems
* Legal decision systems
* Fully autonomous coding without human verification

Model tomonidan generatsiya qilingan kod production environment'da ishlatilishidan oldin inson tomonidan tekshirilishi kerak.

---

# 10. Data Collection

Dataset Hugging Face orqali projectga olinadi.

Datasetni yuklash:

```python
from datasets import load_dataset

dataset = load_dataset(
    "ise-uiuc/Magicoder-Evol-Instruct-110K"
)
```

Raw data:

```text
data/
└── raw/
    └── magicoder_evol_instruct_110k.jsonl
```

Raw dataset original holatda saqlanadi va preprocessing jarayonida o‘zgartirilmaydi.

---

# 11. Data Processing Pipeline

Dataset quyidagi pipeline orqali qayta ishlanadi:

```text
Hugging Face
     ↓
Raw Dataset
     ↓
Inspection
     ↓
Cleaning
     ↓
Quality Filtering
     ↓
Deduplication
     ↓
Normalization
     ↓
Train / Validation / Test
     ↓
Final Dataset
     ↓
Tokenizer
```

---

# 12. Data Inspection

Raw datasetni trainingdan oldin tekshirish kerak.

Tekshiriladigan parametrlar:

```text
Number of samples
Column names
Missing values
Empty instructions
Empty responses
Duplicate samples
Text length
Language
Programming language
Invalid records
```

Example:

```python
print(dataset)
print(dataset.column_names)
print(dataset["train"][0])
```

---

# 13. Data Cleaning

Cleaning bosqichida quyidagi amallar bajariladi:

### Empty data

Quyidagi samplelar olib tashlanadi:

```text
instruction == ""
response == ""
```

### Whitespace normalization

Ortiqcha whitespace kamaytiriladi.

### Unicode normalization

Text normalization amalga oshiriladi.

### Invalid data

Corrupted yoki noto‘g‘ri formatdagi recordlar chiqarib tashlanadi.

### Example

Raw:

```text
"   Write a Python function.   "
```

Cleaned:

```text
"Write a Python function."
```

---

# 14. Quality Filtering

Modelga foydasiz yoki sifatsiz ma'lumotlar berilmasligi uchun filtering ishlatiladi.

Asosiy filtering mezonlari:

```text
Minimum instruction length
Maximum instruction length
Minimum response length
Maximum response length
Empty content
Repeated content
Invalid characters
Extremely long samples
Low-quality responses
```

Masalan:

```python
MIN_INSTRUCTION_CHARS = 10
MAX_INSTRUCTION_CHARS = 5000

MIN_RESPONSE_CHARS = 20
MAX_RESPONSE_CHARS = 10000
```

Aniq thresholdlar dataset statistikasi asosida belgilanadi.

---

# 15. Deduplication

Datasetda duplicate samplelar bo‘lishi mumkin.

Duplicate samplelar training data diversity'ni kamaytirishi mumkin.

Exact duplicate aniqlash uchun normalized text hash qilinadi.

Example:

```python
import hashlib

def document_hash(text):
    normalized = " ".join(text.split())
    return hashlib.sha256(
        normalized.encode("utf-8")
    ).hexdigest()
```

Pipeline:

```text
Document
   ↓
Normalize
   ↓
SHA-256
   ↓
Hash comparison
   ↓
Duplicate removal
```

---

# 16. Dataset Splitting

Final dataset uch qismga ajratiladi:

```text
Train       → 90%
Validation  → 5%
Test        → 5%
```

Structure:

```text
data/
└── final/
    ├── train.jsonl
    ├── validation.jsonl
    └── test.jsonl
```

### Train

Model training uchun ishlatiladi.

### Validation

Training davomida modelni monitoring qilish uchun ishlatiladi.

### Test

Final evaluation uchun ishlatiladi.

Test dataset training jarayonida ishlatilmaydi.

---

# 17. Data Leakage Prevention

Test va validation samplelar training datasetga tushmasligi kerak.

Pipeline:

```text
Raw
 ↓
Cleaning
 ↓
Deduplication
 ↓
Split
 ↓
Train / Validation / Test
```

Dataset splitdan oldin yoki split bilan bog‘liq duplicate prevention strategiyasi qo‘llanadi.

Test data model training jarayoniga aralashtirilmasligi kerak.

---

# 18. Tokenization

Final dataset tokenizer orqali tokenlarga aylantiriladi.

```text
Text
 ↓
Tokenizer
 ↓
Token IDs
```

Example:

```text
"Write Python code"
```

↓

```text
[1542, 892, 4217]
```

Token ID'lar keyinchalik binary formatga o'tkaziladi.

---

# 19. Binary Dataset

Tokenized data:

```text
data/
└── processed/
    ├── train.bin
    ├── validation.bin
    ├── test.bin
    └── meta.json
```

`.bin` fayllar model training vaqtida tezroq o‘qish uchun ishlatiladi.

---

# 20. Metadata

`meta.json` tokenization va dataset haqidagi ma'lumotlarni saqlaydi.

Example:

```json
{
  "vocab_size": 32000,
  "dtype": "uint16",
  "bos_token_id": 1,
  "eos_token_id": 2,
  "pad_token_id": 0
}
```

Metadata training pipeline uchun kerakli parametrlarni saqlashga yordam beradi.

---

# 21. Sequence Packing

Qisqa training samplelar bir sequence ichida packing qilinishi mumkin.

Example:

```text
Sample 1 + EOS
Sample 2 + EOS
Sample 3 + EOS
        ↓
Packed Sequence
```

Bu:

* GPU utilization'ni yaxshilash;
* padding miqdorini kamaytirish;
* training efficiency'ni oshirish

uchun ishlatiladi.

---

# 22. Input / Target Shift

Causal Language Modeling'da model keyingi tokenni bashorat qiladi.

Example:

```text
Input:
[A, B, C, D]

Target:
[B, C, D, E]
```

Shunday qilib:

```text
Current Token
      ↓
Predict Next Token
```

modelning asosiy training objective'i bo‘ladi.

---

# 23. Dataset Statistics

Preprocessingdan keyin quyidagi statistikalar saqlanadi:

```text
Input samples
Empty samples removed
Invalid samples removed
Filtered samples
Duplicates removed
Final samples
Train samples
Validation samples
Test samples
Average instruction length
Average response length
Minimum length
Maximum length
Total characters
Estimated tokens
```

Example report:

```text
================ DATASET REPORT ================

Raw samples:              111183
Empty removed:            ...
Invalid removed:          ...
Filtered:                 ...
Duplicates removed:       ...
Final samples:            ...

Train:                    ...
Validation:               ...
Test:                     ...

==================================================
```

Aniq qiymatlar preprocessing tugagandan keyin avtomatik generatsiya qilinadi.

---

# 24. Known Limitations

Dataset bilan bog‘liq mumkin bo‘lgan cheklovlar:

### 1. Synthetic Data

Instructionlarning bir qismi synthetic generation orqali yaratilgan bo‘lishi mumkin.

Shuning uchun barcha responses bir xil sifat darajasida bo‘lmasligi mumkin.

### 2. Code Correctness

Datasetdagi barcha kodlar avtomatik ravishda production-level correctness kafolatiga ega emas.

### 3. Language Coverage

Dataset asosan programming-related contentga yo‘naltirilgan va barcha programming language'larni teng darajada qamrab olmasligi mumkin.

### 4. Bias

Dataset source va generation process'iga bog‘liq bias mavjud bo‘lishi mumkin.

### 5. Hallucination

Datasetdan o‘qitilgan model ham noto‘g‘ri programming explanation yoki code generation qilishi mumkin.

---

# 25. Data Quality Goals

AI Coding Mentor uchun asosiy data quality maqsadlari:

```text
High-quality instructions
        +
Correct code
        +
Useful explanations
        +
Low duplication
        +
Clean formatting
        +
Consistent structure
```

Target:

```text
Quality > Quantity
```

Ko‘proq dataset har doim ham yaxshiroq model degani emas.

---

# 26. Dataset Versioning

Dataset preprocessing versiyalari alohida belgilanadi.

Example:

```text
raw-v1
cleaned-v1
filtered-v1
final-v1
```

Agar preprocessing qoidalari o‘zgarsa:

```text
final-v2
```

kabi yangi versiya yaratiladi.

Bu model natijalarini qayta ishlab chiqarish uchun kerak.

---

# 27. Reproducibility

Dataset preprocessing deterministic bo‘lishi uchun random seed belgilanadi.

Example:

```python
RANDOM_STATE = 42
```

Dataset split ham shu seed orqali amalga oshiriladi.

```python
train_test_split(
    data,
    test_size=0.1,
    random_state=42
)
```

---

# 28. Storage Structure

Dataset pipeline quyidagicha saqlanadi:

```text
data/
│
├── raw/
│   └── magicoder_evol_instruct_110k.jsonl
│
├── cleaned/
│   └── magicoder_cleaned.jsonl
│
├── filtered/
│   └── magicoder_filtered.jsonl
│
├── final/
│   ├── train.jsonl
│   ├── validation.jsonl
│   └── test.jsonl
│
└── processed/
    ├── train.bin
    ├── validation.bin
    ├── test.bin
    └── meta.json
```

---

# 29. Relationship to Model Training

Dataset ikki xil training stage bilan bog‘lanadi.

```text
Programming Corpus
        ↓
   PRETRAINING
        ↓
     Base LLM
        ↓
Magicoder-Evol-Instruct-110K
        ↓
       SFT
        ↓
AI Coding Mentor
```

Magicoder-Evol-Instruct-110K asosan **instruction tuning / SFT** bosqichida ishlatiladi.

Full pretraining uchun alohida programming corpus ishlatilishi mumkin.

---

# 30. Final Dataset Objective

Final datasetning maqsadi:

```text
High-quality
      +
Clean
      +
Deduplicated
      +
Instruction-oriented
      +
Programming-focused
      ↓
AI Coding Mentor
```

Model foydalanuvchiga:

```text
Question
   ↓
Understand
   ↓
Explain
   ↓
Generate / Fix Code
   ↓
Give Helpful Answer
```

jarayonini amalga oshirishga o‘rgatiladi.

---

# 31. Ethical and Responsible Use

AI Coding Mentor tomonidan yaratilgan kod inson tomonidan tekshirilishi kerak.

Model:

* xavfsizlik-kritik kod;
* production system;
* authentication;
* payment systems;
* infrastructure;
* sensitive applications

uchun inson nazoratisiz ishlatilmasligi kerak.

Modelning javoblari har doim ham to‘g‘ri bo‘lmasligi mumkin.

---

# 32. Citation

Agar datasetdan foydalanish yoki uni qayta tarqatish talablariga ko‘ra citation kerak bo‘lsa, datasetning Hugging Face sahifasi va original project/publication ma'lumotlari ko‘rsatiladi.

Dataset:

https://huggingface.co/datasets/ise-uiuc/Magicoder-Evol-Instruct-110K

Project documentationda dataset manbasi saqlanadi.

---

# 33. Summary

**AI Coding Mentor Dataset Pipeline:**

```text
Magicoder-Evol-Instruct-110K
            ↓
         Raw Data
            ↓
        Inspection
            ↓
         Cleaning
            ↓
        Filtering
            ↓
      Deduplication
            ↓
       Dataset Split
            ↓
      Final JSONL
            ↓
        Tokenizer
            ↓
        Token IDs
            ↓
        Binary .bin
            ↓
       Model Training
            ↓
          SFT
            ↓
      AI Coding Mentor
```

---

## Dataset Status

```text
Dataset: Magicoder-Evol-Instruct-110K
Purpose: AI Coding Mentor SFT
Status: In Development
Preprocessing: Planned / Active
Tokenizer: Custom
Model: Custom Local Transformer
Inference: Local
```

**Project:** AI Coding Mentor

**Goal:** Build a small programming-focused Local LLM from the data preparation stage to local inference.
