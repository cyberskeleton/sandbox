matrix_sum = 0
message = "Sum: "
m = int(input('enter width: '))
n = int(input('enter height: '))
for i in range(0, n):
    s = input()
    s_line = s.split()
    if len(s_line) != m:
        message = "Input error! "
        matrix_sum = 0
        break
    line = list(map(int, s_line))
    matrix_sum = matrix_sum + sum(line)
if matrix_sum == 0:
    print(message)
else:
    print(message + str(matrix_sum))
