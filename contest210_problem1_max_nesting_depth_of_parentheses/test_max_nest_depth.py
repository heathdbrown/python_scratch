import pytest
import max_nest_depth as mnd

# test_vps = [
#     ("", True),
#     ("()()", True),
#     ("()(()())", True),
#     (")(", False),
#     ("(()", False),
# ]
# test_depths = [("", 0), ("()()", 1), ("()(()())", 2)]

test_data = [("(1+(2*3)+((8)/4))+1", 3), ("(1)+((2))+(((3)))", 3), ("1", 0)]


# @pytest.mark.parametrize("string, expected", test_vps)
# def test_is_vps(string, expected):
#     assert mnd.is_vps(string) == expected


# @pytest.mark.parametrize("string, expected", test_depths)
# def test_depth(string, expected):
#     assert mnd.depth(string) == expected


@pytest.mark.parametrize("string, expected", test_data)
def test_max_depth(string, expected):
    assert mnd.max_depth(string) == expected
