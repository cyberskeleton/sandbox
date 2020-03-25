m = int(input('m='))
n = int(input('n='))
x = m * n
if m != 0 and n != 0:
    maxim = max(m, n)
    if maxim % m == 0 and maxim % n == 0:
        x = maxim       # нск = x
        print('x= ', x)
    else:
        maxim += 1
        print('x= ', x)
