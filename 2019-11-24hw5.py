ab = input('a b: ').split()
a = int(ab[0])
b = int(ab[1])
listek = []
for i in range(a, b + 1):
    s = str(i)
    for j in s:
        temp = []
        for c in s:
            if c not in temp:
                temp.append(c)
        if len(temp) == 4 and i not in listek:
            listek.append(i)
results = list(map(str, listek))
print(" ".join(results))