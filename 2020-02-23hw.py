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

    def getitem(self, key):
        return self.default_dict[key]

# add
print('n: ')
n = Multiset()
n.add_multiple_input()
print('2 is removed: ', n.remove(2).items())
print('Cleared Multiset: ', n.clear().items())
print('The Multiset is empty: ', n.is_empty())
print('s1:')
s1 = Multiset()
s1.add_input_line()
print('s2:')
s2 = Multiset()
s2.add_input_line()
print('Union: ', Multiset.__or__(s1, s2).items())
print('Intersection: ', Multiset.__and__(s1, s2).items())
print('')

# find most common
print('a) most common element in s1:', s1.most_frequent_number())

# are items different
if len(s1.items() - s2.items()) != 0 or len(s2.items() - s1.items()) != 0:
    print('b) numbers or their occurrence rate differ')
else:
    print('b) same numbers appear with the same rate')

# do all s1 elements appear in s2 with same or higher rate
result = False
if len(s1.keys() - s2.keys()) == 0:
    result = True
    for i in s1.keys():
        if s1.getitem(i) > s2.getitem(i):
            result = False
            break
print('c) all s1 elements appear in s2 with same or higher rate:', result)
