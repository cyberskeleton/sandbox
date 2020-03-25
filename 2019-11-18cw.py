def isprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def twins(end):
    for i in range(3, end + 1):
        j = i + 2
        if isprime(i) and isprime(j):
            print(i, j)


twins(25)
