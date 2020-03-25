f = open('realnum.txt', 'r')
data = f.read()
res = 0
for num in data.split(' '):
    if int(num) < 0:
        res += 1
        print(num)
print('total: ', res)
