# Neapolitan Digital Infrastructure (NDI) 🌋
> An open-source, bottom-up digital infrastructure and NLP ecosystem for the Neapolitan language (`nap`).

[![License: AGPL v3](https://img.shields.io/badge/License-AGPLv3-blue.svg)](LICENSE)
[![Data License: CC BY-NC-SA 4.0](https://img.shields.io/badge/Data-CC%20BY--NC--SA%204.0-orange.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

[English](#-english) | [Italiano](#-italiano)

---

<a name="english"></a>
## 🇬🇧 English

### Overview
Neapolitan (`nap`) is recognized by UNESCO as a vulnerable language spoken by over 7 million people
across Southern Italy.
Despite its rich literary history, it lacks standardized digital infrastructure—such as open-source
spell-checkers, machine-readable dictionaries, and NLP processing pipelines.

The **Neapolitan Digital Infrastructure (NDI)** project bypasses institutional gridlock by adopting
a software engineering approach:
1. **Minimum Viable Orthography (MVO):** Codifying a pragmatic, developer-friendly written baseline
optimized for standard Latin-1/ASCII keyboards.
2. **Structured Datasets:** Building open, machine-readable dictionaries (JSON/SQL) with POS, IPA
phonetics, and metaphonic markers.
3. **Language Engineering Tools:** Developing Hunspell spell-checkers, Python tokenizers
(`napoli-nlp`), and LLM fine-tuning pipelines.

### 📁 Repository Structure
```text
neapolitan-nlp/
├── docs/                 # Architectural specs & Orthography RFCs (EN / IT)
├── data/                 # Core Datasets (JSON schemas, dictionary entries, corpora)
├── src/                  # Source code for `napoli_nlp` Python tools & CLI
├── prompts/              # System prompts & roles for AI-assisted workflows
├── .github/              # Issue templates, PR guidelines, and CI/CD workflows
├── CONTRIBUTING.md       # Contribution guidelines for developers & linguists
└── LICENSE               # Dual license (AGPLv3 for code, CC BY-NC-SA for data)
```

### 🤖 AI-Assisted Workflows
This repository utilizes structured AI workflows (/prompts) to accelerate dataset generation and
rule verification.
Custom agent personas, such as linguist_agent and data_engineer_agent, ensure that generated data
adheres strictly to linguistic principles and JSON validation schemas.

### 🛠️ Getting Started
```bash
# Clone the repository
git clone [https://github.com/giovanni-nappi/neapolitan-nlp.git](https://github.com/giovanni-nappi/neapolitan-nlp.git)
cd neapolitan-nlp

# Install the Python package in editable mode
pip install -e src/
```

---

<a name="italiano"></a>
## 🇮🇹 Italiano

### Descrizione del Progetto
Il napoletano (`nap`) è riconosciuto dall'UNESCO come lingua vulnerabile parlata da oltre 7 milioni
di persone.
Nonostante una ricca tradizione letteraria, il napoletano soffre della mancanza di un'infrastruttura
digitale standardizzata: correttori ortografici open-source, dizionari strutturati e pipeline per
l'elaborazione del linguaggio naturale (NLP).

Il progetto **Neapolitan Digital Infrastructure (NDI)** adotta un approccio ingegneristico e bottom-up
per superare la stasi istituzionale:
1. ***Ortografia Minima Funzionale (MVO):*** Definizione di uno standard pratico orientato alla
facilità di digitazione su tastiere standard.
2. ***Dataset Strutturati:*** Creazione di dizionari aperti e leggibili da macchina (JSON/SQL)
completi di POS, trascrizione IPA e metafonia.
3. ***Strumenti di Sviluppo:*** Realizzazione di dizionari Hunspell per correzione ortografica,
librerie Python (napoli-nlp) e dataset di addestramento per LLM.

### 🤝 Come Contribuire
Sviluppatori, linguisti, ricercatori e madrelingua sono i benvenuti!
Per iniziare a contribuire con codice, dataset o documentazione, consulta la nostra guida
CONTRIBUTING.md.

---

### 📄 License & Attribution
The Neapolitan Digital Infrastructure (NDI) project uses a hybrid open-source licensing model
designed to preserve author attribution, enforce open collaboration, and prevent unauthorized
commercial exploitation:
* **Software & Code (`/src`, `/prompts`, scripts):** Licensed under the GNU AGPLv3.
Any network service, application, or software platform using this code must release its source code
under the same license.
* **Datasets & Corpora (`/data`):** Licensed under CC BY-NC-SA 4.0.
You are free to share and adapt the data for non-commercial, educational, and research purposes,
provided attribution is given and modified datasets remain open.

### 👤 Author & Attribution
This project was initiated by Giovanni Nappi and the NDI core engineering team.

When citing or attributing this work, please use the following format:

> Neapolitan Digital Infrastructure (NDI), Lead Author: Giovanni Nappi (2026). GitHub repository: https://github.com/giovanni-nappi/neapolitan-nlp

💼 Commercial Licensing
For commercial use, proprietary software integration, or custom licensing agreements that fall outside AGPLv3 / CC BY-NC-SA parameters, please reach out directly to the maintainers.
