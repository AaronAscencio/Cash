from main import minimum_number_of_coins
import pytest


@pytest.mark.parametrize(
    "input,exp",
    [
        (0.99,9),
        (0,0),
        (4,16),
        (0.05,1),
        (0.1,1),
        (0.08,4)
    ]
)
def test_minimum_number_of_coins_multi(input,exp):
    assert minimum_number_of_coins(input) == exp
