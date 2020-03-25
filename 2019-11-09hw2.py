n = int(input())
vertices = []
sp = []
sum1 = 0
sum2 = 0
while n < 3 or n > 50000:
    n = int(input())
for i in range(0, n):
    s = input()
    sp = s.split()
    vertices.append((int(sp[0]), int(sp[1])))
for i in range(0, n - 1):
    sum1 = sum1 + vertices[i][0]*vertices[i+1][1]
    sum2 = sum2 + vertices[i][1]*vertices[i+1][0]
sum1 = sum1 + vertices[n-1][0]*vertices[0][1]
sum2 = sum2 + vertices[0][0]*vertices[n-1][1]
area = abs(sum1 - sum2)/2
print("%.3f" %(area))
