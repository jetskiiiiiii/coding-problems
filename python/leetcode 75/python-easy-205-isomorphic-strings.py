"""
https://leetcode.com/problems/isomorphic-strings

pseudocode:
isIsomorphic (TIME LIMIT):
1. set a count variable to keep track of unique charater occurunces
2. count starts 0, and 0 represents the first unique character
3. each occurance of that character gets assigned the value of count
4. do for s, t
5. compare s, t

fastIsIsomorphic (WRONG):
- create dictionary and replace strings with values of dictionary
1. create empty dict
2. iterate through s
3. TRY if dict[s[i]] matches t[i]: continue
else: return False (dict[s[i]] key exists but t[i] is different than dict value)
4. if EXCEPT, assign t[i] as value for key dict[s[i]] (no s[i] key exists)

setIsIsomorphic:
1. create lists of only unique characters of s, t with set conversion
2. if conversion produces different length sets, automatically not isomorphic
3. use empty dict to keep track of what values are supposed to be
4. iterate through each position
5. TRY value of dict (with current element of s as key) should be current element of t
6. if match, go to next iteration; else t has multiple values associated with key and s, t are not isomorphic
7. EXCEPT means key doesn't exist, create key value pair with s[i] as key and t[i] as value
8, if loop finishes to end, each element in s is associated with only one element in t; s, t are isomorphic
"""

# s, t = "egg", "add"
# s, t = "bacd", "baba"
# s, t = "ab", "ac"
# s, t = "foo", "bar"
s, t = "paper", "title"

def isIsomorphic(s, t):
    char_s, char_t, count = [0 for x in range(len(s))], [0 for x in range(len(t))], 0
    for i in range(len(s)):
        for j in range(len(s)):
            if s[i] == s[j]: char_s[j] = count
            if t[i] == t[j]: char_t[j] = count
            
            if char_t == char_s: continue
            else: return False
        count += 1
    return True

def fastIsIsomorphic(s, t):
    dict_unique = {}
    if s == t: return True
    for i in range(len(s)):
        try: 
            if dict_unique[s[i]] == t[i]: continue
            else: return False
        except:
            dict_unique[s[i]] = t[i]
    print(len(dict_unique), len(t))
    if len(dict_unique) == len(t): return False
    else: return True
    
def setIsIsomorphic(s, t):
    if s == t: return True
    
    set_s, set_t, dict_unique = {x for x in set(s)}, {x for x in set(t)}, {}
    if len(set_s) != len(set_t): return False
    
    for i in range(len(s)):
        try: 
            if dict_unique[s[i]] == t[i]: continue
            else: return False
        except:
            dict_unique[s[i]] = t[i]
            
    return True

def leetIsIsomorphic(s, t):
    map_s, map_t = [], []
    for x in s: map_s.append(s.index(x))
    for x in t: map_t.append(t.index(x))
    if map_s == map_t: return True
    return False

print(leetIsIsomorphic(s, t)) # True / False / True / False / True