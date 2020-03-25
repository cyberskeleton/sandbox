def delete(s1):
    l = len(s1)
    for i in range(1, l):
        c = s1[i-1]
        print(c, s1[i])
        if c == '+' and s1[i].isdigit():
            s1 = s1.replace(c, '')
    l -= 1
    return s1


s = input('input line: ')
print('modified line: ' + delete(s))
