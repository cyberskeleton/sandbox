import collections
import random

class EmptyQueError(Exception):
    def __str__(self):
        return "The queue is already empty"

class Line():
    def __init__(self, serve_time, add_regular_time, add_benefit_time, run_away_time, total_test_time):
        self.t1_max = serve_time
        self.t2_max = add_regular_time
        self.t3_max = add_benefit_time
        self.t4_max = run_away_time
        self.T = total_test_time
        self.line_deque = collections.deque()
        self.t1_serve = 0
        self.t2_add_regular = 0
        self.t3_add_benefit = 0
        self.t4_remove_last = 0

    def input(self):
        self.t1_max = int(input('input max time a client is served: '))
        self.t2_max = int(input('input max time a regular client is added: '))
        self.t3_max = int(input('input max time a client with benefits is added: '))
        self.t4_max = int(input('input max time to the last client run away: '))
        self.T = int(input('input TOTAL test running time: '))

    def run(self):
        for i in range(self.T, 0, -1):
            try:
                if self.t4_remove_last <= 0:
                    self.t4_remove_last = self.random_time(self.t4_max)
                    self.__remove_last__()
                if self.t1_serve <= 0:
                    self.t1_serve = self.random_time(self.t1_max)
                    self.__serve_client__()
            except EmptyQueError as e:
                print(e)
            if self.t3_add_benefit <= 0:
                self.t3_add_benefit = self.random_time(self.t3_max)
                self.__append_benefit__()
            if self.t2_add_regular <= 0:
                self.t2_add_regular = self.random_time(self.t2_max)
                self.__append_client__()
            self.__decrease_timers__()

    def __decrease_timers__(self):
        self.t1_serve -= 1
        self.t2_add_regular -= 1
        self.t3_add_benefit -= 1
        self.t4_remove_last -= 1

    def __remove_last__(self):
        if len(self.line_deque) == 0:
            raise EmptyQueError
        self.line_deque.pop()
        print('- 1 ========> last client has run away, in queue: ', len(self.line_deque))

    def __serve_client__(self):
        if len(self.line_deque) == 0:
            raise EmptyQueError
        c = self.line_deque.popleft()
        print('- 1 ', c, 'client served, in queue: ', len(self.line_deque))

    def __append_benefit__(self):
        self.line_deque.appendleft('__benefits__')
        print('+ 1 client with __benefits__ added, in queue: ', len(self.line_deque))

    def __append_client__(self):
        self.line_deque.append('regular')
        print('+ 1 regular client added, in queue: ', len(self.line_deque))

    def random_time(self, a):
        return random.randint(1, a)

qu = Line(10, 10, 100, 9, 50)
# qu.input()
qu.run()
