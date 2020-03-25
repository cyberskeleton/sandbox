numa = int(input())
a = input().split()
numb = int(input())
b = input().split()
c = []
for i in range(0, numa):
    if a[i] not in b:
        c.append(a[i])
print(len(c))
print(' '.join(str(x) for x in c))
