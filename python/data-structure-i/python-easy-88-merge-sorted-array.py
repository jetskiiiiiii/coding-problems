"""
https://leetcode.com/problems/merge-sorted-array/?envType=study-plan&id=data-structure-i

merge:
-
"""

nums1, m, nums2, n = [1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3  # [1,2,2,3,5,6]
nums1, m, nums2, n = [0], 0, [1], 1  # [1]
# nums1, m, nums2, n = [1], 1, [], 0  # [1]
nums1, m, nums2, n = [2, 0], 1, [1], 1  # [1, 2]
# nums1, m, nums2, n = [1, 0], 1, [2], 1  # [1, 2]


def merge(nums1, m, nums2, n):
    if n + m != 1:
        for i in range(m + n):
            if nums1[i] > nums2[0] or nums1[i] == 0:
                nums1.insert(i, nums2[0])
                nums1.pop()
                nums2 = nums2[1:]
                if nums2 == []:
                    break
    if m == 0:
        nums1[0] = nums2[0]
    print(nums1)


def merge(nums1, m, nums2, n):
    if n + m != 1:
        index1, index2 = 0, 0
        while index1 < m + n or index2 != n:
            print(index1, index2)
            if nums1[index1] > nums2[index2] or nums1[index1] == 0:
                nums1.insert(index1, nums2[index2])
                nums1.pop()
                index2 += 1
            index1 += 1
    if m == 0:
        nums1[0] = nums2[0]
    print(nums1)


merge(nums1, m, nums2, n)
