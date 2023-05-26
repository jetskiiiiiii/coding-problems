"""
https://leetcode.com/problems/merge-strings-alternately/

mergeAlternately:
- append first letter of each word into answer
- modify each word to get rid of first letter
"""
word1, word2 = "abc", "pqr"
# word1, word2 = "ab", "pqrs"
# word1, word2 = "abcd", "pq"


def mergeAlternately(word1: str, word2: str) -> str:
    answer = ""
    while word1 and word2:
        answer += word1[0]
        answer += word2[0]
        word1 = word1[1:]
        word2 = word2[1:]
    answer += word1 + word2
    return answer


print(mergeAlternately(word1, word2))
