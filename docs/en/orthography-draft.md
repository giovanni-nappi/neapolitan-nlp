# RFC-001: Minimum Viable Orthography (MVO) for Neapolitan NLP

* **Status:** Draft / Proposal
* **Author:** Giovanni Nappi
* **Version:** 0.1.0
* **Target Domain:** Computational Linguistics, Lexicography, NLP Utilities

---

## 1. Abstract & Scope

Neapolitan (*napulitano*) exhibits significant orthographic fragmentation due to historical regional
variations, competing literary traditions, and inconsistent accent mark conventions.

The **Minimum Viable Orthography (MVO)** defines a unified, normalized orthographic standard
optimized for Natural Language Processing (NLP).
The primary goal of MVO is to maximize deterministic rule-based tokenization and morphological
parsing while maintaining human readability and fidelity to classical Neapolitan phonology.

---

## 2. Diacritics & Accents

MVO restricts the character set to standard ISO-8859-1 / UTF-8 Latin characters with explicit accent
rules.

### 2.1 Vocalic Accents
1. **Grave Accent (`à`, `è`, `ì`, `ò`, `ù`):**
   * Marks **open vowels** (`/ɛ/`, `/ɔ/`) in stressed syllables.
   * Compulsory on all oxytone words ending in a vowel (e.g., *parlà*, *sentì*, *pussibbilità*).
2. **Acute Accent (`é`, `ó`):**
   * Marks **closed vowels** (`/e/`, `/o/`) in stressed syllables where disambiguation is needed.
3. **Circumflex Accent (`â`, `ê`, `ô`):**
   * Represents crasis, explicitly used for the fusion of the preposition *a* with definite articles
   (see Section 3.3).
4. **Internal Stress:**
   * Internal stress is generally omitted on regular paroxytones, but **compulsory** on
   proparoxytones (words stressed on the antepenultimate syllable) to assist tokenizers and TTS
   models (e.g., *màneche*, *fémmena*).

### 2.2 Schwa Representation and Etymological Vowels
* Unstressed vowels (particularly in word-final position) that reduce phonologically to the schwa
(`/ə/`) must be rendered using their **etymological vowel** (`a`, `e`, `o`, `i`), rather than being
uniformly replaced by `e` or non-standard symbols like `ə`.
* For example:
  * Etymological `a` (feminine singular): *casa* `/ˈkaːsə/`
  * Etymological `o` (masculine singular): *cuorpo* `/ˈkworpə/`
  * Etymological `e`: *bene* `/ˈbeːnə/`
  * Etymological `i` (masculine plural): *guagliuni* `/waˈʎːuːnə/`
* While IPA transcriptions in the dictionary schema will explicitly define the `/ə/` phoneme, the
MVO text representation strictly preserves the historical grammatical vowel to maintain
morphological traceability.

### 2.3 Morphological Final Vowels (The Plural '-i')
To support algorithmic predictability and disambiguate grammatical number, this standard adopts a
**morphological** approach to final unstressed vowels, prioritizing etymology over the phonetic
schwa (often traditionally written as `e`).

Specifically, **masculine plurals must be written with the etymological `-i`** rather than the
phonetic `-e`.
This explicit `-i` provides the historical trigger for metaphony (vowel mutation) in the root of
the word, making the morphological shift predictable for NLP tools.

**Examples:**
* Singular: *'o prèvete* ➔ Plural: *'e priéveti* (❌ *prievete*)
* Singular: *'o pede* ➔ Plural: *'e piedi* (❌ *piede*)
* Singular: *'o frate* ➔ Plural: *'e frati* (❌ *frate*)
* Singular: *'o libbro* ➔ Plural: *'e libbri* (❌ *libbre*)

This rule also applies to plural adjectives and possessives:
* *russo* / *rossa* / *russi* / *rosse*
* *mio* / *mia* / *mieji* / *meje*

**Note on Pronunciation:** While the final `-i` is standardized in spelling, it is understood that
in many spoken varieties of Neapolitan, this vowel is phonetically reduced to a schwa (/ə/).
The orthography encodes the *grammar*, not just the sound.

### 2.4 Consonant Lenition and Voicing Assimilation
Neapolitan speech features heavy phonetic alteration of consonants depending on their syntactic
environment.
To ensure machine readability and prevent lexical fragmentation (where a single word has multiple
spellings), MVO mandates the use of the **etymological "strong" consonant** as the orthographic
anchor.

**1. Initial Consonant Lenition (Dropping and Weakening)**
Certain initial consonants (`g`, `d`, `v`) weaken, rhotacize, or drop entirely in intervocalic/weak
positions, but return (often geminated) in strong positions.
MVO requires writing the underlying root consonant regardless of its phonetic realization in weak
positions.
* ✅ *guaglione* (Even when pronounced *uaglione* or *'uaglione*, g-drop)
* ✅ *doje* (Even when pronounced *roje*, d-rhotacism)
* ✅ *barca* (Even when pronounced *varca*, v-betacism)

The tokenizer will rely on this stable initial consonant.
Phonetic dropping is considered a surface-level grapheme-to-phoneme (G2P) rendering rather than an
orthographic change.

**2. Consonant Fortition (The Jod Strengthening)**
The palatal approximant `j` (*jod*) undergoes extreme strengthening (fortition) when subjected to
syntactic doubling, transforming into a geminated palatal sound written as `gghi-`.
Because MVO requires writing syntactic doubling for morphological disambiguation, this grapheme
shift is preserved in writing.
* *janco* (white) ➔ ✅ *è gghianco* / *'e gghianche*
* *jurnata* (day) ➔ ✅ *'e gghiurnate*
* *jettà* (to throw) ➔ ✅ *a gghiettà*

**NLP Resolution:** The lemmatizer must explicitly map word-initial `gghi-` back to the dictionary
lemma `j-` when encountered in a syntactically strong context.

**3. Voicing Assimilation (Post-Nasal Voicing)**
Spoken Neapolitan frequently blurs the distinction between voiceless (`p`, `t`, `c`) and voiced
(`b`, `d`, `g`) consonants, particularly after nasal sounds (`m`, `n`).
For example, *sempe* is often voiced as [ˈsɛmbə].
MVO strictly preserves the etymological voiceless consonant:
* ✅ *sempe* (❌ *sembe*)
* ✅ *manco* (❌ *mango*)

By anchoring the orthography to the etymological form, NLP systems avoid needing complex
cross-referencing for phonetic variations, and the standard remains accessible to readers across
different regional accents.

---

## 3. Apostrophes, Elision, and Apocope

The apostrophe (`'`) is one of the most overloaded characters in Neapolitan orthography.
MVO standardizes its usage into two distinct classes.

### 3.1 Initial Elision (Aphaeresis)
* Initial truncated consonants or vowels must retain an explicit leading apostrophe:
  * Definite articles: `'o` (*lo*), `'a` (*la*), `'e` (*li/le*).
  * Verbal/pronoun aphaeresis: `'ncoppa` (*in coppa*), `'nnammurato` (*innamorato*).

### 3.2 Apocope (Final Truncation)
* Infinitive verbs drop the final Latin `-re` and carry a **grave accent** on the stressed final
vowel, **not an apostrophe**:
  * ✅ *magnà* (from *magnare*) — **MVO Standard**
  * ❌ *magnar'* or *magna'* — **Deprecated**
* True apocope retains a trailing apostrophe only when no vocalic shift occurs (e.g., *po'* for
*poco*).

### 3.3 Crasis (Articulated Prepositions)
When the preposition *a* (to/at, in) fuses with the definite articles (*'o*, *'a*, *'e*), the
resulting crasis must be represented using a **circumflex accent** (`^`).
This standardizes the token and prevents ambiguous apostrophe clusters.
* *a* + *'o* ➔ **ô** (e.g., *Vaco ô mare* - I go to the sea)
* *a* + *'a* ➔ **â** (e.g., *Dallo â guagliona* - Give it to the girl)
* *a* + *'e* ➔ **ê** (e.g., *Parlo ê guagliuni* - I speak to the boys)

Other prepositions that elide without full crasis retain the apostrophe and a space (e.g., *d' 'o*,
*p' 'a*), which the tokenizer will handle as separate morphemes.

---

## 4. Syntactic Gemination (Raddoppiamento Fonosintattico)

Syntactic doubling (*raddoppiamento fonosintattico*) occurs naturally in spoken Neapolitan following
strong monosyllables or the neuter article.
MVO standardizes its written representation to maximize computational disambiguation.

### 4.1 General Rule: Canonical Base Forms
In general, words in text corpora MUST be written in their canonical un-doubled base form, even if
they are doubled in speech.
The NLP tokenizer should not have to strip doubled consonants for standard prepositions or
conjunctions.
* ✅ *a me* (Spoken: [a ˈmme]. Written as separate canonical tokens: `a` + `me`)
* ❌ *a mme*

### 4.2 Morphological Disambiguation (Neuter and Feminine Plural)
Neapolitan possesses two pairs of homophonous definite articles that are disambiguated in speech
exclusively via syntactic doubling.

To assist NLP part-of-speech (POS) tagging and dependency parsing, MVO **requires** explicitly
writing the geminated consonant when it serves as a morphological marker for gender or number.
The tokenizer will parse the leading double consonant to resolve the article's ambiguity:

**1. Disambiguating the Singular Articles (`'o` Masc. vs `'o` Neuter)**
The neuter article (mass/uncountable nouns) triggers gemination, distinguishing it from the
masculine article.
* **Masculine (Countable):** ✅ `'o fierro` ➔ The tool / the weapon.
* **Neuter (Mass):** ✅ `'o ffierro` ➔ The iron (material).
* **Masculine:** ✅ `'o pate` ➔ The father.
* **Neuter:** ✅ `'o ppane` ➔ Bread (substance).

**2. Disambiguating the Plural Articles (`'e` Masc. vs `'e` Fem.)**
The feminine plural article triggers gemination, distinguishing it from the masculine plural
article.
* **Masculine Plural:** ✅ `'e frati` ➔ The brothers.
* **Feminine Plural:** ✅ `'e ssore` ➔ The sisters.
* **Masculine Plural:** ✅ `'e russi` ➔ The red ones (masc).
* **Feminine Plural:** ✅ `'e rrosse` ➔ The red ones (fem).

*Note: For words starting with a vowel, where syntactic doubling cannot manifest as a geminated
consonant, the tokenizer will rely on metaphonic vowel changes (Section 5.3) or syntactical context.*

### 4.3 Lexicalized (Agglutinated) Compounds
Spoken double consonants are preserved in orthography **only** when they have been permanently fused
(agglutinated) into a single dictionary word over time.
These are treated as independent lemmas, not as live syntactic doubling.
* ✅ *cchiù* (from Latin *eccum plus*)
* ✅ *apposta* (from *a* + *posta*)
* ✅ *avveramente* (from *a* + *veramente*)
---

## 5. Enclitic Pronouns & Agglutination

Neapolitan frequently agglutinates pronominal enclitics onto imperative verbs and infinitive verb
stems.

### 5.1 Verb + Enclitic Rules
* Enclitics attach directly to the verbal stem without hyphens or apostrophes:
  * *dammélle* (*da' + a me + le*)
  * *dicitencello* (*dicite + a isso + 'o*)
* The tokenizer component of `napoli-nlp` will systematically split enclitic clusters into
constituent morphemes during preprocessing:
  * `dammélle` ➔ `da'` [VERB] + `me` [PRON] + `lle` [PRON]

### 5.2 Kinship Possessive Enclitics (Lexicalized)
Neapolitan features a traditional Southern Romance possessive enclisis exclusively for a closed set
of kinship terms in the **singular** (e.g., *patemo* "my father", *mammata* "your mother", *sorama*
"my sister", *fratemo* "my brother").

In the plural, Neapolitan discards the enclitic and reverts to an analytic construction (e.g. *'e
frati miei*).

**Orthography of the Medial Vowel:**
Consistent with the rule on etymological vowels (Section 2.2), the unstressed medial vowel must
retain the etymological vowel of the base noun, rather than being phonetically written as `e`.
* *mamma* + *ta* ➔ ✅ **mammata** (❌ *mammeta*)
* *frate* + *mo* ➔ ✅ **fratemo**

Because these enclitic forms are a finite, closed lexical class restricted to singular family
members, MVO treats them as **fixed, single dictionary lemmas**.
The tokenizer MUST NOT attempt to dynamically split them.
* ✅ *patemo* ➔ parsed as a single `[NOUN]` token meaning "my father".
* ✅ *fratemo* ➔ parsed as a single `[NOUN]` token meaning "my brother".
* ✅ *'e frati mieji* ➔ parsed as separate tokens `[DET]` + `[NOUN]` + `[ADJ]`.

---

## 6. Metaphony (Vowel Mutation) and NLP Stemming

Metaphony is a defining feature of Neapolitan morphology.
It is a predictable vowel mutation where the stressed root vowel of a word changes in response to
its final unstressed vowel.
Specifically, historical final **-i** (typically plural) and **-o/-u** (typically masculine
singular) trigger this mutation, while final **-a** and **-e** do not.

**The Four Metaphonic Paths:**
When triggered by a final `-i` or `-o`, the stressed root vowels mutate as follows:
1. **Open 'E' splits to 'IE':** *'o pede* ➔ *'e piedi* (not *'e piede*)
2. **Open 'O' splits to 'UO':** *grossa* (fem) ➔ *gruosso* (masc)
3. **Closed 'E' raises to 'I':** *nera* (fem) ➔ *niro* (masc)
4. **Closed 'O' raises to 'U':** *rossa* (fem) ➔ *russo* (masc)

**The Computational Problem with Phonetic Spelling:**
In many modern spoken varieties, the final vowels `-o`, `-e`, and `-i` have all phonetically
collapsed into a schwa (traditionally written as `-e`).
If written phonetically (e.g., *russe*, *rosse*, *gruosse*, *grosse*), the trigger suffix is
obscured.
To an NLP tokenizer or stemmer, these words appear to share the exact same suffix (`-e`), making
rule-based lemmatization impossible without exhaustive, hardcoded dictionary lookups.

**The MVO Solution (Etymological Spelling):**
By strictly enforcing the etymological final vowels (Section 2.3), the orthography exposes the
metaphonic trigger directly to the machine.

Standardizing on *russo / rossa / russi / rosse* allows natural language processing models to use
simple, deterministic regex or stemming algorithms.
A lemmatizer can algorithmically deduce that if a word ends in `-i` or `-o` and contains a mutated
root vowel (`ie`, `uo`, `i`, `u`), it can mathematically reverse the metaphony to find the base
dictionary lemma (e.g., stripping `-o` and reverting `u` ➔ `o` to link *russo* to *ross-*).

---

## 7. Alphabet & Digraph Summary

MVO utilizes the standard Latin alphabet, incorporating specific graphemes and digraphs to represent
Neapolitan phonology.
To ensure text normalization, these must be used consistently across the lexicon.

### 7.1 Latin Consonant Clusters
Historically, Neapolitan palatalized several Latin consonant + `l` clusters.
MVO relies on established, traditional digraphs to represent these shifts rather than reverting to
unreadable Latin etymology:

| Latin Cluster | Latin Root | Neapolitan Shift | MVO Spelling | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **fl-** | *florem* | `[ʃ]` | **sciore** | Spelled with `sci-` / `sce-` |
| **pl-** | *plorare* | `[kj]` | **chiagnere** | Spelled with `chi-` |
| **cl-** | *clamare* | `[kj]` | **chiammà** | Spelled with `chi-` |
| **bl-** | *blank* (Germ.) | `[j]` | **janco** | Spelled with `j-` |

### 7.2 The Neapolitan *Jod* (`j`)
The letter **j** (i-lunga) is explicitly retained in the MVO alphabet as a distinct grapheme.
It represents the palatal approximant phoneme `/j/` (similar to the English 'y').
It is typically found at the beginning of words derived from Latin *di-*, *i-*, or *bl-*, and
between vowels.
* ✅ *jurnata* (from *diurnum*)
* ✅ *janco* (from Germanic *blank*)
* ✅ *jammo* (from *eamus*)
* ❌ *iurnata*, ❌ *ianco*, ❌ *giammo* (These phonetic or Italianized spellings are deprecated).

### 7.3 Digraph Summary

For Natural Language Processing (specifically Grapheme-to-Phoneme pipelines), the tokenizer relies
on the following standard digraph mappings:

| MVO Digraph | Context | Phoneme | Example | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **sc** | Before **e, i** | `[ʃ]` | *sciore* | Voiceless postalveolar fricative. |
| **sc** | Before **a, o, u** | `[ʃk]` | *scarpa* | Palatalized *s-impura* + velar plosive. |
| **gn** | Anywhere | `[ɲ]` | *muntagna* | Palatal nasal. Retained etymologically. |
| **gli** | Anywhere | `[ʎ]` | *figlio* | Palatal lateral. Retained etymologically for lexical compatibility, despite often shifting to `[j]` in modern speech. |

---

## 8. Versioning & Compliance

All JSON schemas within `data/schemas/` validate lemmas against MVO standards.
Deviations or regional spelling variants must be designated under the `variants` metadata key within
dictionary entries rather than altering canonical lemmas.
