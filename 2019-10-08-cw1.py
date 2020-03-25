from math import *
x0 = int(input('x0='))
y0 = int(input('y0='))
x1 = int(input('x1='))
y1 = int(input('y1='))
x2 = int(input('x2='))
y2 = int(input('y2='))
x3 = int(input('x3='))
y3 = int(input('y3='))
h = int(input('h='))
m = sqrt((x3 - x0)**2 + (y3 - y0)**2)       # AD
n = sqrt((x2 - x0)**2 + (y2 - y0)**2)       # AC
k = sqrt((x1 - x0)**2 + (y1 - y0)**2)       # AB
i = sqrt((x3 - x2)**2 + (y3 - y2)**2)       # CD
if k > h:
    length = h
else:
    AN = sqrt(k**2 + k**2)
    p = (m + n + i) / 2
    S = sqrt(p*(p - m)*(p - n)*(p - i))
    AE = (2*S)/i
    length = (AN * AE)/k
print('length=', length)
