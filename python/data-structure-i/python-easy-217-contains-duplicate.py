"""
https://leetcode.com/problems/contains-duplicate/?envType=study-plan&id=data-structure-i

containsDuplicates:
- turn array into a set (removes duplicates)
- format original and set into same type (sorted list) to see if any duplicates were removed
"""

from typing import List

# nums = [1, 2, 3, 1]
nums = [1, 5, -2, -4, 0]


def containsDuplicate(nums: List[int]) -> bool:
    return sorted(nums) != sorted(list(set(nums)))


print(containsDuplicate(nums))
