from app.services.quality_service import calculate_quality


def test_quality_match():
    result = calculate_quality(
        "positive",
        "positive",
    )

    assert result == 100.0


def test_quality_mismatch():
    result = calculate_quality(
        "positive",
        "negative",
    )

    assert result == 0.0