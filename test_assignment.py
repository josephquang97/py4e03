import pytest
from main import calculate_price


@pytest.mark.parametrize(
    "hours, rate, expected",
    [
        (39, 3, 117.0),
        (40, 3, 120.0),
        (41, 3, 124.5),
        (45, 3, 142.5),
        (45, 2.75, 130.625),
    ],
)
def test_price(hours, rate, expected):
    result = calculate_price(hours, rate)
    assert result == expected
