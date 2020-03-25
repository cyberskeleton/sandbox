#17.2
def mydec(func):
    def dec(*args, **kwargs):
        a = int(input('input lower bound: '))
        b = int(input('input upper bound: '))
        r = func(*args, **kwargs)
        if a <= r <= b:
            return r
    return dec

@mydec
def calculate_total_sum(*args):
    total_sum = 0
    for arg in args:
        total_sum += arg
    return total_sum

print(calculate_total_sum(5, 4, 3, 2, 1))
