n = int(input('n='))
a1 = int(input('a1='))
p = 0
d = 0
for i in range(1, n):
    a2 = int(input('a2='))
    if a1 > 0 and a2 > 0:
        p += 1
    if (a1 > 0 and a2 < 0) or (a1 < 0 and a2 > 0):
        d += 1
    a1 = a2
print('positive pairs: ', p)
print('pairs with different signs: ', d)
