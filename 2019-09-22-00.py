from random import randint

n=0
while n < 1:
    n = int(input('Input a natural number: '))

a = list()   # create empty list
for i in range(0, n + 1):   # in range 0 to n + 1
    a.append(randint(0, 99))   # add random numbers to list a
print(a)
q = 0   # number of occurrences (cases) when an element is greater than its neighbour
if a[0] > a[1]:   # check lower bound
    q += 1
if a[n] > a[n-1]:   # check upper bound
    q += 1
for i in range(1, n):   # check other numbers
    if a[i] > a[i - 1]:
        q += 1
    if a[i] > a[i + 1]:
        q += 1
print('number of cases: ', q)
