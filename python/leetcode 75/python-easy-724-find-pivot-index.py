"""
https://leetcode.com/problems/find-pivot-index
pseudocode: 

pivotIndex:
1. check left/right edge cases separately (check right edge case at the end, as it is the least possible)
2. iterate through each element
3. calculate left and right sums
4. at every iteration, compare the sums
5. if sums never equal, return -1

shortPivotIndex:
1. create new array with 0 at beginning and end to cover special case where left/right edge is pivot
2. iterate through each element
3. calculate strict left and right sums
4, at every iteration, compare the sums to see if they equal
5. if no equality, return -1

short2PivotIndex:
1. iterate through every element
2. for every element, compare sums of 0-ith and ith-end
3. if no equality, return -1
"""

# nums = [1,7,3,6,5,6]
# nums = [1,2,3]
# nums = [2,1,-1]
# nums = [-1,-1,0,1,1,0]

def pivotIndex(nums):
    if sum(nums[1:len(nums)]) == 0: return 0 # count right sum first, since first index has no values to its left
    for i in range(1, len(nums)):
        if sum(nums[i+1:len(nums)]) == sum(nums[0:i]): return i
    if sum(nums[0:len(nums)-1]) == 0: return 0
    return -1

def shortPivotIndex(nums):
    nums.insert(0, 0)
    nums.insert(len(nums), 0)

    for i in range(1, len(nums)-1):
        if sum(nums[0:i]) == sum(nums[i+1:len(nums)]): return i-1
    return -1
        
def short2PivotIndex(nums):
    for i in range(len(nums)):
        if sum(nums[0:i]) == sum(nums[i+1:len(nums)]): return i
    return -1

def leetPivotIndex(nums):
    leftSum, rightSum = 0, sum(nums)
    for i in range(len(nums)):
        rightSum -= nums[i]
        if leftSum == rightSum: return i
        leftSum += nums[i]
    return -1

print(leetPivotIndex(nums)) # Output: 3 / Output: -1 / Output: 0 / Output: 5