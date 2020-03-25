def C(a, b):
    e = 'k cant be bigger than n'
    if b == 0 or a == b:
        return 1
    if a != 1:
        return C(a - 1, b - 1) + C(a - 1, b)
    else:
        return e


n = int(input('input n: '))
k = int(input('input k: '))
result = C(n, k)
print(result)
