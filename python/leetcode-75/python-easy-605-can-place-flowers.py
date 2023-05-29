"""
https://leetcode.com/problems/can-place-flowers/


Description:
You have a long flowerbed in which some of the plots are planted, and some are not. 
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, 
where 0 means empty and 1 means not empty, and an integer n, 
return true if n new flowers can be planted in the flowerbed 
without violating the no-adjacent-flowers rule and false otherwise.


canPlaceFlowers:
- keep track of empty spaces (0s)
- empty space counter starts at 0, and 0 gets added at the end (as [1, 0, 0] or [0, 0, 1] show that ends are empty spaces)
- if there are ever 3 or 4 empty spaces, a flower can be plotted
    - when end is reached, two empty spaces might be added, which can skip 3 and go to 4 (e.g. [1, 0, 0, 0])
"""

from typing import List

# examples
flowerbed, n = [1, 0, 0, 0, 1], 1  # true
# flowerbed, n = [1, 0, 0, 0, 1], 2 # false
# flowerbed, n = [1, 0, 0, 0, 0, 1], 2 # false
# flowerbed, n = [1, 0, 0, 0, 1, 0, 0], 2 # true
# flowerbed, n = [1, 0, 0, 0], 1 # true


def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    empty_space_counter = 1  # start of flowerbed is an empty space
    flower_counter = 0
    for flower in range(len(flowerbed)):
        if flowerbed[flower] == 0:
            empty_space_counter += 1
        else:
            empty_space_counter = 0

        # if end is reached, add an empty space
        if flower == len(flowerbed) - 1:
            empty_space_counter += 1

        if empty_space_counter >= 3:
            flower_counter += 1
            empty_space_counter = 1

    return flower_counter >= n


print(canPlaceFlowers(flowerbed, n))
