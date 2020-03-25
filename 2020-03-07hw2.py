class Iterator():
    def __init__(self, list):
        self.list = list
        self.pos = 0
        self.ukr = ['а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї',
           'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',	'х',
           'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я']

    def __iter__(self):
        return self

    def __next__(self):
        if self.pos == len(self.list):
            raise StopIteration
        symbol = self.list[self.pos]
        self.pos += 1
        if symbol in self.ukr:
            return symbol

str = input('input your string: ')
str_list = str.lower().split(' ')
it = Iterator(str_list)
try:
    while True:
        next = it.__next__()
        if next:
            print(next)
except:
    pass
