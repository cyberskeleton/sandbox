# 18.2 Описати класи МузичнийТвір, Звукозапис та МузичнийЗапис. Клас
# МузичнийЗапис є нащадком класів МузичнийТвір та Звукозапис.
# Клас МузичнийТвір має поля «назва твору», «рік створення», «автор»,
# «жанр» та методи створення, введення та виведення музичного твору.
# Клас Звукозапис має поля «частота», «стандарт запису» та «тривалість» та
# методи створення, введення та виведення.
# Клас МузичнийЗапис має власні поля «носій», «розташування» та методи
# створення, введення, виведення усіх характеристик музичного запису.
# З використанням цих класів скласти програму побудови списку із загального
# списку музичних записів списку відтворення (плейлисту). Плейлист може
# бути побудований за жанром, за автором або у випадковому порядку. Може
# бути також вказана кількість творів або тривалість плейлисту.

class MusicPiece:
    def __init__(self):
        self.title = None
        self.year = None
        self.author = None
        self.genre = None

    

    def input(self, title, year, author, genre, *attribute_names):
        self.title = title #input('input the name of the piece: ')
        self.year = year #int(input('input the year of creation: '))
        self.author = author #input('input author: ')
        self.genre = genre #input('input genre: ')

    def print(self):
        print(' title: ', self.title,
              ' by ', self.author,
              ' genre: ', self.genre,
              ' written in ', self.year)

class SoundRecording:
    def __init__(self):
        self.frequency = None
        self.standard = None
        self.duration = None

    def input(self, frequency, standard, duration, *attribute_names):
        self.frequency = frequency #int(input('input frequency: '))
        self.standard = standard #input('input recording standard: ')
        self.duration = duration #float(input('input duration: '))

    def print(self):
        print(' frequency: ', self.frequency,
              ' standard: ', self.standard,
              ' duration: ', self.duration)

class MusicRecording(MusicPiece, SoundRecording):
    def __init__(self):
        MusicPiece.__init__(self)
        SoundRecording.__init__(self)
        self.carrier = None
        self.location = None

    def input(self, title, year, author, genre, frequency, standard, duration, carrier, location):
        MusicPiece.input(self, title, year, author, genre)
        SoundRecording.input(self, frequency, standard, duration)
        self.carrier = carrier #input('input carrier: ')
        self.location = location #input('input location: ')

    def print(self):
        print(MusicPiece.print(self),
              SoundRecording.print(self),
              ' carrier: ', self.carrier,
              ' location: ', self.location)

m = MusicPiece()
m.input()
m.print()
s = SoundRecording()
s.input()
s.print()
