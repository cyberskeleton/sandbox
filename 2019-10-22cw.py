s = input()
s.isdigit()
if True:
    num = int(s)
    t = chr(77)*(num // 1000)
    h = chr(67)*(num // 100 % 10)
    ten = chr(88)*(num // 10 % 10)
    o = chr(73)*(num % 10)
    summa = t + h + ten + o
    print(summa)
