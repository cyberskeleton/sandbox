def pascal(n):
    if n == 1:
        return [[1]]
    elif n == 0:
        return []
    else:
        newrow = [1]
        result = pascal(n - 1)
        lastrow = result[-1]
        for i in range(len(lastrow)-1):
            newrow.append(lastrow[i] + lastrow[i + 1])
        newrow += [1]
        result.append(newrow)
    return result


rows = int(input('input height: '))
for i in pascal(rows):
    print(i)
