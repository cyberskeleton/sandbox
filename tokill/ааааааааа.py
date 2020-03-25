text = input('input text: ')
text = text.lower()
print(text)
symbols = {'.', ',', '!', '(', ')', '?', ':', ';'}
consonants = {'б','в', '','г','', 'д', '', 'ж', '','з', '', 'г', '', 'ґ', '', 'п', '', 'р', '', 'щ', '', 'ш', '', 'ч', '', 'к', '','л', '', 'м', '','н', '', 'с', '', 'т', '', 'ф', '', 'х', 'ц', 'й'}
vowels = {'а', 'я', 'о', 'у', 'ю', 'е', 'є', 'и', 'і', 'ї'}
for i in text:
    if i in symbols:
        text = text.replace(i, '')
print(text)
words = text.split()
print(words)
endstr = 100
for word in words:
    word2 = str(word)
    for i in range(0, len(word2)):
        if word2[i] in consonants:
            if word2[i + 1] in vowels:
                if i + 2 != len(word2):
                    print(word2[i],word2[i + 1])
                else:
                    #f i + 2 <= len(word):
                    if i > len(word2):
                        i = i - len(word2)
                        if word2[i + 2] in consonants:
                            print(word2[i],word2[i + 1],word2[i + 2])
                        else:
                            print(word2[i],word2[i + 1])
                            print(word2[i + 2])
        else:
            if i == 0:
                if word2[i] in vowels:
                    if word2[i+1] in consonants:
                        print(word2[i])
                        print(word2[i+1])
                else:
                    if word2[i+1] in consonants and word2[i +2] in vowels:
                        print(word2[i], word2[i+1], word2[i+2])
