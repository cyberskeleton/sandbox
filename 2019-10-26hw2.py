s = input('s= ')
k = ""
for i in s:
    r = i
    if i.isalpha():
        r = i + i
    k = k + r
print(k)
