def check_if_arg(func):
    def check(*args, **kwargs):
        res = func(*args)
        if len(kwargs) != 0:
            raise AssertionError
        else:
            return res
    return check
@check_if_arg
def function(*args, **kwargs):
    x = list(args)
    if max(x) > sum(x):
        return 1
    else:
        return sum(x)
a = (1, 2, 3)
b = {'4':6}
print(function(*a))
