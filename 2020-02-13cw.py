from collections import Counter
seq = input('input sequence: ')
specials= ['+', '-', '*', '/']
def count_numbers(str):
    for i in str:
        if i in specials:
            str = str.replace(i, '')
    ans = 0
    count = Counter(str)
    print(count)
    for i in count:
        c = count[i]
        ans += c
    return ans
def count_specials(str):
    for i in str:
        if i not in specials:
            str = str.replace(i, '')
    ans = 0
    count = Counter(str)
    print(count)
    for i in count:
        c = count[i]
        ans += c
    return ans
print('numbers: ', count_numbers(seq))
print('specials: ', count_specials(seq))
