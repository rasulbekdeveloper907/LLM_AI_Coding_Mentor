# 🤖 AI Coding Mentor

> **A Local Large Language Model for Programming Education, Code Generation, Explanation, and Debugging**

AI Coding Mentor — bu dasturlashni o‘rganayotgan foydalanuvchilarga yordam berish uchun ishlab chiqilayotgan **local LLM (Large Language Model)** loyihasi.

Loyiha maqsadi — Hugging Face'dagi programming datasetlardan foydalanib, datasetni tozalash va tayyorlashdan boshlab, **tokenizer → tokenization → pretraining → supervised fine-tuning (SFT) → evaluation → local inference** bosqichlarigacha bo‘lgan to‘liq LLM pipeline'ni mustaqil qurish.

Model internet yoki tashqi API'ga bog‘liq bo‘lmasdan local kompyuterda ishlashi uchun mo‘ljallangan.

---

## 🎯 Project Goal

AI Coding Mentor quyidagi vazifalarni bajarishga mo‘ljallangan:

* 💻 Programming savollariga javob berish
* 🐛 Code xatolarini aniqlash
* 🔧 Kodni tuzatishga yordam berish
* 📚 Programming mavzularini tushuntirish
* 🧩 Algoritm va masalalarni tushuntirish
* ✍️ Kod yozishda yordam berish
* 🔍 Kodni tahlil qilish
* ⚡ Kodni yaxshilash bo‘yicha tavsiyalar berish
* 👨‍🏫 Foydalanuvchiga mentor sifatida tushuntirish

Asosiy prinsip:

```text
User Problem
     ↓
AI Coding Mentor
     ↓
Explanation
     +
Solution
     +
Example
```

Model faqat tayyor kod berish emas, balki **kodning nima sababdan ishlashi yoki ishlamasligini tushuntirishga** yo‘naltiriladi.

---

# 🧠 Project Architecture

Loyihaning umumiy pipeline'i:

```text
                    ┌──────────────────────┐
                    │   Hugging Face       │
                    │     Datasets         │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     Raw Dataset      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Data Cleaning      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Quality Filtering    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Deduplication      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Train / Val / Test   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      Tokenizer       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Token IDs         │
                    │      (.bin)           │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   LLM Pretraining    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Supervised         │
                    │   Fine-Tuning (SFT)  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      Evaluation      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Local Inference    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  AI Coding Mentor    │
                    └──────────────────────┘
```

---

# 📂 Project Structure

```text
AI_Coding_Mentor/
│
├── README.md
├── MODEL_CARD.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── pyproject.toml
│
├── configs/
│   ├── pretrain_config.yaml
│   ├── sft_config.yaml
│   ├── tokenizer_config.yaml
│   └── evaluation_config.yaml
│
├── data/
│   ├── raw/
│   │   └── magicoder_evol_instruct_110k.jsonl
│   │
│   ├── cleaned/
│   │   └── magicoder_cleaned.jsonl
│   │
│   ├── filtered/
│   │   └── magicoder_filtered.jsonl
│   │
│   ├── final/
│   │   ├── train.jsonl
│   │   ├── validation.jsonl
│   │   └── test.jsonl
│   │
│   └── processed/
│       ├── train.bin
│       ├── validation.bin
│       ├── test.bin
│       └── meta.json
│
├── dataset/
│   ├── download_dataset.py
│   ├── inspect_dataset.py
│   ├── clean_dataset.py
│   ├── filter_dataset.py
│   ├── deduplicate.py
│   ├── split_dataset.py
│   └── build_dataset.py
│
├── tokenizer/
│   ├── train_tokenizer.py
│   ├── encode_dataset.py
│   ├── tokenizer.py
│   ├── special_tokens.py
│   ├── tokenizer_config.json
│   ├── vocab.json
│   └── merges.txt
│
├── model/
│   ├── config.py
│   ├── model.py
│   ├── transformer.py
│   ├── attention.py
│   ├── embeddings.py
│   ├── feed_forward.py
│   ├── normalization.py
│   ├── positional_encoding.py
│   └── generation.py
│
├── training/
│   ├── pretrain.py
│   ├── train_sft.py
│   ├── trainer.py
│   ├── dataset_loader.py
│   ├── optimizer.py
│   ├── scheduler.py
│   ├── checkpoint.py
│   └── utils.py
│
├── checkpoints/
│   ├── pretrain/
│   └── sft/
│
├── evaluation/
│   ├── evaluate.py
│   ├── code_generation.py
│   ├── code_explanation.py
│   ├── bug_fixing.py
│   ├── metrics.py
│   └── benchmark.json
│
├── inference/
│   ├── generate.py
│   ├── chat.py
│   └── prompt_template.py
│
├── deployment/
│   ├── app.py
│   ├── api.py
│   └── requirements.txt
│
├── scripts/
│   ├── prepare_data.py
│   ├── train_tokenizer.py
│   ├── preprocess.py
│   ├── pretrain.sh
│   ├── sft.sh
│   └── evaluate.sh
│
├── tests/
│   ├── test_dataset.py
│   ├── test_tokenizer.py
│   ├── test_model.py
│   ├── test_training.py
│   └── test_generation.py
│
├── notebooks/
│   ├── 01_dataset_exploration.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_tokenizer.ipynb
│   ├── 04_pretraining.ipynb
│   ├── 05_sft.ipynb
│   └── 06_evaluation.ipynb
│
└── logs/
    ├── preprocessing/
    ├── training/
    └── evaluation/
```

---

# 📊 Dataset

## Primary SFT Dataset

Loyihaning instruction tuning bosqichida **Magicoder-Evol-Instruct-110K** datasetidan foydalanish rejalashtirilgan.

Dataset:

**`ise-uiuc/Magicoder-Evol-Instruct-110K`**

Hugging Face:

https://huggingface.co/datasets/ise-uiuc/Magicoder-Evol-Instruct-110K

Dataset programming-related instruction va response juftliklaridan tashkil topgan.

Asosiy struktura:

```text
instruction
response
```

Misol:

```json
{
  "instruction": "Write a Python function that checks whether a number is prime.",
  "response": "def is_prime(n):\n    ..."
}
```

### Dataset Pipeline

```text
Magicoder-Evol-Instruct-110K
            ↓
          Raw
            ↓
         Cleaning
            ↓
         Filtering
            ↓
       Deduplication
            ↓
      Train / Validation
            ↓
          Tokenizer
            ↓
        Model Training
```

> **Note:** Magicoder-Evol-Instruct-110K asosan instruction/SFT maqsadlari uchun ishlatiladi. Full pretraining uchun alohida programming/code corpus qo‘shilishi mumkin.

---

# 🧹 Data Processing

Dataset preprocessing quyidagi bosqichlardan iborat:

### 1. Cleaning

* Empty records removal
* Invalid records removal
* Whitespace normalization
* Unicode normalization
* Keraksiz belgilarni tozalash
* Corrupted text filtering

### 2. Quality Filtering

Quyidagi mezonlar tekshiriladi:

```text
Minimum text length
Maximum text length
Alphabetic ratio
Code/text ratio
Repeated content
Invalid characters
```

### 3. Deduplication

Bir xil yoki juda o‘xshash samplelarni kamaytirish uchun deduplication ishlatiladi.

Exact duplicate uchun:

```text
SHA-256 hash
```

ishlatilishi mumkin.

### 4. Dataset Split

Final dataset:

```text
Train       → 90%
Validation  → 5%
Test        → 5%
```

ko‘rinishida ajratilishi mumkin.

---

# 🔤 Tokenizer

Project o‘z tokenizer'iga ega bo‘lishi rejalashtirilgan.

Tokenizer pipeline:

```text
Raw Text
   ↓
Normalization
   ↓
Pre-tokenization
   ↓
BPE
   ↓
Special Tokens
   ↓
Token IDs
```

Tokenizer'da quyidagi special tokenlar ishlatilishi mumkin:

```text
<BOS>
<EOS>
<PAD>
<UNK>
```

Tokenizer sifatini tekshirish uchun round-trip test:

```text
text
 ↓
encode
 ↓
token IDs
 ↓
decode
 ↓
text
```

tekshiriladi.

---

# 🧮 Token Storage

Tokenlar integer ID ko‘rinishida saqlanadi.

```text
Text
 ↓
Token IDs
 ↓
uint16
 ↓
.bin
```

Masalan:

```text
data/processed/
├── train.bin
├── validation.bin
├── test.bin
└── meta.json
```

`meta.json` tokenizer va dataset haqidagi metadata'ni saqlaydi.

Misol:

```json
{
  "vocab_size": 32000,
  "dtype": "uint16",
  "bos_token_id": 1,
  "eos_token_id": 2,
  "pad_token_id": 0
}
```

---

# 🧠 Model Architecture

AI Coding Mentor uchun **decoder-only Transformer language model** ishlatiladi.

Umumiy arxitektura:

```text
Input Tokens
     ↓
Token Embeddings
     ↓
Positional Information
     ↓
Transformer Blocks
     │
     ├── Self Attention
     ├── Feed Forward Network
     ├── Layer Normalization
     └── Residual Connections
     ↓
Language Model Head
     ↓
Logits
     ↓
Next Token Prediction
```

Modelning dastlabki konfiguratsiyasi hardware imkoniyatiga qarab belgilanadi.

Misol:

```text
Parameters      ≈ 100M–300M
Context Length  ≈ 512–2048
Vocabulary      ≈ 32K
Architecture    Decoder-only Transformer
```

> Ushbu qiymatlar boshlang‘ich konfiguratsiya bo‘lib, tajribalar davomida o‘zgartirilishi mumkin.

---

# 🏋️ Training

Training ikki asosiy bosqichga bo‘linadi.

## Stage 1 — Pretraining

Model programming/code corpus orqali language modeling vazifasida o‘qitiladi.

```text
Input:
Write a Python function...

Target:
Python function...
```

Modelning asosiy vazifasi:

> **Next Token Prediction**

ya’ni keyingi tokenni bashorat qilish.

---

## Stage 2 — Supervised Fine-Tuning

SFT bosqichida model instruction-response formatida o‘qitiladi.

```text
User Instruction
       ↓
      LLM
       ↓
Assistant Response
```

Misol:

```text
User:
Explain Python decorators.

Assistant:
A decorator is a function that modifies...
```

Maqsad — modelni oddiy language modeldan **coding mentor**ga moslashtirish.

---

# 📦 Sequence Packing

Training samaradorligini oshirish uchun bir nechta qisqa sample bitta sequence ichiga joylashtirilishi mumkin.

```text
Sample 1 + EOS
Sample 2 + EOS
Sample 3 + EOS
       ↓
Packed Sequence
```

Bu GPU memory'dan samaraliroq foydalanishga yordam beradi.

---

# 🔄 Input / Target Shift

Causal language modeling uchun:

```text
Input:
[A, B, C, D]

Target:
[B, C, D, E]
```

Model har bir token uchun **keyingi tokenni** bashorat qiladi.

---

# 📈 Evaluation

Model quyidagi yo‘nalishlarda baholanadi:

### Code Generation

```text
Prompt
  ↓
Generated Code
  ↓
Syntax / Test Evaluation
```

### Code Explanation

Model kodni qanchalik tushunarli izohlashi tekshiriladi.

### Bug Fixing

Model xatoli kodni tuzata oladimi:

```text
Buggy Code
    ↓
Model
    ↓
Fixed Code
```

### Language Modeling

Validation loss va perplexity kuzatiladi.

Asosiy metrikalar:

```text
Validation Loss
Perplexity
Code Pass Rate
Exact Match
Test Pass Rate
```

---

# 💬 Local Inference

Trained modelni local kompyuterda ishga tushirish:

```bash
python inference/chat.py
```

Misol:

```text
User: What is a Python list?

AI Coding Mentor:
A Python list is an ordered, mutable collection...
```

---

# 🌐 Deployment

Keyingi bosqichda local web interface yaratish mumkin.

```text
Browser
   ↓
Local API
   ↓
AI Coding Mentor
   ↓
Local Transformer
```

Masalan:

```text
http://localhost:8000
```

---

# ⚙️ Installation

Repository'ni clone qilish:

```bash
git clone https://github.com/YOUR_USERNAME/AI_Coding_Mentor.git
cd AI_Coding_Mentor
```

Virtual environment yaratish:

```bash
python -m venv .venv
```

Windows:

```bash
source .venv/Scripts/activate
```

yoki:

```bash
.venv\Scripts\activate
```

Dependencies:

```bash
pip install -r requirements.txt
```

---

# 📥 Dataset Download

Datasetni yuklash:

```bash
python dataset/download_dataset.py
```

Dataset inspection:

```bash
python dataset/inspect_dataset.py
```

---

# 🧹 Data Preparation

Cleaning:

```bash
python dataset/clean_dataset.py
```

Filtering:

```bash
python dataset/filter_dataset.py
```

Deduplication:

```bash
python dataset/deduplicate.py
```

Train/validation/test split:

```bash
python dataset/split_dataset.py
```

---

# 🔤 Train Tokenizer

Tokenizer yaratish:

```bash
python tokenizer/train_tokenizer.py
```

Datasetni tokenize qilish:

```bash
python tokenizer/encode_dataset.py
```

---

# 🧠 Model Training

Pretraining:

```bash
python training/pretrain.py
```

SFT:

```bash
python training/train_sft.py
```

Checkpointlar:

```text
checkpoints/
├── pretrain/
└── sft/
```

---

# 💬 Run the Model

Local chat:

```bash
python inference/chat.py
```

Generation:

```bash
python inference/generate.py
```

---

# 🧪 Testing

Barcha testlarni ishga tushirish:

```bash
pytest tests/
```

Tokenizer:

```bash
pytest tests/test_tokenizer.py
```

Model:

```bash
pytest tests/test_model.py
```

Generation:

```bash
pytest tests/test_generation.py
```

---

# 🔐 Privacy

AI Coding Mentor local ishlashga mo‘ljallangan.

Inference vaqtida foydalanuvchi inputlari tashqi LLM API'lariga yuborilmasligi ko‘zda tutiladi.

Bu architecture local development va offline experimentation uchun mos.

---

# ⚠️ Limitations

Modelning dastlabki versiyalarida quyidagi cheklovlar bo‘lishi mumkin:

* Murakkab programming masalalarida xatolar.
* Noto‘g‘ri yoki ishlamaydigan code generation.
* Hallucination.
* Datasetdagi bias yoki xatolar.
* Kichik model sababli context understanding cheklangan bo‘lishi mumkin.
* Training dataset model imkoniyatlarini sezilarli darajada belgilaydi.

Generated code production environment'da ishlatishdan oldin test qilinishi kerak.

---

# 🚀 Future Improvements

Kelajakda quyidagilar qo‘shilishi mumkin:

* [ ] Ko‘proq programming language
* [ ] Uzbek programming mentor
* [ ] Code execution sandbox
* [ ] Retrieval-Augmented Generation (RAG)
* [ ] Larger context window
* [ ] Better code evaluation
* [ ] Human preference dataset
* [ ] Preference optimization
* [ ] Quantization
* [ ] GPU inference optimization
* [ ] Web UI
* [ ] REST API
* [ ] VS Code extension
* [ ] Automated unit-test generation
* [ ] Code review mode
* [ ] Interactive debugging mode

---

# 🗺️ Development Roadmap

```text
[1] Project Setup
       ↓
[2] Dataset Collection
       ↓
[3] Dataset Inspection
       ↓
[4] Cleaning
       ↓
[5] Filtering
       ↓
[6] Deduplication
       ↓
[7] Dataset Split
       ↓
[8] Tokenizer
       ↓
[9] Tokenization
       ↓
[10] Binary Dataset
       ↓
[11] Transformer
       ↓
[12] Pretraining
       ↓
[13] SFT
       ↓
[14] Evaluation
       ↓
[15] Inference
       ↓
[16] Local Chat
       ↓
[17] Deployment
```

---

# 📚 Learning Objectives

Ushbu loyiha davomida quyidagi LLM tushunchalari amalda o‘rganiladi:

* Dataset collection
* Dataset licensing
* Data cleaning
* Data filtering
* Deduplication
* Train/validation/test split
* BPE tokenizer
* Vocabulary
* Special tokens
* Token fertility
* Compression
* Token IDs
* `uint16`
* `.bin` files
* `meta.json`
* Sequence packing
* Input-target shifting
* Transformer architecture
* Self-attention
* Feed-forward networks
* Residual connections
* Layer normalization
* Causal language modeling
* Pretraining
* SFT
* Checkpointing
* Evaluation
* Local inference
* Model deployment

---

# 📄 License

Project code license information will be defined in the `LICENSE` file.

Dataset licenses are separate from the project code license and must be reviewed according to the terms of each source dataset.

---

# 👨‍💻 Project Status

**Status:** 🚧 Active Development

Current focus:

```text
Dataset
   ↓
Data Preparation
   ↓
Tokenizer
   ↓
Model
```

---

# 🤝 Contributing

Contributions, suggestions, bug reports and improvements are welcome.

Before contributing:

1. Create a branch.
2. Make your changes.
3. Add or update tests where appropriate.
4. Verify the project runs correctly.
5. Submit a pull request.

---

# ⭐ Project Vision

AI Coding Mentor'ning asosiy maqsadi — **kichik, tushunarli va local ishlaydigan programming-oriented LLM'ni noldan qurish**.

Loyiha tayyor API'ni shunchaki ulashdan ko‘ra, LLM yaratishning barcha asosiy bosqichlarini amalda ko‘rsatishga qaratilgan:

```text
Data
 ↓
Tokenizer
 ↓
Model
 ↓
Training
 ↓
Evaluation
 ↓
Inference
 ↓
AI Coding Mentor
```

**Built for learning. Built locally. Built from the ground up.**
