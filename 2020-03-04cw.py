def iteration(a):
    a_iter = iter(a)
    try:
        while True:
            c = next(a_iter)
            if int(c) % 2 == 0:
                print(c)
    except StopIteration:
        pass
x = input('input string: ')
x_list = x.split(' ')
iteration(x_list)
