n = int(input('input 3 <= n <= 10000: '))
coordinates = ()
for i in range(0, n):
    tochka = input('nazva tochky: ')
    x = input('x= ')
    y = input('y= ')
    coordinates = coordinates + (tochka, x, y)
    coordnum = len(coordinates)
    l = [(coordinates[i+1][0] - coordinates[i][0])*(coordinates[i+1][1]+coordinates[i][1]) for i in range(coordnum - 1)]
    result = abs(sum(l)/2)
    print(result)
