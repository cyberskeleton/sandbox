word = input()
n = int(input())
wlist = []
key = 0
for i in range(0, n):
    keyword = input()
    wlist.append(keyword)
letters = []
for j in word:
    if j not in letters:
        letters.append(j)
# result = [w for w in wlist if all(i in letters for i in w)]
x = 0
list = []
for w in wlist:
    letters_copy = letters.copy()
    list = list(w)
    word_in_list = True
    while word_in_list:
        for l in list:
            if l in letters_copy:
                word_in_list = False
            else:
                letters_copy.remove(l)

    x += 1
# x = len(result)
print(x)
