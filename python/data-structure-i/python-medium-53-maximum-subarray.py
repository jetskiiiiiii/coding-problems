"""
https://leetcode.com/problems/maximum-subarray/?envType=study-plan&id=data-structure-i

maxSubArray:
- basic premise: elements are compared to the sum of the subarray up to (including) that element
1. check if subarray is length 1 or 0, in which case return values are itself or 0, respectively
2. create variables
    - store current sum (sum of the current subarray up to the element being iterated)
    - store maximum sum found from all subarrays program has looked at
    - keep track of sums 
"""

from typing import List

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  # 6
# nums = [1]  # 1
# nums = [5, 4, -1, 7, 8]  # 23
# nums = [1, 2]  # 3
# nums = [1, 2, -1, -2, 2, 1, -2, 1, 4, -5, 4]  # 6
# nums = []  # 0
# nums = [-1]
# nums = [-1, -2]
nums = [-2, -1]


def maxSubArray(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    elif len(nums) == 0:
        return 0

    max_subarray_sum[-1] = max_sum = nums[0]
    max_subarray_sum = [nums[0]]
    for i in range(1, len(nums)):
        max_subarray_sum[-1] += nums[i]
        if nums[i] >= max_subarray_sum[-1]:
            max_sum = (
                max_sum
                if max_subarray_sum == []
                else max_sum
                if max(max_subarray_sum) <= max_sum
                else max(max_subarray_sum)
            )
            max_subarray_element = max_subarray_sum = []
            max_subarray_sum[-1] = nums[i]
            max_subarray_sum.append(max_subarray_sum[-1])
        else:
            max_subarray_sum.append(max_subarray_sum[-1])

    return max(max_subarray_sum) if max(max_subarray_sum) > max_sum else max_sum


def maxSubArray(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    elif len(nums) == 0:
        return 0

    max_sum = nums[0]
    max_subarray_sum = [nums[0]]
    for i in range(1, len(nums)):
        max_subarray_sum[-1] += nums[i]
        if nums[i] >= max_subarray_sum[-1]:
            max_sum = (
                max_sum
                if max_subarray_sum == []
                else max_sum
                if max(max_subarray_sum) <= max_sum
                else max(max_subarray_sum)
            )
            max_subarray_sum[-1] = nums[i]
            max_subarray_sum.append(max_subarray_sum[-1])
            del max_subarray_sum[0:-1]
        else:
            max_subarray_sum.append(max_subarray_sum[-1])

    return max(max_subarray_sum) if max(max_subarray_sum) > max_sum else max_sum


def maxSubArray(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    elif len(nums) == 0:
        return 0

    max_subarray_sum = [nums[0]]
    for i in range(1, len(nums)):
        max_subarray_sum.append(max_subarray_sum[-1] + nums[i])
        if nums[i] >= max_subarray_sum[-1]:
            max_subarray_sum.append(nums[i])
        else:
            max_subarray_sum.append(max_subarray_sum[-1])

    return max(max_subarray_sum)


def fastmaxSubArray(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    elif len(nums) == 0:
        return 0

    curr_sum = max_sum = nums[0]
    for i in range(1, len(nums)):
        curr_sum += nums[i]
        if curr_sum > curr_sum - nums[i]:
            
        if nums[i] >= curr_sum:
            max_sum = curr_sum = nums[i]
        elif curr_sum > max_sum:
            max_sum = curr_sum

    return max_sum


# def maxSubArray(nums: List[int]) -> int:
#     max_sum = 0
#     for i in range(0, len(nums)):
#         if nums[i] >= max_sum + nums[i]:
#             max_sum = nums[i]
#         elif max_sum + nums[i] > max_sum:
#             max_sum += nums[i]

#     return max_sum


print(fastmaxSubArray(nums))
