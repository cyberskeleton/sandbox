s = input('введіть рядок ')
count = 0
s = s.replace('//', '/')
s = s.replace('**', '*')
for i in s:
    if i == '*' or i == '/' or i == '%' or i == '+' or i == '-':
        count = count + 1
print('count=', count)
