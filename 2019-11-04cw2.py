karty = [('six', 0), ('seven', 1), ('eight', 2), ('nine', 3), ('ten', 4), ('valet', 5), ('dame', 6), ('king', 7), ('trump', 8)]
suites = ['kresty', 'piki', 'bubni', 'chervi']
result = False
trump = 'kresty'
karta1 = ('chervi', 1)
karta2 = ('bybni', 4)
if karta1[1] == karta2[1]:
    value1 = [item[1] for item in karty if item[0] == karta1[0]]
    value2 = [item[1] for item in karty if item[0] == karta2[0]]
    if value1 > value2:
        result = True
    else:
        if karta1[1] == trump:
            result = True
print('karta1 beats karta2', result)
