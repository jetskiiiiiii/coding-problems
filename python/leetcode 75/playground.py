list = []
new = [1, 2, 3]
while new:
    list.insert(0, new[-1])
    new.pop()

print(list)
