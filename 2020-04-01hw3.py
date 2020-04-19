# 19.16 Описати метаклас PoolMeta, який дозволяє відслідковувати, що
# кількість об’єктів певного класу не перевищує n. При спробі створити (n+1)
# об’єкт, у якості результату повертається перший створений об’єкт, далі –
# другий тощо.
# Використати цей метаклас для розв’язання задачі. Деякий клас дозволяє
# зберігати та обробляти інформацію про інцидент (назва, тип, опис, час
# виникнення, заходи тощо). Одночасно на екрані не може розміщуватись
# більш, ніж 9 інцидентів. Забезпечити одночасне знаходження у пам’яті тільки
# 9 інцидентів (в той же час інформація про всі інциденти повинна зберігатись у
# текстовому файлі).
from datetime import datetime

class Utils():
    def __init__(self, filename):
        self.filename = filename

    def save(self, name, type, description, time):
        f = open(self.filename, 'a')
        f.write(name + ", " + type + ", " + description + ", " + time + "\n")
        f.close()

    def clean(self):
        f = open(self.filename, 'w')
        f.close()

class FactoryPoolMeta(type):
    load_list = []
    instances = []
    n_allowed = 1
    def __init__(cls, n, filename):
        super(FactoryPoolMeta, cls).__init__(n, filename)
        cls.n_allowed = n  # Number of instances allowed
        cls.filename = filename
        cls.f = open(cls.filename, 'r')
        load_list = cls.f.read().split('\n')
        cls.f.close()
        for idx in range(n):
            event = load_list[idx].split(', ')
            new_event = Events()
            setattr(new_event, "name", event[0])
            setattr(new_event, "type", event[1])
            setattr(new_event, "description", event[2])
            setattr(new_event, "time", event[3])
            instances.append(new_event)
            new_event.print()

    def __new__(cls, *args, **kwargs):
        idx = len(cls.load_list) % cls.n_allowed
        print(idx)
        return cls.instances[idx]

class Events(metaclass=FactoryPoolMeta):
    def __init__(self, n, filename):
        super(FactoryPoolMeta, self.__class__).__init__(n, filename)
        self.name = None
        self.type = None
        self.description = None
        self.time = None

    def print(self):
        print(str(self.name) + ", " +
              str(self.type) + ", " +
              str(self.description) + ", " +
              str(self.time) + "\n")

myfile = 'events.txt'
# util = Utils(myfile)
# util.clean()
# for i in range(10):
#     util.save('name' + str(i), 'type' + str(i), 'description' + str(i), datetime.now().strftime("%m/%d/%Y_%H:%M:%S"))

FactoryPoolMeta(9, myfile)
for i in range(0, 10):
    event = Events()
    event.print()
