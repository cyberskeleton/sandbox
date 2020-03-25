def permutation(string):
    if len(string) == 1:
        return [string]
    permutationlist = []   # resulting list
    for a in string:
        remainingelements = [x for x in string if x != a]
        sublistpermutation = permutation(remainingelements)   # permutations of sublist
        for b in sublistpermutation:
            permutationlist.append([a] + b)
    return permutationlist


n = int(input())
joiner = ' '
arrange = []
for i in range(1, n + 1):
    arrange.append(i)
lists = permutation(arrange)
print(lists)
for list in lists:
    #iter = joiner.join(str(list))
    iter0 = str(list).replace(',', ' ')
    iter1 = iter0.replace('[', '')
    iter = iter1.replace(']', '')
    print(iter)
