# 18.11 Описати клас-домішок CompareMixin, який реалізує усі 6 стандартних
# відношень (==, !=, <, >, <=, >=) на базі одного реалізованого відношення < та
# бульових операцій. Для цього треба реалізувати спеціальні методи __eq__,
# __ne__ тощо
# Вагою числового списку назвемо суму модулів його елементів.
# Описати клас зважений список WeightedList, що є нащадком стандартного
# класу list та реалізує відношення < у відповідності з вагою списків.
# Описати клас нащадок цього класу та домішку CompareMixin
# FullOrderWeightedList – зважений список з повним порядком.
# Ввести список зважених списків з повним порядком та перевірити, чи є всі
# вони у сенсі заданого порядку (мають рівну вагу)

class CompareMixin:
  def __eq__(self, other):
    return not(self < other) and not(other < self)

  def __ne__(self, other):
    return (self < other) or (other < self)

  def __lt__(self, other):
    return (self < other)

  def __gt__(self, other):
    return (other < self)

  def __le__(self, other):
    return (self < other) or self.__eq__(other)

  def __ge__(self, other):
    return (other < self) or self.__eq__(other)

class WeightedList(list):
  def weight(self):
    result = 0
    for i in self:
      result += abs(i)
    return result

  def __lt__(self, p2):
    return self.weight() < p2.weight()

class FullOrderWeightedList(list):
  def weight(self):
    result = 0
    for i in self:
      result += abs(i)
    return result

  def __eq__(self, other):
    return not(self.weight() < other.weight()) and not(other.weight() < self.weight())

  def __ne__(self, other):
    return (self.weight() < other.weight()) or (other.weight() < self.weight())

  def __lt__(self, other):
    return (self.weight() < other.weight())

  def __gt__(self, other):
    return (other.weight() < self.weight())

  def __le__(self, other):
    return (self.weight() < other.weight()) or self.__eq__(other)

  def __ge__(self, other):
    return (other.weight() < self.weight()) or self.__eq__(other)

a = FullOrderWeightedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
b = FullOrderWeightedList([i for  i in range(1, 10)])
c = FullOrderWeightedList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
d = FullOrderWeightedList([i for  i in range(1, 11)])
e = FullOrderWeightedList([i for  i in range(1, 12)])
l = FullOrderWeightedList([a, b, c, d, e])

print("Greater or Equal:")
for i in range(1, len(l)):
  print(l[i].__ge__(l[i - 1]), end=' ')
print()

print("Equal:")
for i in range(1, len(l)):
  print(l[i].__eq__(l[i - 1]), end=' ')
print()
