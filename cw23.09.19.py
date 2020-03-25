n = int(input('n='))
maxim = int(input('maxim='))
ai = int(input('a='))
for i in range(1, n - 1):
    if ai > maxim:
        maxim = ai
    print(maxim)
