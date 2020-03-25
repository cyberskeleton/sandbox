x = float(input('x='))
if x <= 0:
    y = 0
elif 0 < x <= 1:
    y = x**2
else:
    y = x**4
print('значення фунції y =', y)
