time = []
sp = []
n = 0
while n < 1 or n >100:
    n = int(input())
for i in range(0, n):
    s = input()
    sp = s.split()
    time.append((int(sp[0]), int(sp[1]), int(sp[2])))
swapped = True
while swapped:
    swapped = False
    for i in range(n-1):
        if time[i][0] > time[i+1][0]:
            time[i], time[i+1] = time[i+1], time[i]
            swapped = True
        elif time[i][0] == time[i+1][0]:
            if time[i][1] > time[i+1][1]:
                time[i], time[i+1] = time[i+1], time[i]
                swapped = True
            elif time[i][1] == time[i+1][1]:
                if time[i][2] > time[i+1][2]:
                    time[i], time[i+1] = time[i+1], time[i]
                    swapped = True
for i in range(n):
    print(' '.join(str(x) for x in time[i]))
