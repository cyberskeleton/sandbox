a = input("a= ")
a = a.replace(",", " ")
a = a.replace("!", " ")
a = a.replace(".", " ")
a = a.replace(":", " ")
a = a.split()
result = ""
for i in range(len(a)):
    if len(a[i]) > len(result):
        result = a[i]
print("result = ", result)
