"""Given a 0-indexed integer array `nums` of size `n`, find the
maximum difference between `nums[i]` and nums[j]
(i.e., nums[j] - nums[i]), such that 0 <= i <j < n
and nums[i] < nums[j].

Return the maximum difference. if no such i and j exists, return -1.
"""

# my shot at the problem
import itertools


def maximum_difference_mine(nums: list[int]) -> int:
    qualified = [j - i for i, j in itertools.combinations(nums, 2) if i < j]

    if not qualified:
        return -1
    return max(qualified)
    # return max(j - i for i, j in itertools.combinations(nums, 2) if i < j)


# from https://youtu.be/UogkQ67d0nY?t=438
# imperative 'style'
import sys


def maximum_difference_imperative(nums: list[int]) -> int:
    result, min_so_far = -1, sys.maxsize
    for elem in nums:
        min_so_far = min(min_so_far, elem)
        if elem > min_so_far:
            result = max(result, elem - min_so_far)
    return result


# Combinators?
# https://joshbohde.com/blog/combinators-in-python/
# https://youtu.be/UogkQ67d0nY?t=1133

if __name__ == "__main__":
    nums = [7, 1, 5, 4]
    print(max_diff(nums))
