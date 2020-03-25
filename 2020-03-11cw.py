def mydec(func):
    def _mydec(*args):
        r = func(args)
        return abs(r)
    return _mydec()
@mydec
def mult(*args):
    res = 0
    for arg in args:
        res = arg * res
    return res

arg1 = int(input('arg1: '))
arg2 = int(input('arg2: '))
print(mult(arg1, arg2))
