"""
https://leetcode.com/problems/first-bad-version

firstBadVersion:
- check if low is bad, if true then first bad version found
- if middle index is bad
    - move range from low:high to low+1:mid+1, and repeat step 1
- if middle index is false
    - move range from low:high to mid+1:high, and repeat step 1
"""

n, bad = 5, 4
# n, bad = 1, 1
# n, bad = 300, 208
# n, bad = 3, 2
n, bad = 2126753390, 1702766719


def isBadVersion(n: int) -> bool:
    if n >= bad:
        return True
    return False


def firstBadVersion(n: int) -> int:
    low, high = 1, n
    while low != high:
        mid = (low + high) // 2  # order of operations important!
        if isBadVersion(low):
            return low
        elif isBadVersion(mid):
            low = low + 1
            high = mid + 1
        else:
            low = mid + 1
    return low


print(firstBadVersion(n))
