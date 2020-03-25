def add(self, key, value):
    if key not in self.keys():
        self[key] = []
    self.get(key).append(value)
    # print(str(key) + ' - ' + str(self.get(key)))
n = int(input())
englat = {}
for i in range(n):
    string = input().replace(' ','').split('-')
    key = string[0]
    values = string[1].split(',')
    for value in values:
        add(englat, key, value)
lateng = {}
for key, values in englat.items():
    for value in values:
        add(lateng, value, key)
for key, values in lateng.items():
    values = values.sort()

print(len(lateng))
for key in sorted(lateng.keys()):
    print(key + ' - ' + ', '.join(map(str, lateng.get(key))))
