#assert abs(x) < 1 str(x) + '> 1'
import math
class Logarythm():
    def __init__(self):
        self.x = float(input('input -1 < x < 1: '))
        self.n = int(input('input precision: '))
    def ln(self):
        self.res = 0
        for i in range(1, self.n+1):
            el = (((self.x)**(i))/i)*(-1)**(i+1)
            self.res += el
            print(el)
        return self.res
    def log_error(self):
        try:
            assert abs(self.x) < 1, str(self.x) + '> 1'
        except AssertionError:
            print('abs(x) > 1 ')
log = Logarythm()
print(log.ln())
log.log_error()
#print(math.log(0.4 + 1))
