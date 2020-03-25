def generator(file1):
    f = open(file1, 'r')
    for line in f:
        if len(line) > 10:
            yield line
for i in generator('filegen.txt'):
    print(i)
