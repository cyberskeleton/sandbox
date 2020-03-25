from math import *
r = float(input('r= '))
n = 1
if r < 1 or r > 5:
    print('введіть 1 <= r <= 5')
else:
    while floor(n * r) < n * r:
        n += 1
    print('n = ', n)
