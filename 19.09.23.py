from math import *

n = 0
while n < 1:
    n = int(input('n='))
r = log2(n)
k = ceil(r)
for i in range(k, n+k+1):
    if 2**i > n:
        print(2**i)
        break
