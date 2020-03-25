#def lcm(x, y):
   # return x * y // gcd(x, y)

def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)

count = 0
ab = input('a b: ').split()
a = int(ab[0])
b = int(ab[1])
p = a*b
for i in range(1, b + 1):
    if p % i == 0 and gcd(i, p/i) == a:
        count += 1
print(count)
