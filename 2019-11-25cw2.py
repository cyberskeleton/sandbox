def number(a, d, n):
    if n == 1:
        return a
    else:
        return number(a + d, d, n-1)


def summa(a, d, n):
    if n == 1:
        return a
    else:
        return a + summa(a + d, d, n-1)


a1 = int(input('first element: '))
np = int(input('number of elements: '))
dp = int(input('input common difference: '))
result = summa(a1, dp, np)
print('sum of ' + str(np) + ' elements equals ' + str(result))
resultnum = number(a1, dp, np)
print(str(np) + ' element equals ' + str(resultnum))
