def f(n):
    if n % 10 > 0:
        return n % 10
    if n == 0:
        return 0
    else:
        return f(n / 10)
def s(p, q):
    sum = 0
    for j in range(p, q + 1):
        sum += f(j)
    return sum

pmass = []
qmass = []
while True:
    pq = input('input p q: ').split()
    p = int(pq[0])
    q = int(pq[1])
    if p < 0 or q < 0:
        break
    pmass.append(p)
    qmass.append(q)
for i in range(len(pmass)):
    print(int(s(pmass[i], qmass[i])))
