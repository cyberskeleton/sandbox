nm = input().split()
n = int(nm[0])
m = int(nm[1])
words = []
for i in range(0, n):
    word = input()
    if word not in words:
        words.append(word)
essay = []
for i in range(0, m):
    s = input()
    s = s.lower().replace('.','').replace(',','').replace(':','').replace(';','')
    s = s.replace('-','').replace('\'','').replace('\"','').replace('!','').replace('?','')
    list = s.split()
    for word in list:
        if word not in essay:
            essay.append(word)
error = ''
for w in words:
    if w not in essay:
        error = 'The usage of the vocabulary is not perfect.'
        break
for w in essay:
    if w not in words:
        error = 'Some words from the text are unknown.'
        break
if len(error) == 0:
    print('Everything is going to be OK.')
else:
    print(error)
