import random
n = random.randint(10, 20)
print('number of elements: ', n)
A = set()
B = []
for i in range(0, n):
    A.add(random.randint(0, 100))
print('unsorted: ', *A)
for i in range(0, len(A)):
    minim = min(A)
    B.append(minim)
    A.remove(minim)
print('sorted: ', *B)
