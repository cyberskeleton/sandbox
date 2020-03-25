mountains = []
n = int(input())
result = ("", 0)
for i in range(0, n):
    mount = input('name: ')
    h = float(input('height: '))
    mountains.append((mount, h))
for mount in mountains:
    if mount[1] > result[1]:
        result = mount
print(result)
