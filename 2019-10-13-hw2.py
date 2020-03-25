n = int(input('n='))
zeros = 0
while n > 0:
    n /= 5
    zeros += n
print('quantity of zeros = ', int(zeros))
