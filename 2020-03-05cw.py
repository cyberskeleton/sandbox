class Text():
    def __init__(self, filename):
        self.list = []
        self.file = open(filename, 'r')
        self.data = self.file.read()
    def word_append(self):
        a = self.data.lower()
        self.list = a.split()
        return self.list

    def __len__(self):
        length = len(self.list)
        return length

    def remove_specials(self):
        self.cleaned = []
        specials = [',', '.', ':', ';', '!', '?', '-']
        for word in self.list:
            print(word)
            for i in word:
                print(i)
                if i in specials:
                    i = ' '
                    print(word)
                    self.cleaned.append(word)
        return self.cleaned

    def __add__(self, filename):
        file2 = open(filename, 'r')
        data2 = file2.read()
        new_data = self.data + data2
        return new_data

class Iter(Text):
    def __iter__(self):
        return self

    def find(self, str):
        for word in self.list:
            print(word)
            for i in str.split():
                if i ==  word.split[0]:
                    return word
text = Text('document.txt')
print(text.word_append())
print(text.__len__())
#print(text.remove_specials())
print('concatenation: ', text.__add__('realnum.txt'))
i = Iter('document.txt')
print(i.find('в'))
