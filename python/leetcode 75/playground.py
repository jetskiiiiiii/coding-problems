s = "abababab"
b = "a"
for i in range(1, len(b), 2):
    if b[i - 1] == b[i]:
        print(True)
    else:
        print(False)

for i in range(2):
    print(b[i])
