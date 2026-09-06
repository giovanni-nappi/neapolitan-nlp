# Grapheme-to-Phoneme (G2P) Mapping Rules

* **Target Domain:** Text-to-Speech (TTS), Phonetic Transcription
* **Input:** Text standardized in Minimum Viable Orthography (MVO)
* **Output:** Broad phonetic transcription (IPA)

## 1. Abstract

The Neapolitan Minimum Viable Orthography (MVO) is morphosyntactic and etymological.
It anchors spellings to their strong, historical roots to ensure machine readability and seamless
NLP tokenization.

Consequently, MVO text does not explicitly write surface phonetic phenomena like lenition
(weakening), rhotacism, or vowel reduction.
A TTS or phonetic transcription engine must apply G2P sandhi (word-boundary) rules to dynamically
generate the correct pronunciation.

---

## 2. Consonant Lenition (Intervocalic Weakening)

When specific etymological consonants occur in a "weak" phonetic position (typically intervocalic,
such as following a vowel-ending article like `'o`, `'a`, `nu`, `na`), they undergo lenition.
The G2P engine must apply these transformations dynamically.

### 2.1 The `g ➔ v` Shift (Spirantization)
Initial `g` frequently spirantizes into a `v` sound when preceded by a vowel without syntactic
doubling.
* **MVO Text:** `'o gatto` ➔ **TTS Output:** `[o ˈvattə]`
* **MVO Text:** `'a gamma` (the leg) ➔ **TTS Output:** `[a ˈvammə]`
* *Exception:* Following a doubling trigger, the etymological `g` remains and geminates (e.g.,
`'e ggatte` ➔ `[e ˈggattə]`).

### 2.2 The `d ➔ r` Shift (Rhotacism)
Initial (and sometimes internal) `d` transforms into an alveolar tap `[ɾ]` (rhotacism) in
intervocalic positions.
* **MVO Text:** `'o dito` ➔ **TTS Output:** `[o ˈɾitə]`
* **MVO Text:** `'a madonna` ➔ **TTS Output:** `[a maˈɾɔnnə]`
* *Exception:* Following a doubling trigger, the etymological `d` remains and geminates (e.g.,
`'e ddete` ➔ `[e ˈddetə]`).

### 2.3 The `b ➔ v` Shift (Betacism)
Initial `b` softens to a `v` sound in weak intervocalic positions.
* **MVO Text:** `'a barca` ➔ **TTS Output:** `[a ˈvarkə]`
* *Exception:* Following a doubling trigger, the etymological `b` remains and geminates (e.g.,
`'e bbarche` ➔ `[e ˈbbarkə]`).

---

## 3. Voicing Assimilation (Post-Nasal Voicing)

MVO preserves etymological voiceless consonants (`p`, `t`, `c`/`k`).
However, in continuous speech, these consonants assimilate and become voiced (`b`, `d`, `g`) when
immediately following a nasal consonant (`m` or `n`).

* **`p ➔ b`:** *sempe* ➔ `[ˈsɛmbə]`
* **`t ➔ d`:** *mantené* ➔ `[mandəˈne]`
* **`c ➔ g`:** *manco* ➔ `[ˈmaŋgə]`

The G2P engine must apply a regex or sequential check: if `[m, n]` + `[p, t, c]`, apply voicing to
the plosive.

---

## 4. Vowel Reduction (The Schwa)

MVO dictates writing the etymological final unstressed vowels (`-a`, `-e`, `-i`, `-o`) to preserve
metaphonic triggers for lemmatization.

For pan-Neapolitan or urban Neapolitan TTS, the G2P engine must reduce these unstressed final vowels
to a schwa `[ə]`.
* **MVO Text:** *'e priéveti* ➔ **TTS Output:** `[e ˈprjeːvətə]`
* **MVO Text:** *'o russo* ➔ **TTS Output:** `[o ˈrussə]`

*Note: For regional dialect TTS configurations (e.g., peripheral Campanian varieties), this G2P rule
can be disabled to pronounce the full final vowels.*
