import pytest

import maximum_differnece.max_diff_between_increasing_elements as md

test_data = [([7, 1, 5, 4], 4), ([9, 4, 3, 2], -1), ([1, 5, 2, 10], 9)]


@pytest.mark.parametrize("input, output", test_data)
def test_maximum_difference_mine(input, output):
    assert md.maximum_difference_mine(input) == output


@pytest.mark.parametrize("input, output", test_data)
def test_maximum_difference_imperative(input, output):
    assert md.maximum_difference_imperative(input) == output
