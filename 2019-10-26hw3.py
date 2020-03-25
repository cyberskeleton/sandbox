s = input('s= ')
specials = ('!', '"', '#', '$', '%', '&', '‘', '(', ')', '*', '+')
isAlphaLow = False
isAlphaUp = False
isNum = False
isSpecial = False
isLong = False
count = 0
for i in s:
    if isAlphaLow and isAlphaUp and isNum and isSpecial and isLong:
        break
    if i.isalpha():
        if not isAlphaLow and i.lower():
            isAlphaLow = True
        if not isAlphaUp and i.isupper():
            isAlphaUp = True
    if not isNum and i.isdigit():
        isNum = True
    if not isSpecial:
        for j in specials:
            if j == i:
                isSpecial = True
    count += 1
    if not isLong and count >= 8:
        isLong = True
print("isAlphaLow:", isAlphaLow, " isAlphaUp:", isAlphaUp, " isNum:", isNum, " isSpecial", isSpecial, " isLong:", isLong)
print("Password quality: ", isAlphaLow + isAlphaUp + isNum + isSpecial + isLong)
