def ln(x, n):
    try:
        assert abs(x) < 1, str(x) + '> 1'
    except AssertionError:
        print('abs(x) > 1 ')
    if type(n) is not int or type(x) is not float:
        raise TypeError
    else:
        res = 0
        for i in range(1, n + 1):
            el = (((x) ** (i)) / i) * ((-1) ** (i + 1))
            res += el
        return res
x = float(input('input x: '))
n = int(input('how many chlens you want to calculate: '))
print(ln(x, n))
