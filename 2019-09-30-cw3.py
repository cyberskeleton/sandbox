n = int(input('n='))
for i in range(1, n):
    if (i**2)%10 == i%10:
        print(i)
