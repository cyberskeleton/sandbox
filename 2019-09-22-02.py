from random import *

n=0
while n < 1:
    n = int(input('Input a natural number: '))

a = list()   # create empty list
for i in range(0, n):   # in range 0 to n
    a.append(uniform(-100, 100))   # add random numbers to list a
print(a)
p = 0   # number of positive neighbours
d = 0   # number of neighbours with different signs

for i in range(0, n - 1):   # check other numbers
    if a[i] > 0 and a[i + 1] > 0:
        p += 1
    if (a[i] > 0 and a[i + 1] < 0) or (a[i] < 0 and a[i + 1] > 0):
        d += 1
print('number of positive pairs: ', p)
print('number of pairs with different signs: ', d)
