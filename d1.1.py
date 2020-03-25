x = float(input('x='))
y = float(input('y='))
z = float(input('z='))
r = float(input('r='))
from math import sqrt
d = sqrt(x**2 + y**2 + z**2) #відстань від точки до початку координат
if d > r:
    print('точка не належить кулі')
else:
    print('точка належить кулі')
