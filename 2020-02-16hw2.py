import collections
import random
class Line():
    def __init__(self, t1, t2, T):
        self.t1 = t1
        self.t2 = t2
        self.T = T
        self.line_deque = collections.deque()

    def input(self):
        self.T = int(input('input total running time: '))
        self.t1 = int(input('input max time of client being served: '))
        self.t2 = int(input('input max time of client being added: '))

    def run(self):
        time_to_serve = 0
        time_to_add = 0
        for i in range(self.T, 0, -1):
            if len(self.line_deque) > 0 and time_to_serve <= 0:
                time_to_serve = self.random_time(self.t1)
                self.line_deque.pop()
                print('- 1 served, in queue: ', len(self.line_deque))
            if time_to_add <= 0:
                time_to_add = self.random_time(self.t2)
                self.line_deque.append('a')
                print('+ 1  added, in queue: ', len(self.line_deque))
            time_to_serve -= 1
            time_to_add -= 1

    def random_time(self, a):
        return random.randint(1, a)
qu = Line(1, 1, 1)
qu.input()
qu.run()
