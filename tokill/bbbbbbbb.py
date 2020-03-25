text = input('input text: ')
text = text.lower()
print(text)
symbols = {'.', ',', '!', '(', ')', '?', ':', ';'}
consonants = {'б','в', 'г', 'д', 'ж', 'з', 'г', 'ґ', 'п', 'р', 'щ', 'ш', 'ч', 'к', 'л', 'м', 'н', 'с', 'т', 'ф', 'х', 'ц', 'й'}
vowels = {'а', 'я', 'о', 'у', 'ю', 'е', 'є', 'и', 'і', 'ї'}
for i in text:
    if i in symbols:
        text = text.replace(i, '')
print(text)
words = text.split()
print(words)
lastvowel = False
for word in words:
    for i in word:
        for v in vowels:
            isvowel = False
            if i == v and lastvowel:
                isvowel = True
                lastvowel = True
                break
            elif i == v and not lastvowel:
                isvowel =True
                lastvowel = True
                break
            if not isvowel:
                lastvowel = False
