import json
from pathlib import Path
import jsonschema
import pytest

PROJECT_ROOT = Path(__file__).parent.parent
SCHEMA_FILE = PROJECT_ROOT / "schemas" / "lemma.schema.json"
LEXICON_DIR = PROJECT_ROOT / "data" / "lexicon"


@pytest.fixture(scope="module")
def lemma_schema() -> dict:
    """Loads the JSON schema for lemma validation from file."""
    with open(SCHEMA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


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
def test_validate_lexicon_shard_schema(shard_path: Path, lemma_schema: dict):
    """Validates each entry in each lexicon JSON file against the JSON schema."""
    with open(shard_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, list):
        for entry in data:
            jsonschema.validate(instance=entry, schema=lemma_schema)
    else:
        jsonschema.validate(instance=data, schema=lemma_schema)


@pytest.mark.parametrize(
    "shard_path",
    get_lexicon_shards(),
    ids=lambda p: p.name,
)
def test_lexicon_shard_ordering_and_uniqueness(shard_path: Path):
    """Verifies that entries in each shard are sorted alphabetically and unique."""
    with open(shard_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    lemmas = [entry["lemma"] for entry in data]

    # Check for duplicates
    duplicates = {l for l in lemmas if lemmas.count(l) > 1}
    assert not duplicates, f"Duplicate lemmas found in {shard_path.name}: {duplicates}"

    # Check alphabetical sorting
    assert lemmas == sorted(
        lemmas
    ), f"Entries in {shard_path.name} are not sorted alphabetically."
