def mnogochlens(n, x):
    mnogochlen = []
    for i in range(0, n+1):
        x1 = (x**3)**i
        mnogochlen.append(x1)
    #print(mnogochlen)
    answer = sum(mnogochlen)
    return answer


n = int(input('input n: '))
x = int(input('input x: '))
print(mnogochlens(n, x))
