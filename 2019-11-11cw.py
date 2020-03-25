n = int(input('number of cars: '))
search_brand = input('input brand you are looking for: ')
brands = []
avto = []
for i in range(0, n):
    brand = input('brand: ')
    uid = input('id: ')
    owner = input('name of owner: ')
    car = {'brand': brand, 'id': uid, 'owner': owner}
    avto.append(car)
owners = []
for car in avto:
    value = car.get('brand')
    if value == search_brand:
        owners.append(car.get('owner'))
        owners.append(car.get('id'))
print('name and id vidpovidno: ', owners)
for car in avto:
    brands.append(car.get('brand'))
ubrands = []
for x in brands:
    if x not in ubrands:
        ubrands.append(x)
for ubrand in ubrands:
    count = 0
    for brand in brands:
        if ubrand == brand:
            count += 1
    print('brand: ', str(ubrand), 'number of cars: ', str(count))
