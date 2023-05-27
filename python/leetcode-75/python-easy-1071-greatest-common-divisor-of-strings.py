"""
https://leetcode.com/problems/greatest-common-divisor-of-strings/

gcdOfStrings:
- go through each word, letter by letter
- find first place where letters don't match or letter repeats
"""

str1, str2 = "ABCABC", "ABC"
# str1, str2 = "ABABAB", "ABAB"
# str1, str2 = "LEET", "CODE"
# str1, str2 = "ABCDEF", "ABC"
# str1, str2 = (
#     "TAUXXTAUXXTAUXXTAUXXTAUXX",
#     "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX",
# )
# str1, str2 = "ABABABAB", "ABAB"
str1, str2 = "A", "AA"


def gcdOfStrings(str1: str, str2: str) -> str:
    if str1 == str2:
        return str1
    i = 1
    biggest = ""
    while i != max(len(str1), len(str2)):
        answer = str1[:i]
        if len(str1) % len(answer) != 0:
            i += 1
            continue
        factor1 = len(str1) // len(answer)
        factor2 = len(str2) // len(answer)
        if answer * factor1 == str1 and answer * factor2 == str2:
            biggest = answer
        i += 1
    return biggest


print(gcdOfStrings(str1, str2))
