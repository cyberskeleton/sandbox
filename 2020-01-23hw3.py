text = input('input text: ')
vowels = {'а', 'я', 'о', 'у', 'ю', 'е', 'є', 'и', 'і', 'ї'}
text = text.replace('.', '')
letters = set()
words = text.split()
for word in words:
    for i in word:
        if i in vowels:
            letters.add(i)
print(letters)
finalvow = set()
for i in letters:
    result = True
    for w in words:
        result = i in w
        if not result:
            break
    if result:
        finalvow.add(i)
print(sorted(finalvow))
