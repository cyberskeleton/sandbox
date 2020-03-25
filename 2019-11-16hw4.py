givenword = input()
word = input()
letters = []
for i in givenword:
    if i not in letters:
        letters.append(i)
result = True
for j in word:
    if j not in letters:
        result = False
if result:
    print('Ok')
else:
    print('No')
