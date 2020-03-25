n = int(input('n='))
a1 = int(input('a1='))
a2 = int(input('a2='))
i = 1
counter = 0
if a1 > a2:
    counter = 1
for i in range(1, n - 1):
    ai = int(input('ai='))
    if a2 > a1:
        counter += 1
    if a2 > ai:
        counter += 1
    a1 = a2
    a2 = ai
if a2 > a1:
    counter += 1
print(counter)
