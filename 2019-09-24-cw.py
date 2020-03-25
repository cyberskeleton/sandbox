from math import *

a = float(input('a='))   # angle in radians
v = float(input('v='))   # m/s
h = float(input('h='))   # metres
g = 9.8   # m/s
length = (v * cos(a))*(((v * sin(a))/g) + sqrt((2 / g) * (h + ((v ** 2)*sin(a))/(2 * g))))
print('точка у яку влучить снаряд: ', length)
