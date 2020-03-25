# Т16.17 Описати генератор-функцію, що повертає всі доданки нескінченної
# суми дійсних чисел, заданої співвідношенням, та обчислити суму всіх
# доданків при заданому значенні x, що за абсолютною величиною не
# перевищують заданого ε > 0:
def generator(x, eps):
    power = 1
    try:
        while True:
            power += 1
            addend = sign(power) * x**power/power
            if addend > eps:
                raise StopIteration
            yield addend
    except StopIteration:
        pass

def sign(power):
    if power % 2 == 0:
        return -1
    return 1

x, eps = float(input('input x: ')), float(input('input eps: '))

print('y = ln(1+x) Addends:')
counter = 0
print(counter, x)
for x in generator(x, eps):
    counter += 1
    print(counter, x)
