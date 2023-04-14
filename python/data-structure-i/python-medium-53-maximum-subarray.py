"""
https://leetcode.com/problems/maximum-subarray/?envType=study-plan&id=data-structure-i

maxSubArray:
- basic premise: elements are compared to the sum of the subarray up to (including) that element
1. check if subarray is length 0, in which case return 0
2. create variables
    - one to track maximum sum found so far
    - one to track sum of current subarray up to the element being indexed
3. iterate through the list
4. if element is bigger than the current sum (including the element), restart the count (create a new subarray)
5. else, just update current sum to include current element
6. check if the current sum is bigger than the current sum
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
# nums = [-2, -1]


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


def maxSubArray(nums: List[int]) -> int:
    # check if list is empty
    if nums == []:
        return 0

    # if list not empty, set maximum sum and sum of current subarray as first element
    else:
        max_sum = curr_sum = nums[0]

    # iterate through list (exclude first element)
    for i in range(1, len(nums)):
        """if current element is bigger than current sum,
        then the current element by itself is more valuable
        (e.g. [1, 0, -2, 5]; in this list, when index is at 5, current sum is 4 (1 + 0 + -2 + 5 = 4)
        so, 5 by itself is bigger than 4; the max sum is then 5 by itself)
        if this condition is met, a "new" subarray is made (meaning restart the sum count)
        """
        if nums[i] >= curr_sum + nums[i]:
            curr_sum = nums[i]
        else:
            curr_sum + +nums[i]
        # always check if current sum is bigger than any previous max sums
        max_sum = max(max_sum, curr_sum)

    return max_sum


print(maxSubArray(nums))
