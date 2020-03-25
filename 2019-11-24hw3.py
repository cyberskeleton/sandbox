def countBits(x):
    count = 0
    while x:
        count += (x & 1)
        x >>= 1
    return count

line = input().split()
n = int(line[0])
m = int(line[1])

result = 0
for index in range(n, m + 1):
    result += countBits(index)
print(result)
