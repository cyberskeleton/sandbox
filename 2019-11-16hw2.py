n = int(input())
ulist = []
phone = input()
list1 = phone.split()
for x in list1:
    if x not in ulist:
        ulist.append(x)
print(len(ulist))
