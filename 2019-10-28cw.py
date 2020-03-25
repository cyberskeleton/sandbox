a = []
b = []
n = int(input("n= "))
result = 0
for i in range(n):
    x = float(input("{} coordinaty 1:".format(i)))
    a.append(x)
    y = float(input("{} coordinaty 2:".format(i)))
    b.append(y)
for i in range(n):
    result += a[i]*b[i]
print("result= ", result)
