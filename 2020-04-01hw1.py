#19.7 Описати декоратор класу, який здійснює модифікацію класу з метою
# обчислення часу роботи усіх методів класу. Під час виклику методу
# показувати ім’я методу та час його роботи. Застосувати цей декоратор до
# класу Btree (див. приклад до теми «Рекурсивні структури даних») та
# побудувати бінарне дерево пошуку.
import time
def timeit(method):
    def timed(*args, **kwargs):
        ts = time.time()
        result = method(*args, **kwargs)
        te = time.time()
        print(method.__name__, (te - ts) * 1000, ' ms')
        return result
    return timed

class MyClass:
    @timeit
    def my_method(**kwargs):
        print('result: no result')

    @timeit
    def my_another_method(**kwargs):
        result = 0
        for i in range(0, 100000):
            result += 1
        print('result: ', result)

MyClass.my_method()
MyClass.my_another_method()
