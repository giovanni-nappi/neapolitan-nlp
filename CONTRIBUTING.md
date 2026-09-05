# Contributing to Neapolitan Digital Infrastructure (NDI) 🌋

Thank you for your interest in contributing to the **Neapolitan Digital Infrastructure (NDI)** project! Whether you are a software engineer, computational linguist, academic, or native speaker, your contributions help build an open, accessible digital future for the Neapolitan language.

[English](#-english) | [Italiano](#-italiano)

---

<a name="english"></a>
## 🇬🇧 English

### Code of Conduct
By participating in this project, you agree to maintain a welcoming, respectful, and collaborative environment. We value constructive feedback, scientific/linguistic rigor, and open community debate.

### How You Can Contribute

#### 1. Datasets & Dictionaries (`/data`)
* **Dictionary Entries:** Help expand our lemmatized JSON wordlists in `data/dictionary/`. Ensure entries match our schema in `data/schemas/dictionary_entry.schema.json`.
* **Parallel Corpora:** Add aligned sentence pairs (Neapolitan ↔ Italian / English) to `data/corpus/`. Please ensure Neapolitan sentences adhere to our Minimum Viable Orthography (MVO) standards.

#### 2. Software & Tooling (`/src`)
* **Python Tools (`napoli_nlp`):** Improve tokenization, lemmatization algorithms, and clitic handling.
* **Integrations:** Help build desktop/mobile keyboard layouts, browser extensions, or Hunspell spell-checker dictionaries.
* **Tests:** Write unit tests using `pytest` inside `src/tests/` to maintain code stability.

#### 3. AI Prompts & Agents (`/prompts`)
* Refine agent system prompts (`prompts/roles/`) or data collection workflows (`prompts/workflows/`) to increase AI accuracy when assisting with dataset extraction.

#### 4. Orthography & Linguistics (`/docs`)
* Participate in **RFC (Request for Comments)** discussions on GitHub regarding spelling standards, schwa representations, and metaphony rules.

---

### Pull Request (PR) Workflow

1. **Fork the Repository:** Create your own fork on GitHub.
2. **Create a Feature Branch:**
   ```bash
   git checkout -b feat/add-new-lemmas
   # or
   git checkout -b fix/tokenizer-clitic-bug
   ```
3. **Validate Data & code:**
* Ensure JSON data validates against `/data/schemas/`.
* Run Python tests: `pytest src/`
4. **Commit with Clear Messages:** Follow Conventional Commits convention:
* `feat`: add 500 new verbs to dictionary
* `fix`: handle leading apostrophes in tokenizer
* `docs`: update orthography RFC-001
5. *Open a PR*: Submit your Pull Request against the `main` branch with a description of the changes.

---

<a name="italiano"></a>
## 🇮🇹 Italiano

### Codice di Comportamento
Partecipando a questo progetto, accetti di mantenere un ambiente accogliente, rispettoso e
collaborativo.
Valorizziamo il feedback costruttivo, il rigore scientifico/linguistico e la discussione aperta.

### Come Puoi Contribuire
#### 1. Dataset e Dizionari (`/data`)
* *Lemmi del Dizionario:* Aiutaci a espandere i dizionari JSON in `data/dictionary/`.
Assicurati che le voci siano conformi allo schema in `data/schemas/dictionary_entry.schema.json`.
* *Corpora Paralleli*: Aggiungi frasi allineate (Napoletano ↔ Italiano / Inglese) in `data/corpus/`.
Le frasi in napoletano devono seguire le linee guida dell'Ortografia Minima Funzionale (MVO).
#### 2. Software e Strumenti (`/src`)
* *Libreria Python (`napoli_nlp`)*: Migliora i moduli di tokenizzazione, lemmatizzazione e la
gestione delle enclitiche/proclitiche.
* *Integrazioni*: Contribuisci alla creazione di layout per tastiere, estensioni browser o dizionari
di correzione ortografica Hunspell.
* *Test:* Scrivi unit test utilizzando pytest nella cartella `src/tests/` per garantire la stabilità
del codice.
#### 3. Prompt e Agenti AI (`/prompts`)
Perfeziona i prompt di sistema (`prompts/roles/`) o i workflow di estrazione dati
(`prompts/workflows/`) per migliorare la precisione dei modelli AI nel supporto al progetto.
#### 4. Ortografia e Linguistica (`/docs`)
* Partecipa alle discussioni *RFC (Request for Comments)* su GitHub riguardanti le regole
ortografiche, la rappresentazione dello schwa e la metafonia.

### Procedura per le Pull Request (PR)
1. Fai un Fork del Repository: Crea una copia del progetto sul tuo account GitHub.
2. Crea un Branch Dedicato:
```shell
git checkout -b feat/nuovi-lemmi
# oppure
git checkout -b fix/bug-tokenizer
```
3. **Verifica Dati e Codice:**
* Assicurati che i dati JSON siano validi secondo gli schemi in `/data/schemas/`.
* Esegui i test Python: `pytest src/`
4. **Fai il Commit con Messaggi Chiari:** Segui la convenzione *Conventional Commits*:
* `feat`: aggiungi 500 nuovi verbi al dizionario
* `fix`: gestisci gli apostrofi iniziali nel tokenizer
* `docs`: aggiorna RFC-001 sull'ortografia RFC-001
5. **Apri una PR:** Invia la tua Pull Request verso il branch `main` con una descrizione delle
modifiche apportate.
