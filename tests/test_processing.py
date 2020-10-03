import pytest

from data_processing import validate_stats, apply_stats_to_craft_skill


def test_validate_stats():
    with pytest.raises(Exception):
        validate_stats(6, 1, 0)

    with pytest.raises(Exception):
        validate_stats(0, -1, 0)

    validate_stats(0, 0, 0)
    validate_stats(1, 0, 0)

    with pytest.raises(Exception):
        validate_stats(1, 1, 0)

    validate_stats(2, 0, 0)
    validate_stats(3, 0, 0)
    validate_stats(4, 0, 0)
    validate_stats(4, 1, 0)

    with pytest.raises(Exception):
        validate_stats(4, 1, 1)

    validate_stats(4, 5, 0)
    validate_stats(4, 5, 1)

    with pytest.raises(Exception):
        validate_stats(4, 4, 1)

    with pytest.raises(Exception):
        validate_stats(4, 4, 5)

    with pytest.raises(Exception):
        validate_stats(5, 4, 1)


def test_apply_stats_to_craft_skill():
    assert apply_stats_to_craft_skill(4, 0, 0) == 126
    assert apply_stats_to_craft_skill(4, 5, 0) == 106
    assert apply_stats_to_craft_skill(5, 5, 5) == 95
