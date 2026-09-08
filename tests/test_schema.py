import json
from pathlib import Path
import pytest

PROJECT_ROOT = Path(__file__).parent.parent
LEXICON_DIR = PROJECT_ROOT / "data" / "lexicon"

ALLOWED_POS = {
    "adj", "adv", "conj", "det", "interj",
    "noun", "num", "prep", "pron", "verb"
}

ALLOWED_GENDER = {
    "masculine", "feminine", "neuter", "common"
}


def get_lexicon_shards():
    """Returns all JSON shard files inside data/lexicon/."""
    if not LEXICON_DIR.exists():
        return []
    return list(LEXICON_DIR.glob("*.json"))


@pytest.mark.parametrize(
    "shard_path",
    get_lexicon_shards(),
    ids=lambda p: p.name,
)
def test_lexicon_pos_and_gender_values(shard_path: Path):
    """Asserts that all pos and gender fields use valid enum values across lemmas and forms."""
    with open(shard_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    for idx, entry in enumerate(data):
        lemma = entry.get("lemma", f"index_{idx}")

        # Validate headword POS
        if "pos" in entry:
            assert entry["pos"] in ALLOWED_POS, (
                f"Invalid pos '{entry['pos']}' in {shard_path.name} "
                f"for lemma '{lemma}'. Allowed: {ALLOWED_POS}"
            )

        # Validate headword gender
        if "gender" in entry:
            assert entry["gender"] in ALLOWED_GENDER, (
                f"Invalid gender '{entry['gender']}' in {shard_path.name} "
                f"for lemma '{lemma}'. Allowed: {ALLOWED_GENDER}"
            )

        # Validate gender overrides inside inflected forms
        forms = entry.get("forms", {})
        if isinstance(forms, dict):
            for form_key, form_value in forms.items():
                _check_form_gender(form_value, shard_path.name, lemma, form_key)


def _check_form_gender(form_value, shard_name: str, lemma: str, form_key: str):
    """Helper to check gender in nested form objects or lists of form objects."""
    if isinstance(form_value, dict):
        if "gender" in form_value:
            assert form_value["gender"] in ALLOWED_GENDER, (
                f"Invalid gender '{form_value['gender']}' in form '{form_key}' "
                f"in {shard_name} for lemma '{lemma}'. Allowed: {ALLOWED_GENDER}"
            )
    elif isinstance(form_value, list):
        for sub_item in form_value:
            _check_form_gender(sub_item, shard_name, lemma, form_key)
