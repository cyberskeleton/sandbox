text = input('input text: ')
symbols = {'.', ',', '!', '(', ')', '?', ':', ';'}
consonants = {'б', 'Б','в', '','г','', 'д', '', 'ж', '','з', '', 'г', '', 'ґ', '', 'п', '', 'р', '', 'щ', '', 'ш', '', 'ч', '', 'к', '','л', '', 'м', '','н', '', 'с', '', 'т', '', 'ф', '', 'х', 'ц', 'й'}
vowels = {'а', 'я', 'о', 'у', 'ю', 'е', 'є', 'и', 'і', 'ї'}
for i in text:
    if i in symbols:
        text = text.replace(i, '')
print(text)
words = text.split()
print(words)
for word in words:
    word = str(word)
    for i in range(0, len(word)):
        if word[i] in consonants:
            if word[i+1] in vowels:
                if i + 2 != len(word):
                    print(word[i], word[i+1])
                else:
                    if i+2 <= len(word):
                        if word[i+2] in consonants:
                            print(word[i], word[i+1], word[i + 2])
                        else:
                            print(word[i], word[i+1])
                            print(word[i+2])
                    else:
                        break
                        