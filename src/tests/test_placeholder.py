"""Basic smoke test for napoli_nlp package initialization."""

import napoli_nlp


def test_package_metadata():
    """Verify package version is accessible."""
    assert hasattr(napoli_nlp, "__version__")
    assert napoli_nlp.__version__ == "0.1.0"
