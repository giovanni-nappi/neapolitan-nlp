# Dictionary Architecture & Ingestion Strategy

This document outlines the roadmap and architectural decisions for building the Neapolitan NLP
dictionary.
To maintain high linguistic accuracy and keep the data layer scalable, we follow a strict ingestion
protocol.

## The Problem with Web Scraping
We do not accept raw text scraped from the internet or social media to build the core lexicon.
Most Neapolitan text online is written phonetically, lacks grammatical structure, and ignores the
Morphological-Vocalic Orthography (MVO) standard. Ingesting this data directly would pollute the
tokenizer with non-standard variants and Italianisms.

Instead, we use a structured, "clean-room" approach.

## Phase 1: The "Clean Room" Seed
The foundation of the dictionary is built using structured, verified word lists translated directly
into MVO-compliant Neapolitan.
* **Sources:** Swadesh lists, high-frequency core vocabulary, and public domain historical
dictionaries (e.g., Altamura, D'Ambra).
* **Goal:** Establish a robust core of 1,000–2,000 lemmas to provide baseline coverage for the NLP
tools.

## Phase 2: Data Sharding
To prevent the lexicon from becoming a massive, unmaintainable JSON monolith (which causes merge
conflicts and slows down parsing), the dictionary data is sharded.

* **Strategy:** Lemmas are split into distinct JSON files based on their Part of Speech (POS) (e.g.,
`nouns.json`, `verbs.json`, `adjectives.json`).
* **Runtime:** The Python library dynamically reads the shard directory, concatenates the JSON
payloads in memory, and builds the lookup tables for the tokenizer.

## Phase 3: CLI Tooling (No Manual JSON Editing)
To maintain schema integrity, contributors should not manually edit the JSON files.
We use a dedicated Python CLI script (`scripts/add_lemma.py`) for data entry. The script prompts
the user for the lemma, part of speech, translation, and metaphonic triggers, then automatically:
1. Validates the entry against our JSON schemas.
2. Generates necessary feminine/plural forms based on MVO rules.
3. Appends the validated block to the correct POS shard.

## Phase 4: Corpus Mining (Future State)
Only after the core dictionary and tokenizer are stable will we begin processing raw corpus text.
* The tokenizer will parse wild text and flag "Unknown Tokens".
* Maintainers will review this list, filter out slang and misspellings, and feed valid new words
back through the CLI ingestion tool.
