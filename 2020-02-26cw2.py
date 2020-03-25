def find_largest(file):
    try:
        numbers = []
        text = open(file, 'r')
        data = text.read().split(' ')
        data2 = text.read().split('\n')
        for i in data:
            numbers.append(i)
        for j in data2:
            numbers.append(j)
