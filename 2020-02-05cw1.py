class Auto():
    def __init__(self):
        self.kilometrage = None
        self.palne_na_100km = None
        self.zalyshok_v_baci = None
    def input(self):
        self.kilometrage = float(input('input kilometres: '))
        self.palne_na_100km = float(input('input consumption: '))
        self.zalyshok_v_baci = float(input('input ostatok: '))

    def print(self):
        print(self.kilometrage, self.palne_na_100km, self.zalyshok_v_baci)
    #1
    def zbilsh_palivo(self):
        f = int(input('input f litres: '))
        self.zalyshok_v_baci = self.zalyshok_v_baci + f
        return self.zalyshok_v_baci
    #2
    def show_bak(self):
        print(self.zalyshok_v_baci)
    #3
    def show_kilometrage(self):
        print(self.kilometrage)
    #4
    def show_all(self):
        print(self.kilometrage, self.palne_na_100km, self.zalyshok_v_baci)
    #5
    def new_vytraty(self):
        new = ((self.palne_na_100km/100) * self.kilometrage//1000) + self.palne_na_100km/100
        self.palne_na_100km = new + self.palne_na_100km
        return self.palne_na_100km
    #6
    def go(self):
        self.vidstan = int(input('input distance '))
        if self.zalyshok_v_baci == 0 or self.zalyshok_v_baci < self.palne_na_100km*self.vidstan:
            return 'Not enough fuel'
        self.zalyshok_v_baci = self.zalyshok_v_baci - self.palne_na_100km*self.vidstan
        self.kilometrage = self.kilometrage + self.vidstan
        return self.zalyshok_v_baci, self.kilometrage
avto = Auto()
avto.input()
avto.print()
print(avto.zbilsh_palivo())
print(avto.new_vytraty())
print(avto.go())

class Car(Auto):
    def __init__(self):
        Auto.__init__(self)
