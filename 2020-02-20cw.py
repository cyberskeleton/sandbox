inj = []
test = []
kadr = []
class Employee:
    def __init__(self):
        self.name = None
        self.start_date = None
        self.education = None
        self.for_one_day = None
    def input(self, quantiti):
        for i in range(quantiti):
            self.name = input('input name: ')
            self.start_date = input('input start date: ')
            self.d = self.start_date.split()
            self.education = input('education: ')
            self.for_one_day = int(input('input wage for a day: '))
            if self.education == 'inj':
                inj.append(self.name)
            if self.education == 'test':
                test.append(self.name)
            if self.education == 'kadr':
                kadr.append(self.name)
    def calculate_salary(self, ed):
        S = 0
        ed = self.education
        if ed == 'kadr':
            S = self.for_one_day*(1 + 0.1*(self.time_in_company()/3))
        if ed == 'inj':
            G = int(input('input qualification; '))
            S = G*self.for_one_day*(1+self.time_in_company()/10)
        if ed == 'test':
            S = self.for_one_day*(1+self.time_in_company()/5)
        return S

    def time_in_company(self):
        today_year = 2020
        start_year = int(self.d[0])
        age = today_year - start_year
        return age
class Kadry(Employee):
    def __init__(self):
        Employee.__init__(self)
    def calculate_salary(self, ed):
        Employee.calculate_salary(self, ed)
e = Employee()
e.input(1)
print(e.time_in_company())
k = Kadry()
for i in kadr:
    print(k.calculate_salary('kadr'))
print(inj)
print(test)
print(kadr)
