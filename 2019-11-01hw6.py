#7.37. Скласти програми обчислення кількості компонент дійсного вектора б) які належать заданому відрізку прямої.
k = int(input('k= '))
b = int(input('b= '))

v = input().split()
length = int(input())
count = 0
for i in range(0, length):
    if i not in v:
        break
    else:
        count += 1
        print(count)
