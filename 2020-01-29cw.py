import pickle
f = open('document', 'w')
s = input('input text: ')
for i in s:
    if i == '.' or i == ',':
        s = s.replace(i, '')
f.write(s)
f.close()
file = open('document', 'r')
data = file.read()
print(data)
binary = open('tokill/bin1', 'wb')
for i in data:
    pickle.dump(ord(i), binary)
binary.close()
binary = open('tokill/bin1', 'br')
binarydata = binary.read()
print(binarydata)
