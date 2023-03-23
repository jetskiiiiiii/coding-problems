"""
pseudocode:

1. create sum variable, initialize to 0
2. assign indices in runningSum as num[i] + sum
3. update sum += num[i] 
"""

nums = [1,2,3,4]
def runningSums(nums):
    runningSum = []
    sum = 0 # keep track of previous sums
    
    for i in range(0, len(nums)):
        runningSum.append(nums[i] + sum)
        sum = sum + nums[i] # update value to the sum including current index
    return runningSum

# trying to make a shorter version with list comprehension
def shortRunningSums(nums):
    # return [(nums[x] + nums[i]) for x in range(len(nums)) for i in range(x)]
    # sum = 0
    # return [[i for i in x] + x for x in range(len(nums))]
    return [()]
    
print(shortRunningSums(nums)) # expected output [1, 3, 6, 10]
