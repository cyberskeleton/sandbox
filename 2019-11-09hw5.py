list = []
result = []
n = int(input('number of students: '))
for i in range(0, n):
    name = input(str(i) + '. name: ')
    group = input(str(i) + '. group: ')
    mark1 = int(input(str(i) + '. mark1: '))
    mark2 = int(input(str(i) + '. mark2: '))
    mark3 = int(input(str(i) + '. mark3: '))
    list.append((name, group, mark1, mark2, mark3))
for i in range(0, n):
    st = list[i]
    if (st[2] >= 4) and (st[3] >= 4) and (st[4] >= 4):
        result.append(st)
print(result)
