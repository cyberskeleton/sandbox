import collections
class Multiset():

    def __init__(self):
        self.default_dict = collections.defaultdict()

    def add_multiple_input(self):
        self.number_of_el = int(input('input number of elements: '))
        for i in range(self.number_of_el):
            el = int(input(' input an element: '))
            self.add(el)

    def add_input_line(self):
        line = input('enter numbers divided by spaces: ')
        line_split = line.split(' ')
        for i in line_split:
            self.add(i)

    def add(self, elem):
        if elem in self.default_dict:
            self.default_dict[elem] += 1
        else:
            self.default_dict[elem] = 1
        return self.default_dict

    def remove(self, elem):
        print('Unchanged multiset: ', self.default_dict.items())
        if elem in self.default_dict:
            self.default_dict[elem] -= 1
        else:
            print('Element is not in multiset')
        return self.default_dict

    def most_frequent_number(self):
        elem = 0
        max = 0
        for i in self.default_dict.keys():
            if self.default_dict[i] > max:
                elem = i
                max = self.default_dict[i]
        return elem

    def clear(self):
        self.default_dict = collections.defaultdict()
        return self.default_dict

    def is_empty(self):
        if len(self.default_dict) == 0:
            return True
        return False

    def __or__(self, other):
        if isinstance(other, Multiset):
            result = collections.defaultdict()
            # add all items from self
            for key in self.default_dict.keys():
                if key in other.keys() and other.getitem(key) > self.getitem(key):
                    result[key] = other.getitem(key)
                else:
                    result[key] = self.getitem(key)
            # add all items from other
            for key in other.keys() - self.keys():
                result[key] = other.getitem(key)
            return result

    def __and__(self, other):
        if isinstance(other, Multiset):
            result = collections.defaultdict()
            for key in self.keys() - (self.keys() - other.keys()):
                if self.getitem(key) < other.getitem(key):
                    result[key] = self.getitem(key)
                else:
                    result[key] = other.getitem(key)
            return result

    def print(self):
        print('Multiset:', self.default_dict.items())

    def keys(self):
        return self.default_dict.keys()

    def items(self):
        return self.default_dict.items()

    def getitem(self, elem):
        if elem in self.default_dict:
            return self.default_dict[elem]
        else:
            raise NotFoundError

class File():
    def __init__(self):
        self.data = []
    def read_file(self, file1):
        self.file1 = open(file1, 'r')
        self.data1 =self.file1.read()
        return self.data1

    def file_to_multiset(self):
        set1 = Multiset()
        for i in self.data1:
            set1.add(i)
        return set1

class ElementNotFoundError(Exception):
    def __init__(self):
        self._txt="FIle not ..."
    def __str__(self):
        return self._txt

#NotFoundError = NotFoundError()
f1 = File()
f1.read_file('f1.txt')
s1 = f1.file_to_multiset()
# f1.only_nums()
f2 = File()
f2.read_file('f2.txt')
s2 = f2.file_to_multiset()
# f2.only_nums()
try:
    for e in s1.keys():
        s2.getitem(e)
except NotFoundError:
    print('s2 does not have all s1 elements')
print('Union: ', Multiset.__or__(s1, s2).items())
print('Intersection: ', Multiset.__and__(s1, s2).items())
print('')


# are items different
if len(s1.items() - s2.items()) != 0 or len(s2.items() - s1.items()) != 0:
    print('a) numbers or their occurrence rate differ')
else:
    print('a) same numbers appear with the same rate')

# do all s1 elements appear in s2 with same or higher rate
result = False
if len(s1.keys() - s2.keys()) == 0:
    result = True
    for i in s1.keys():
        if s1.getitem(i) > s2.getitem(i):
            result = False
            break
print('b) all s1 elements appear in s2 with same or higher rate:', result)
