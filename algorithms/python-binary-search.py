"""
binary search:
- works for SMALL and ORDERED collections
- generate new range based on midpoints
- faster than sequential search

0(logN)
"""

from typing import List

collection, target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11  # false
collection, target = [1, 2, 3, 4, 6, 7, 8, 9, 10], 5  # false


def binary_search(collection: List[int], target: int) -> bool:
    low = 0
    high = len(collection) - 1
    # repeat while range exists
    while low <= high:
        mid = (high + low) // 2
        if target < collection[mid]:  # target is less than midpoint of collection
            high = mid - 1
        elif target > collection[mid]:  # target is greater than midpoint of collection
            low = mid + 1
        else:
            return True  # target is midpoint of collection
    return -(low + 1)  # returns -index of where element should be


print(binary_search(collection, target))
