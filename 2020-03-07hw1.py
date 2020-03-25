def iterate_even(a):
    a_iter = iter(a)
    try:
        while True:
            c = next(a_iter)
            if a.index(c) % 2 == 0:
                print(c)
    except StopIteration:
        pass

def iterate_odd(a):
    a_iter = iter(a)
    try:
        while True:
            c = next(a_iter)
            if a.index(c) % 2 != 0:
                print(c)
    except StopIteration:
        pass

seq = input('input sequence: ')
seq_list = seq.split(' ')
print('even indexes: ')
iterate_even(seq_list)
print('odd indexes: ')
iterate_odd(seq_list)
