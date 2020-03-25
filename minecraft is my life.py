def f(s):
    count = 0
    digit = 0
    for x in s:
        if x.isdigit():
            count += 1
            #print(count)
            digit = x
            #print(digit)
        if len(s) == int(digit) and count == 1:
            return True
        else:
            return False


row = input('input row: ')
answer = f(row)
print(answer)

