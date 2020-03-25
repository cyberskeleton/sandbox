n = int(input('введіть 0 < n < 10**10 '))
def count(x):
    m = 5
    zeros = 0
    while x >= m:
        zeros += x // m
        m *= 5
    return zeros
print(count(n))
