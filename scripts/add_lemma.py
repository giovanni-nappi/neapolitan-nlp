#!/usr/bin/env python3
import difflib
import json
from pathlib import Path
from typing import Dict

# Configuration
LEXICON_DIR = Path("data/lexicon")
VALID_POS = ["noun", "verb", "adj", "adv", "func"]


def setup_directories():
    """Ensure the sharded data directories exist."""
    LEXICON_DIR.mkdir(parents=True, exist_ok=True)
    for pos in VALID_POS:
        file_path = LEXICON_DIR / f"{pos}s.json"
        if not file_path.exists():
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump([], f)


def predict_metaphonic_forms(lemma: str) -> Dict[str, str]:
    """
    Automates MVO metaphony generation by reversing the metaphonic root shift
    for feminine forms and applying standard MVO endings (-a, -i, -e).

    Natural MVO Metaphonic Shifts (Masculine -> Feminine stem):
      - 'uo' -> 'o' (e.g., gruosso  -> grossa,   stem: gruoss- -> gross-)
      - 'ie' -> 'e' (e.g., viecchio -> vecchia,  stem: viecch- -> vecch-)
      - 'u'  -> 'o' (e.g., russo    -> rossa,    stem: russ-   -> ross-)
      - 'i'  -> 'e' (e.g., niro     -> nera,     stem: nir-    -> ner-)
    """
    if lemma.endswith(("o", "a", "e", "i")):
        stem = lemma[:-1]
    else:
        stem = lemma

    unmetaphorized_stem = stem
    if "uo" in stem:
        idx = stem.rfind("uo")
        unmetaphorized_stem = stem[:idx] + "o" + stem[idx + 2 :]
    elif "ie" in stem:
        idx = stem.rfind("ie")
        unmetaphorized_stem = stem[:idx] + "e" + stem[idx + 2 :]
    elif "u" in stem:
        idx = stem.rfind("u")
        unmetaphorized_stem = stem[:idx] + "o" + stem[idx + 1 :]
    elif "i" in stem:
        idx = stem.rfind("i")
        unmetaphorized_stem = stem[:idx] + "e" + stem[idx + 1 :]

    # Deduplicate trailing 'i' for masculine plural (e.g. viecchi -> viecchi, not viecchii)
    m_pl = stem if stem.endswith("i") else f"{stem}i"

    return {
        "base": lemma,
        "m_sg": lemma,
        "f_sg": f"{unmetaphorized_stem}a",
        "m_pl": m_pl,
        "f_pl": f"{unmetaphorized_stem}e",
    }


def generate_forms(lemma: str, pos: str, has_metaphony: bool) -> Dict[str, str]:
    """Handles morphological form generation with auto-prediction and user review."""
    forms = {"base": lemma}

    if pos in ["adj", "noun"] and has_metaphony:
        predicted = predict_metaphonic_forms(lemma)

        print("\n[★] Auto-generated Metaphonic Forms (MVO Rules):")
        print(f"  • Masculine Singular : {predicted['m_sg']}")
        print(f"  • Feminine Singular  : {predicted['f_sg']}")
        print(f"  • Masculine Plural   : {predicted['m_pl']}")
        print(f"  • Feminine Plural    : {predicted['f_pl']}")

        confirm = input("\nAccept these predicted forms? (Y/n): ").strip().lower()

        if confirm in ["", "y", "yes"]:
            return predicted
        else:
            print("\nPlease enter custom inflected forms:")
            forms["m_sg"] = lemma
            forms["f_sg"] = input("  Feminine Singular : ").strip()
            forms["m_pl"] = input("  Masculine Plural  : ").strip()
            forms["f_pl"] = input("  Feminine Plural   : ").strip()

    return forms


def show_diff(existing_entry: dict, new_entry: dict):
    """Prints a clean unified diff between existing and new JSON records."""
    existing_str = json.dumps(existing_entry, indent=2, ensure_ascii=False)
    new_str = json.dumps(new_entry, indent=2, ensure_ascii=False)

    diff = difflib.unified_diff(
        existing_str.splitlines(),
        new_str.splitlines(),
        fromfile="Existing Entry",
        tofile="New Entry",
        lineterm="",
    )

    print("\n" + "=" * 50)
    print("      DUPLICATE DETECTED - PROPOSED DIFF")
    print("=" * 50)
    diff_lines = list(diff)
    if not diff_lines:
        print("(No changes detected; entries are identical)")
    else:
        for line in diff_lines:
            if line.startswith("+") and not line.startswith("+++"):
                print(f"\033[92m{line}\033[0m")  # Green for addition
            elif line.startswith("-") and not line.startswith("---"):
                print(f"\033[91m{line}\033[0m")  # Red for deletion
            else:
                print(line)
    print("=" * 50)


def main():
    setup_directories()
    print("=== Neapolitan NLP: Lemma Ingestion Tool ===")

    while True:
        print("\n" + "-" * 50)
        lemma = (
            input(
                "Enter Neapolitan lemma (e.g., 'gruosso', 'chiagnere', 'q' to quit): "
            )
            .strip()
            .lower()
        )
        if lemma == "q":
            break
        if not lemma:
            continue

        pos = input(f"Enter POS {VALID_POS}: ").strip().lower()
        if pos not in VALID_POS:
            print(f"Error: POS must be one of {VALID_POS}")
            continue

        phonetic_prompt = (
            f"Phonetic/Stress display (press Enter to default to '{lemma}'): "
        )
        phonetic_input = input(phonetic_prompt).strip()
        phonetic_display = phonetic_input if phonetic_input else lemma

        translation_input = input(
            "Enter Italian translations (comma-separated): "
        ).strip()
        translations = [t.strip() for t in translation_input.split(",") if t.strip()]

        has_metaphony = False
        if pos in ["adj", "noun"]:
            meta_input = input("Does this trigger metaphony? (y/n): ").strip().lower()
            has_metaphony = meta_input == "y"

        forms = generate_forms(lemma, pos, has_metaphony)

        entry = {
            "lemma": lemma,
            "phonetic_display": phonetic_display,
            "pos": pos,
            "it_translations": translations,
            "metaphony": has_metaphony,
            "forms": forms,
        }

        target_file = LEXICON_DIR / f"{pos}s.json"

        with open(target_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Check for duplicate lemma
        existing_idx = next(
            (i for i, item in enumerate(data) if item.get("lemma") == lemma),
            None,
        )

        if existing_idx is not None:
            existing_entry = data[existing_idx]
            show_diff(existing_entry, entry)

            overwrite = (
                input(
                    f"Lemma '{lemma}' already exists in {target_file.name}. Overwrite? (y/N): "
                )
                .strip()
                .lower()
            )

            if overwrite in ["y", "yes"]:
                data[existing_idx] = entry
                print(f"\n[✓] Updated existing record for '{lemma}'.")
            else:
                print(f"\n[!] Skipped updating '{lemma}'.")
                continue
        else:
            data.append(entry)
            print(f"\n[✓] Added new record for '{lemma}'.")

        # Keep JSON shards sorted alphabetically
        data = sorted(data, key=lambda x: x["lemma"])

        with open(target_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"[✓] Saved {target_file.name} successfully!")


if __name__ == "__main__":
    main()
