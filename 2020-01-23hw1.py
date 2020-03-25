import random
n = int(input('input n: '))
numbers = set()
for i in range(n):
    numbers.add(random.randint(1, 50))
print(numbers)
fibgroup = set()
onetwogroup = set()

def isfib(a):
    fibonacchi = {0, 1, 2, 3, 5, 8, 13, 21, 34}
    return a in fibonacchi

def isnum(a):
    return (str(a)[0] == '1') or (str(a)[0] == '2')

for i in numbers:
    if isfib(i):
        fibgroup.add(i)
    if isnum(i):
        onetwogroup.add(i)
print('Fibonacci: ', sorted(fibgroup))
print('onetwo: ', sorted(onetwogroup))
