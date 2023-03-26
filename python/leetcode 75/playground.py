s, t = "ab", "baab" # true

map = [0]

for x in range(1, len(s)+1):
    map.append(t[map[-1]:].index(s[x-1])+map[-1]+x)
    
print(map)