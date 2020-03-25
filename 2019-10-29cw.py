s = input()
kp = s.split()
if len(kp) == 2:
    k = int(kp[0])
    p = int(kp[1])
    if k > 0 and k <= 10**8 and p > 0 and p <= 10**8:
        first = 'a'
        second = 'bc'
        third = ''
        for i in range(3, k + 1):
            third = first + second
            first = second
            second = third
        print(third[p - 1])
    else:
        print('no solution')
else:
    print('wrong input')
