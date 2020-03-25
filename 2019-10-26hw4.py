s = input('s= ')
k = int(input('k= '))
output = ""
alphabet = ""
for i in range(97, 123):
    alphabet = alphabet + chr(i)
n = len(alphabet)
print("alphabet: ", alphabet)

for i in s:
    index = alphabet.index(i) - k
    print(index)
    if index < 0:
        index = index + n
        print(index)
    output = output + alphabet[index]
    print(alphabet[index])
print('output: ', output)
