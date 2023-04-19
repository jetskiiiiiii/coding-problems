"""
https://leetcode.com/problems/two-sum/?envType=study-plan&id=data-structure-i


twoSum:
- iterate through each index
- for each iteration, iterate through list to find any pairs whose sum == target

fastTwoSum:
- sort elements and iterate
- for each element, find the other addend (numbers that make up a sum are called addends), if it exists
- return indices if matches are found
- don't look in previously indexed elements, but make sure to properly account for those positions when matches are found
"""

# nums, target = [2, 7, 11, 15], 9  # [0, 1]
# nums, target = [3, 2, 4], 6  # [1, 2]
# nums, target = [3, 3], 6  # [0, 1]
# nums, target = [0, 4, 3, 0], 0  # [0, 3]
nums, target = [1, 6142, 8192, 10239], 18431  # [2, 3]


def twoSum(nums, target):
    # iterate through list
    for i in range(len(nums)):
        # for each index, iterate through list again to find any matches
        for j in range(len(nums)):
            # skip if i and j are referencing the same index
            if i == j:
                continue
            if nums[i] + nums[j] == target:
                return i, j


def fastTwoSum(nums, target):
    # since an answer always exists, values of lists of length 2 are answers
    if len(nums) == 2:
        return 0, 1

    for i in range(len(nums)):
        # check if addends exist
        # nums[i + 1 :] ensures previous elements (including current index) are not searched
        if target - nums[i] in nums[i + 1 :]:
            # return the indices if addends are found
            # i + 1 at the end of the second return value ensures that previous indices are accounted for
            return i, nums[i + 1 :].index(target - nums[i]) + i + 1


# def fasterTwoSum(nums, target):

print(fastTwoSum(nums, target))
