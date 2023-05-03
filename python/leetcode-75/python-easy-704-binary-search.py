"""
https://leetcode.com/problems/binary-search

search:
- determine position of target within a dynamic range
- because the collection is ordered, if target is less than midpoint, we can shrink the range down to [low, mid)
- if target is greater than midpoint, we can also shrink the range down to (midpoint, high]
- if target is midpoint, we've found the target
- if low ever becomes greater than high, then whole list has been looked through (return -1, no solution exists)
"""

from typing import List

nums, target = [-1, 0, 3, 5, 9, 12], 9
# nums, target = [-1, 0, 3, 5, 9, 12], 2
# nums, target = [-1, 0, 3, 5, 9, 12], 13


def binarySearch(nums: List[int], target: int) -> int:
    if not nums:
        return 0

    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (high + low) >> 1
        if target == nums[mid]:
            return mid
        if target < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


print(binarySearch(nums, target))
