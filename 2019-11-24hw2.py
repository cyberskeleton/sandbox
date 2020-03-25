t = int(input('input tests number: '))
n = []
m = []
for i in range(t):
    line = input('n m: ').split()
    nn = int(line[0])
    mn = int(line[1])
    n.append(nn)
    m.append(mn)

for i in range(t):
    nn = n[i]
    s = 0
    if nn == 2:
        s = 2
    elif nn > 2:
        s = 2
        for k in range(2, nn):
            s += k * k * (2 << (k-1))
    print(s % m[i])
