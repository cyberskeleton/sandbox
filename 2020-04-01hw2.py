#Т19.14 Виконати задачу Т19.7 з використанням метакласів замість
#декоратора.
import time
import types
def timeit(method):
    def timed(*args, **kwargs):
        ts = time.time()
        result = method(*args, **kwargs)
        te = time.time()
        print(method.__name__, (te - ts) * 1000, ' ms')
        return result
    return timed

class Meta(type):
    def __new__(cls, name, bases, attr):
        for name, value in attr.items():
            if type(value) is types.FunctionType or type(value) is types.MethodType:
                attr[name] = timeit(value)
        return super(Meta, cls).__new__(cls, name, bases, attr)

class MyClass(metaclass=Meta):
    def my_method(self):
        print('result: no result')

    def my_another_method(self):
        result = 0
        for i in range(0, 100000):
            result += 1
        print('result: ', result)

m = MyClass()
m.my_another_method()
m.my_method()
