from math import *

x = 0
while x <= 0:
    x = float(input('Input x > 0: '))

y = 1
while y <= 1:
    y = float(input('Input y > 1: '))

res = ceil(x/y)
if res <= x/y + 1:
    k = res
    print('k = ', k)
else:
    print('No solutions found')
