# Скласти програму для обчислення суми всіх діагональних елементів
# дійсної квадратної матриці.
# Вказівка: використати спискоутворення
diag_sum = 0
message = "Sum: "
m = int(input('enter width: '))
n = int(input('enter height: '))
for i in range(0, n):
    s = input()
    s_line = s.split()
    if len(s_line) != m:
        message = "Input error! "
        diag_sum = 0
        break
    line = list(map(int, s_line))
    diag_sum = diag_sum + line[i]
if diag_sum == 0:
    print(message)
else:
    print(message + str(diag_sum))
