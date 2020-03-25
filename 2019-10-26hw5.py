s = input('s= ')
output = ""
for i in range(65, 123):
    n = s.count(chr(i))
    if n > 0:
        for c in range(0, n):
            output = output + chr(i)
print("output: ", output)
