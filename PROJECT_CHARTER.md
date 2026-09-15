# PROJECT CHARTER

## AI Coding Mentor

**Project Type:** Local Large Language Model (LLM)
**Project Domain:** Programming Education and Code Assistance
**Project Status:** Development
**Primary Language:** Python
**Repository:** AI_Coding_Mentor

---

## 1. Project Overview

**AI Coding Mentor** — dasturlashni o‘rganayotgan foydalanuvchilarga yordam berish uchun ishlab chiqilayotgan lokal Large Language Model (LLM) loyihasidir.

Loyiha foydalanuvchiga kod yozish, kodni tushuntirish, xatolarni aniqlash va tuzatish, algoritmlar bo‘yicha yordam berish hamda dasturlash savollariga javob berish imkoniyatlarini taqdim etishni maqsad qiladi.

Model imkon qadar lokal muhitda ishlashi rejalashtiriladi. Bu foydalanuvchining kodlari va ma'lumotlarini tashqi API xizmatlariga yubormasdan ishlash imkonini beradi.

---

## 2. Project Purpose

Loyihaning asosiy maqsadi — dasturlash bo‘yicha ta'lim va amaliy yordam uchun kichik, tushunarli va lokal ishlaydigan LLM yaratish.

Model quyidagi vazifalarni bajarishga yo‘naltiriladi:

* Code Generation
* Code Explanation
* Bug Fixing
* Algorithm Explanation
* Programming Q&A
* Code Completion
* Learning Assistance

---

## 3. Problem Statement

Dasturlashni o‘rganayotgan foydalanuvchilar ko‘pincha:

* kod yozishda;
* syntax xatolarini topishda;
* algoritmlarni tushunishda;
* mavjud kodni optimallashtirishda;
* error sabablarini aniqlashda;
* dasturlash tushunchalarini o‘rganishda

yordamga muhtoj bo‘ladi.

Ko‘plab zamonaviy AI coding assistantlar tashqi server va API xizmatlariga bog‘liq.

**AI Coding Mentor** loyihasi ushbu muammoga lokal model orqali yechim berishni maqsad qiladi.

---

## 4. Project Objectives

### Primary Objectives

1. Programming-oriented dataset yaratish va tayyorlash.
2. Datasetni cleaning, filtering va deduplication jarayonlaridan o‘tkazish.
3. Programming uchun mos tokenizer yaratish yoki moslashtirish.
4. Tokenlarni binary formatda saqlash.
5. Decoder-only Transformer architecture asosida LLM yaratish.
6. Modelni pretraining orqali o‘qitish.
7. Instruction/SFT dataset yordamida modelni instruction-following uchun moslashtirish.
8. Model sifatini evaluation orqali tekshirish.
9. Lokal inference tizimini yaratish.
10. Foydalanuvchi bilan ishlaydigan AI Coding Mentor interfeysini yaratish.

### Secondary Objectives

* Reproducible training pipeline yaratish.
* Dataset va model versiyalarini nazorat qilish.
* Training checkpointlarini saqlash.
* Model performance statistikalarini kuzatish.
* Kod sifati va javob sifatini alohida baholash.

---

## 5. Project Scope

### In Scope

Loyiha quyidagi komponentlarni o‘z ichiga oladi:

* Dataset collection
* Dataset inspection
* Data cleaning
* Data filtering
* Deduplication
* Train/validation/test split
* Tokenizer training
* Token encoding
* Binary dataset creation
* Transformer model implementation
* Pretraining
* Supervised Fine-Tuning (SFT)
* Checkpoint management
* Evaluation
* Local inference
* Code generation
* Code explanation
* Bug fixing
* Documentation
* Testing

### Out of Scope

Quyidagi imkoniyatlar loyihaning boshlang‘ich versiyasiga kiritilmaydi:

* Internet orqali real-time web search
* Katta production-scale distributed training
* Commercial API platformasi
* Multimodal image understanding
* Voice assistant
* Large-scale cloud deployment
* General-purpose AGI

---

## 6. Target Users

Asosiy foydalanuvchilar:

* Beginner programmers
* Computer Science students
* Programming students
* Junior developers
* ML/LLM o‘rganuvchilar
* Coding practice qilayotgan foydalanuvchilar

---

## 7. Target Programming Tasks

Model quyidagi programming vazifalariga yo‘naltiriladi:

### Code Generation

Foydalanuvchi bergan talab asosida kod yaratish.

### Code Explanation

Mavjud kodni sodda va tushunarli qilib tushuntirish.

### Bug Fixing

Koddagi xatolarni aniqlash va tuzatish.

### Algorithm Assistance

Algoritmlarning ishlash prinsipini tushuntirish va implementatsiya qilish.

### Programming Questions

Python, data structures, algorithms va boshqa programming mavzulari bo‘yicha savollarga javob berish.

---

## 8. Data Strategy

Loyihaning asosiy instruction/SFT datasetlaridan biri:

**Magicoder-Evol-Instruct-110K**

Dataset programming-oriented instruction va response juftliklaridan foydalanib modelni coding-related instruction following vazifalariga moslashtirish uchun ishlatiladi.

Dataset pipeline:

```text
Raw Dataset
     ↓
Inspection
     ↓
Cleaning
     ↓
Filtering
     ↓
Deduplication
     ↓
Train / Validation / Test Split
     ↓
Tokenization
     ↓
Binary Dataset
     ↓
Training
```

Dataset uchun asosiy hujjat:

```text
DATASET_CARD.md
```

---

## 9. Model Strategy

Model decoder-only Transformer architecture asosida quriladi.

Asosiy komponentlar:

```text
Token Embedding
       ↓
Positional Information
       ↓
Transformer Blocks
       ↓
Multi-Head Self-Attention
       ↓
Feed Forward Network
       ↓
Normalization
       ↓
Language Modeling Head
       ↓
Next Token Prediction
```

Model autoregressive language modeling prinsipida ishlaydi.

Modelning asosiy vazifasi:

> Berilgan tokenlar ketma-ketligidan keyingi tokenni prediction qilish.

---

## 10. Training Strategy

Training ikki asosiy bosqichga ajratiladi.

### Stage 1 — Pretraining

Model katta programming corpus orqali language modeling vazifasini o‘rganadi.

Asosiy maqsad:

```text
Input Tokens → Next Token Prediction
```

### Stage 2 — Supervised Fine-Tuning

Model instruction-response formatidagi dataset yordamida coding assistant sifatida moslashtiriladi.

Misol:

```text
Instruction:
Write a Python function to calculate factorial.

Response:
def factorial(n):
    ...
```

SFT bosqichining maqsadi modelni foydalanuvchi instructionlariga mos javob berishga o‘rgatishdir.

---

## 11. Data Processing Requirements

Dataset trainingdan oldin quyidagi tekshiruvlardan o‘tishi kerak:

### Cleaning

* Empty records
* Invalid records
* Excessive whitespace
* Invalid formatting
* Unnecessary metadata

### Filtering

* Minimum text length
* Maximum text length
* Invalid content
* Extremely repetitive samples
* Low-quality samples

### Deduplication

Bir xil yoki juda o‘xshash namunalarni kamaytirish uchun deduplication amalga oshiriladi.

Exact duplicate detection uchun SHA-256 hashing ishlatilishi mumkin.

---

## 12. Dataset Split

Dataset quyidagi qismlarga ajratiladi:

```text
Train       → 90%
Validation  → 5%
Test        → 5%
```

### Train

Modelni o‘qitish uchun ishlatiladi.

### Validation

Training davomida model performance monitoring uchun ishlatiladi.

### Test

Yakuniy evaluation uchun ishlatiladi.

Test dataset training jarayonida ishlatilmasligi kerak.

---

## 13. Tokenizer Strategy

Tokenizer programming code uchun mos bo‘lishi kerak.

Tokenizer quyidagi talablarni bajarishi kerak:

* Code tokenlarini samarali ajratish
* Common programming symbols bilan ishlash
* Python syntaxini yaxshi saqlash
* Special tokensni qo‘llab-quvvatlash
* Encode/decode consistency
* Compact token representation

Muhim special tokenlar:

```text
<BOS>
<EOS>
<PAD>
<UNK>
```

Tokenizer quality quyidagilar orqali tekshiriladi:

* Token fertility
* Compression ratio
* Round-trip test
* Vocabulary coverage

---

## 14. Binary Dataset

Tokenized dataset training uchun binary formatga o‘tkaziladi.

Masalan:

```text
train.bin
validation.bin
test.bin
```

Token ID lar integer formatda saqlanadi.

Dataset metadata:

```text
meta.json
```

faylida saqlanadi.

Metadata quyidagilarni o‘z ichiga olishi mumkin:

* vocabulary size
* special token IDs
* dataset sizes
* tokenizer information
* sequence length
* encoding information

---

## 15. Sequence Packing

Training samaradorligini oshirish uchun tokenlar fixed-length sequence'larga joylashtiriladi.

Masalan:

```text
Token Stream
↓
[1024 tokens]
[1024 tokens]
[1024 tokens]
...
```

Bu GPU memory va training computation'dan samaraliroq foydalanishga yordam beradi.

---

## 16. Input-Target Shift

Autoregressive trainingda input va target bir token pozitsiyasiga siljitiladi.

Masalan:

```text
Input:
I love Python

Target:
love Python <EOS>
```

Model har bir pozitsiyada keyingi tokenni prediction qiladi.

---

## 17. Evaluation Strategy

Model quyidagi yo‘nalishlarda baholanadi:

### Code Generation

Modelning berilgan instruction asosida kod yaratish qobiliyati.

### Code Explanation

Kodning ma'nosi va ishlash prinsipini tushuntirish qobiliyati.

### Bug Fixing

Xatoli kodni to‘g‘rilash qobiliyati.

### Instruction Following

Berilgan talablarni to‘g‘ri bajarish qobiliyati.

### Language Modeling

Validation loss va perplexity kabi metrikalar orqali baholash.

---

## 18. Evaluation Metrics

Asosiy metrikalar:

```text
Training Loss
Validation Loss
Perplexity
Exact Match
Code Execution Success
Pass Rate
```

Code generation uchun imkon qadar generated code avtomatik execution testlari orqali tekshiriladi.

---

## 19. Project Deliverables

Loyiha yakunida quyidagi natijalar olinishi kerak:

* Processed dataset
* Tokenizer
* Binary dataset
* Model architecture
* Pretrained checkpoint
* SFT checkpoint
* Evaluation results
* Inference script
* Chat interface
* Documentation
* Tests
* Model Card
* Dataset Card

---

## 20. Project Structure

```text
AI_Coding_Mentor/
│
├── README.md
├── PROJECT_CHARTER.md
├── MODEL_CARD.md
├── DATASET_CARD.md
├── LICENSE
├── requirements.txt
├── pyproject.toml
│
├── configs/
├── data/
├── dataset/
├── tokenizer/
├── model/
├── training/
├── checkpoints/
├── evaluation/
├── inference/
├── deployment/
├── scripts/
├── tests/
├── notebooks/
└── logs/
```

---

## 21. Risks and Mitigation

| Risk                       | Impact | Mitigation                    |
| -------------------------- | ------ | ----------------------------- |
| Low-quality data           | High   | Cleaning and filtering        |
| Duplicate samples          | Medium | Deduplication                 |
| Data leakage               | High   | Dataset split validation      |
| Poor tokenizer efficiency  | High   | Tokenizer evaluation          |
| Overfitting                | High   | Validation monitoring         |
| Insufficient training data | High   | Additional programming corpus |
| Hallucinated code          | High   | Execution-based evaluation    |
| Limited hardware           | High   | Small model architecture      |
| Training instability       | High   | Checkpoints and monitoring    |
| Incorrect answers          | High   | Test suites and evaluation    |

---

## 22. Hardware Considerations

Initial development kichik model va mavjud local hardware imkoniyatlariga moslashtiriladi.

Training quyidagi muhitlarda amalga oshirilishi mumkin:

* Local GPU
* Google Colab
* Cloud GPU

Model size va sequence length mavjud GPU memory'ga qarab belgilanadi.

---

## 23. Reproducibility

Training natijalarini qayta olish imkoniyati uchun quyidagilar version-control qilinadi:

* Dataset version
* Dataset preprocessing configuration
* Tokenizer configuration
* Model configuration
* Training configuration
* Random seed
* Python dependencies
* Checkpoints
* Evaluation configuration

Asosiy configuration fayllari:

```text
configs/
├── pretrain_config.yaml
├── sft_config.yaml
├── tokenizer_config.yaml
└── evaluation_config.yaml
```

---

## 24. Success Criteria

Loyiha quyidagi holatlarda muvaffaqiyatli deb hisoblanadi:

* Dataset pipeline to‘liq ishlashi.
* Tokenizer datasetni xatosiz encode/decode qilishi.
* Binary dataset muvaffaqiyatli yaratilishi.
* Transformer model trainingni bajara olishi.
* Validation loss monitoring qilinishi.
* SFT modeli instructionlarni qabul qilishi.
* Model Python/code-related vazifalarda ishlaydigan javoblar bera olishi.
* Code generation natijalari avtomatik testlar orqali baholanishi.
* Lokal inference ishlashi.
* Loyihaning barcha asosiy qismlari hujjatlashtirilishi.

---

## 25. Project Milestones

### Milestone 1 — Project Setup

* Repository yaratish
* Folder structure
* Environment
* Dependencies
* Configuration

### Milestone 2 — Dataset

* Dataset download
* Inspection
* Cleaning
* Filtering
* Deduplication
* Split

### Milestone 3 — Tokenizer

* Vocabulary
* Special tokens
* Training
* Encoding
* Decoding
* Evaluation

### Milestone 4 — Preprocessing

* Tokenization
* Sequence packing
* Binary dataset
* Metadata

### Milestone 5 — Model

* Transformer
* Attention
* Feed Forward
* Embeddings
* Normalization
* Generation

### Milestone 6 — Training

* Pretraining
* Checkpointing
* Validation
* SFT

### Milestone 7 — Evaluation

* Code generation
* Code explanation
* Bug fixing
* Execution tests
* Metrics

### Milestone 8 — Inference

* Local generation
* Chat interface
* Prompt template

### Milestone 9 — Documentation

* README
* PROJECT_CHARTER
* DATASET_CARD
* MODEL_CARD
* Technical documentation

---

## 26. Project Constraints

Loyiha quyidagi cheklovlar asosida ishlab chiqiladi:

* Limited GPU resources
* Limited training time
* Limited dataset size
* Limited model parameters
* Local hardware limitations
* Dataset license requirements

Ushbu cheklovlar sabab modelning imkoniyatlari katta commercial LLMlar bilan bir xil bo‘lishi kutilmaydi.

---

## 27. Ethical and Responsible Use

AI Coding Mentor quyidagi maqsadlarda ishlatilishi ko‘zda tutiladi:

* Programming education
* Code assistance
* Learning
* Debugging
* Experimentation
* Research

Model tomonidan yaratilgan kodni production muhitiga qo‘yishdan oldin foydalanuvchi tomonidan tekshirilishi kerak.

Model javoblari har doim ham to‘g‘ri bo‘lmasligi mumkin.

---

## 28. Project Governance

Project development quyidagi prinsiplar asosida olib boriladi:

* Version control orqali source code boshqarish
* Documentation bilan har bir asosiy componentni hujjatlashtirish
* Reproducible experiments
* Dataset va model versioning
* Automated testing
* Evaluation before release

---

## 29. Final Project Vision

AI Coding Mentor yakuniy holatda foydalanuvchi bilan lokal muhitda ishlaydigan programming assistant bo‘lishi ko‘zda tutiladi.

Umumiy pipeline:

```text
                  ┌─────────────────┐
                  │ Programming Data│
                  └────────┬────────┘
                           ↓
                  ┌─────────────────┐
                  │ Data Processing │
                  └────────┬────────┘
                           ↓
                  ┌─────────────────┐
                  │    Tokenizer    │
                  └────────┬────────┘
                           ↓
                  ┌─────────────────┐
                  │ Binary Dataset  │
                  └────────┬────────┘
                           ↓
                  ┌─────────────────┐
                  │   Pretraining   │
                  └────────┬────────┘
                           ↓
                  ┌─────────────────┐
                  │      SFT        │
                  └────────┬────────┘
                           ↓
                  ┌─────────────────┐
                  │    Evaluation   │
                  └────────┬────────┘
                           ↓
                  ┌─────────────────┐
                  │ Local Inference │
                  └────────┬────────┘
                           ↓
                  ┌─────────────────┐
                  │ AI Coding Mentor│
                  └─────────────────┘
```

---

## 30. Final Statement

**AI Coding Mentor** loyihasining asosiy maqsadi — programming vazifalariga yo‘naltirilgan, tushunarli architecture va reproducible training pipeline asosida ishlab chiqilgan lokal LLM yaratish.

Loyiha dataset tayyorlashdan boshlab tokenizer, Transformer architecture, pretraining, SFT, evaluation va local inferencegacha bo‘lgan to‘liq LLM development lifecycle'ni amaliy ravishda namoyish etadi.

**Project Goal:**

> Build a small, local, programming-oriented Large Language Model that can assist users with code generation, code explanation, debugging, and programming education.
