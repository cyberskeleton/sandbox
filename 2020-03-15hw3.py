# Т17.11
# Побудувати декоратор, який здійснює трасування рекурсивної функції,
# показуючи номер рекурсивного виклику (глибину вкладень викликів) та
# значення параметрів перед викликом функції, а також номер рекурсивного
# виклику та результат після виклику функції. З використанням декоратора
# виконати трасування рекурсивних функцій для обчислення факторіалу та
# чисел Фібоначчі.
# Вказівка: описати глибину вкладення викликів як нелокальну змінну
# (nonlocal) у функції-декораторі.

def trace(func):
    count = 0
    def print_trace(*args, **kwargs):
        nonlocal count
        result = func(*args, **kwargs)
        print("count: " + str(count), func.__name__ + ' ' + str(result))
        count += 1
        return result
    return print_trace

@trace
def factor(n):
    if n < 1:
        return 0
    if n == 1:
        return n
    return n * factor(n - 1)

@trace
def fib(n):
    if n > 1:
        return fib(n-1) + fib(n-2)
    return n

factor(5)
fib(9)
