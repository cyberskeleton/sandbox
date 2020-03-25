import sympy

def read_file():
    file = open('tokill/coefficients.txt', 'r')
    coefs = file.read()
    coefs_split = coefs.strip('\n').split(', ')
    return(coefs_split)
def count_poly(x, coefficient):
    polynomial = [x**3, x**2, x]
    result = 0
    for i in range(0, len(polynomial)):
        polynomial[i] = int(polynomial[i])*int(coefficient[i])
        print(polynomial[i])
        result += int(polynomial[i])
    return(result)
print(count_poly(3, read_file()))
def count_derivative(x, coefficient):
    polynomial = [3*x**2, 2*x, 1]
    result = 0
    for i in range(0, len(polynomial)):
        polynomial[i] = int(polynomial[i])*int(coefficient[i])
        print(polynomial[i])
        result += int(polynomial[i])
