def f(s):
    count = 0
    digit = 0
    sl = len(s)
    #print(sl)
    for c in s:
        if c.isdigit():
            count += 1
            #print("count:" + str(count))
            digit = c
            #print("digit:" + str(digit))

    if (count == 1) and (sl == int(digit)):
        return True
    else:
        return False

row = input('input row: ')
print(f(row))
