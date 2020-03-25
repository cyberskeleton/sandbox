def f(r, n, k):
    sum = 0
    if r == 0 and n == 0:
        return 1
    if n > 0 and 0 <= r < n*(k - 1) + 1:
        for i in range(k):
            sum += f(n-1, r-i, k)
    return sum

kmass = []
nmass = []
tmass = []
while True:
    knt = input('input k n t: ').split()
    k = int(knt[0])
    n = int(knt[1])
    t = int(knt[2])
    if k == 0 or n == 0 or t == 0:
        break
    kmass.append(k)
    nmass.append(n)
    tmass.append(t)
#for i in range(len(kmass)):
 #   print(int(f()))
m = 10**t
x = k**n
case = 1
while True:
    m = 1
    for i in range(t):
        m *= 10
        res = f(k % m, n, m)
        case += 1
        print('Case #', case, ':', res)
