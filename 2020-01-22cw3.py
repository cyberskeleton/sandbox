import random
num = random.randint(0, 5)
num_of_shops = random.randint(2, 6)
print('we have ', num_of_shops, ' shops')
A = set()
shopname = []
for i in range(0, num):
    A.add(input('food: '))
print('assort: ', *A)
for i in range(num_of_shops):
    products = set(random.sample(A, random.randint(1, num)))
    shopname.append(products)
print(shopname)
