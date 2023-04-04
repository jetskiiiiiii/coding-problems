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
- compare the len of the set to the len of original string
- if two lenghts are equal, no more duplicates exist (no more values to count towards palindrome length)
- if set and list are not equal in length, iterate through the list, looking for duplicates
- when a duplicate is found, add 2 to palindrome, and remove duplicates from list so program can recompare original to set
- at the end, if length is completely empty, return palindrome as is, else add 1 to the palindrome count (to account for the single value that the center of the palindrome ('bab' where 'a' is center))

fasterLongestPalindrome:
- for every unique value in s i.e. set(s), add the # of occurances (count) of that value if even or count-1 if odd
- if there are any odd values present in s, total length of palindrome increases by 1
"""
import time

s = "abbccccd"  # 4/8 -> 7
s = "aAbccccdd"  # 4/8 -> 7
# s = "a"  # 1/1 -> 1
# s = "aabbcc"  # 3/6 -> 6
# s = "abbccc"  # 3/6 -> 5
# s = "abb"  # 2/3 -> 3
# s = "abaab"  # 2/5 -> 5
# s = "abcccab"  # 3/7 -> 7
# s = "aaaa"  # 1/4 -> 4
# s = "tattarrattat"  # 3/13 -> 12
# s = s = "aabbbcccd"  # 7


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


def memoryLongestPalindrome(s: str) -> int:
    count = {}

    for i in set(s):
        count[i] = s.count(i)

    print(count)

    odd = [j - 1 for j in count.values() if j % 2 == 1] + [1]
    even = [j for j in count.values() if j % 2 == 0]
    return sum(even) if len(odd) == 1 else sum(even) + sum(odd)


def fastLongestPalindrome(s: str) -> int:
    p = odd = 0
    for i in set(s):
        p += s.count(i) if s.count(i) % 2 == 0 else s.count(i) - 1
        if s.count(i) % 2 == 1:
            odd = 1

    return p + odd


print(fastLongestPalindrome(s))
