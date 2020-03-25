import random
n = random.randint(10, 20)
print('number of elements: ', n)
A = set()
ded = set()
for i in range(0, n):
    A.add(random.randint(0, 10))
for x in A:
    for y in A:
