import random
# names = ['Semiramis Sicilian',
#          'Julius Genevieve',
#          'Rwanda Cohn',
#          'Quito Sutherland',
#          'Eocene Wheller',
#          'Olav Jove',
#          'Weldon Pappas',
#          'Renus Biggus',
#          'Vienna Leyden',
#          'Io Dave',
#          'Schwartz Stromberg']
n = int(input('input number of people: '))
names = []
for i in range(n):
    name = input('input name: ')
    names.append(name)

group = []
for i in range(len(names)):
    s = set()
    group.append(s)
    for n in names:
        if bool(random.getrandbits(3)):
            s.add(n)
    if names[i] in s:
        s.remove(names[i])
    print(s)

for n in names:
    visits = 0
    for s in group:
        if n in s:
            visits += 1
    if visits == len(names)-1:
        print('любит ходить ко всем подряд: ', n)
