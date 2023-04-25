"""
https://leetcode.com/problems/merge-sorted-array/?envType=study-plan&id=data-structure-i

merge:
- create a temporary list which is a copy of nums1
- temp list gets rid of the 0s and extends nums2
- since temporary list will be same length as original, set the value of each index in nums1 to be equal as temp list
"""

nums1, m, nums2, n = [1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3  # [1,2,2,3,5,6]
# nums1, m, nums2, n = [0], 0, [1], 1  # [1]
# nums1, m, nums2, n = [1], 1, [], 0  # [1]
# nums1, m, nums2, n = [2, 0], 1, [1], 1  # [1, 2]
# nums1, m, nums2, n = [1, 0], 1, [2], 1  # [1, 2]
# nums1, m, nums2, n = [1, 2, 3, 0, 0, 0], 3, [4, 5, 6], 3  # [1, 2, 3, 4, 5, 6]
# nums1, m, nums2, n = [4, 0, 0, 0, 0, 0], 1, [1, 2, 3, 5, 6], 5  # [1,2,3,4,5,6]


def merge(nums1, m, nums2, n):
    temp = nums1
    for i in range(n):
        temp.pop()
    temp.extend(nums2)
    temp = sorted(temp)
    for i in range(m + n):
        nums1[i] = temp[i]
    return nums1


num = merge(nums1, m, nums2, n)
print(num)
