s = "aabbbcccd"  # 7
count = {}
for i in set(s):
    count[i] = s.count(i)

odd = [j - 1 for j in count.values() if j % 2 == 1] + [0]
even = [j for j in count.values() if j % 2 == 0]

print(odd, even)
print(1 % 2)
