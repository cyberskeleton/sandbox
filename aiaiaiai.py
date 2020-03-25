def f(s):
    for i in range(0, len(s)):
        if s[i] == '+':
            s = s.replace(s[i], '')
            print(s)
    return s


s = input('input line: ')
ans = f(s)
print(ans)
