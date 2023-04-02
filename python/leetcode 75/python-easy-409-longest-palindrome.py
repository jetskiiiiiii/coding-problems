"""
https://leetcode.com/problems/longest-palindrome

longestPalindrome:
- if s == [] or [x] or [xx], len(s) is palindrome length
- else iterate through string
- if the value is in the count dict and there is already one occurance of the value, the palindrome length goes up 2 and count resets for that value
- if there has been no occurance, add 1 to the count
- once string has been iterated through, if there is anything left in count dict, it will be keys with values of 1 (so add one of those occurances to the palindrome)
- if count is empty, just return the palindrome

fastLongestPalindrome:
- 
"""

# s = "abccccdd"  # 7
# s = "a"  # 1
# s = "aaaa" # 4
s = "abbb"  # 3


def longestPalindrome(s: str) -> int:
    if len(s) == 0 or len(s) == 1 or (len(s) == 2 and s[0] == s[1]):
        return len(s)

    palindrome = 0
    count = {}
    for i in s:
        if i in count and count[i] == 1:
            palindrome += 2
            del count[i]
        else:
            count[i] = 1
        print(i, palindrome, count)

    if count != {}:
        return palindrome + 1
    else:
        return palindrome


# def fastLongestPalindrome(s: str) -> int:
#     s = sorted(s)
#     palindrome = 0
#     for i in range(1, len(s)):
#     while
#         if s[i - 1] == s[i]:
#             palindrome += 2
#             # s = s[: i - 1] + s[i + 1 :]
#     if len(s) - palindrome == 0:
#         return palindrome
#     return palindrome + 1


print(fastLongestPalindrome(s))
