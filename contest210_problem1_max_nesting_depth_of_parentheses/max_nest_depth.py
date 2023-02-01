def is_vps(s: str) -> bool:
    if s in ["(", ")", ""]:
        return True
    return False


def char_map(s: str) -> int:
    value_map = {"(": 1, ")": -1}
    return value_map[s]


def depth(vps_value_list: list[int]) -> int:
    import itertools

    return max(list(itertools.accumulate(vps_value_list)))


def maxDepth(s: str) -> int:
    # remove everything but parenthesis?
    vps = [char_map(char) for char in s if is_vps(char)]
    return depth(vps)


###
class Solution:
    def maxDepth(self, s: str) -> int:
        import itertools

        value_map = {"(": 1, ")": -1}

        vps = [value_map[char] for char in s if char in ["(", ")", ""]]

        positive_sum_scan = max(list(itertools.accumulate(vps)))

        if not positive_sum_scan:
            return 0
        return positive_sum_scan
