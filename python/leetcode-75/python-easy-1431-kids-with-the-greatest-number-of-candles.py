"""
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

kidsWithCandies:
- get number of max candies out of all kids
- list comprehension to make a new list
    - if kid candies + your candies >= max candies, then True, else False
"""

from typing import List

candies, extraCandies = [2, 3, 5, 1, 3], 3
# candies, extraCandies = [4, 2, 1, 1, 2], 1
# candies, extraCandies = [12, 1, 12], 10


def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    max_candies = max(candies)
    result = [True if x + extraCandies >= max_candies else False for x in candies]
    return result


print(kidsWithCandies(candies, extraCandies))
