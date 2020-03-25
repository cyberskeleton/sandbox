def lcm(x, y):
    return x * y // gcd(x, y)


def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)


n = int(input('input n: '))
listk = []
k = 0
for i in range(n):
    k += 1
    listk.append(k)
el = lcm(listk[0], listk[1])
for j in range(2, len(listk)):
    el = lcm(el, listk[j])
print(el)
