"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock

maxProfit:
- set min and max as first price
- iterate through list
- everytime a new minimum is found, reset min and max so that profits will be from new min, continue loop and don't recalculate profit yet
- everytime a new max is found, reset max
- change profit only if new profit is bigger than the last
"""

from typing import List

# prices = [7, 1, 5, 3, 6, 4]  # 5
# prices = [7, 6, 4, 3, 1]  # 0
# prices = [1, 2]  # 1
prices = [2, 1, 2, 1, 0, 1, 2]  # 2


def maxProfit(prices: List[int]) -> int:
    min_price = max_price = prices[0]
    profit = 0
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = max_price = prices[i]
            continue
        if prices[i] > max_price:
            max_price = prices[i]
        profit = max_price - min_price if max_price - min_price > profit else profit
    return profit


print(maxProfit(prices))
