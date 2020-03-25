f = input('введіть рядок')
n = 0
for i in f:
    if i == '(':
        n = n + 1
    elif i == ')':
        n = n - 1
        if n < 0:
            break

if 0 == n:
    print('true')
else:
    print('false')
