azazel = open('tokill/azazel.txt', 'r+', encoding='utf-8')
specials = {ord(','), ord('.'), ord(';'), ord(':'), ord('-'), ord('!'), ord('?'), ord('"'), ord("'"), 8212, 171, 8230, 187}
print(specials)
lines = azazel.read()
for i in lines:
    if ord(i) in specials:
        print(i)
        newline = lines.replace(i, '')
        #azazel = open('azazel.txt', 'w', encoding='utf-8')
        azazel.write(newline)
for i in lines:
    if ord(i) == ord('\n'):
        a = azazel.readline()
        for j in a:
            print(j)
#data = azazel.read()
#print(data)
azazel.close()
