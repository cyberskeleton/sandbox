f = open('tokill/doc1', 'w')
for i in range(1, 10):
    for j in range(i-1):
        print(i, end=' ', file=f)
    print(str(i) + '\n', file=f)
f.close()
f = open('tokill/doc1', 'r')
data = f.read()
print(data)
f.close()
