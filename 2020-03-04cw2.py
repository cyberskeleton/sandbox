class Iterator():
    def __init__(self, list):
        self._list = list
        self.len = len(list)
        self._pos = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._pos == self.len:
            raise StopIteration
        if int(self._list[self._pos]) % 2 == 0:
            self.len += 1
            return self._list[self._pos - 1]
        else:
            self._pos += 1
            self.__next__()
str = input('input string: ')
list = str.split(' ')
for i in Iterator(list):
    print(i)
