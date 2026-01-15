from app.main import get_human_age


def test_should_return_zeros_for_zero_age() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zeros_when_age_less_than_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_when_age_between_15_and_24() -> None:
    assert get_human_age(15, 15) == [1, 1]
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_two_when_age_is_24() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_calculate_correctly_after_second_year() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_work_with_large_numbers() -> None:
    assert get_human_age(100, 100) == [21, 17]
