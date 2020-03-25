n = int(input('n='))
if n % 2:
    a = 1
else:
    a = 2
for i in range(a + 2, n + 1, 2):
    a += 1
print(a)
