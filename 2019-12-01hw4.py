 #10)  заміни у вихідному рядку всіх входжень даного символа даним рядком;
s = input('input string: ')
symb = input('input symbol: ')
replacement = input('input replacement: ')
result = ""
for i in s:
    if i == symb:
        result += replacement
    else:
        result += i
print(result)