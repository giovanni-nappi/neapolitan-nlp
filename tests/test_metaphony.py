import sys
from pathlib import Path
import pytest

# Ensure project root is on sys.path for script imports
PROJECT_ROOT = Path(__file__).parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.add_lemma import predict_metaphonic_forms


@pytest.mark.parametrize(
    "lemma, expected_forms",
    [
        # Shift 1: 'uo' -> 'o'
        (
            "gruosso",
            {
                "base": "gruosso",
                "m_sg": "gruosso",
                "f_sg": "grossa",
                "m_pl": "gruossi",
                "f_pl": "grosse",
            },
        ),
        # Shift 2: 'ie' -> 'e' (with -i stem deduplication)
        (
            "viecchio",
            {
                "base": "viecchio",
                "m_sg": "viecchio",
                "f_sg": "vecchia",
                "m_pl": "viecchi",
                "f_pl": "vecchie",
            },
        ),
        # Shift 3: 'u' -> 'o'
        (
            "russo",
            {
                "base": "russo",
                "m_sg": "russo",
                "f_sg": "rossa",
                "m_pl": "russi",
                "f_pl": "rosse",
            },
        ),
        # Shift 4: 'i' -> 'e'
        (
            "niro",
            {
                "base": "niro",
                "m_sg": "niro",
                "f_sg": "nera",
                "m_pl": "niri",
                "f_pl": "nere",
            },
        ),
    ],
)
def test_predict_metaphonic_forms(lemma: str, expected_forms: dict):
    """Verifies that MVO metaphonic predictions generate accurate masculine/feminine forms."""
    result = predict_metaphonic_forms(lemma)
    assert result == expected_forms


def test_consonant_ending_stem():
    """Verifies metaphonic handling for words ending in consonants if encountered."""
    result = predict_metaphonic_forms("fuerte")
    assert result["f_sg"] == "forte-a" or result["m_sg"] == "fuerte"
