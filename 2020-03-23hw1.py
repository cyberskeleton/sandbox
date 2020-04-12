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

import random

class MusicPiece:
    def __init__(self, title, year, author, genre, *attribute_names):
        self.title = title
        self.year = year
        self.author = author
        self.genre = genre

    def print(self):
        print(' title: ', self.title,
              ' by ', self.author,
              ' genre: ', self.genre,
              ' written in ', self.year,
              end = " ")

class SoundRecord:
    def __init__(self, frequency, standard, duration, *attribute_names):
        self.frequency = frequency
        self.standard = standard
        self.duration = duration

    def print(self):
        print(' frequency: ', self.frequency,
              ' standard: ', self.standard,
              ' duration: ', self.duration,
              end = " ")

class MusicRecord(MusicPiece, SoundRecord):
    def __init__(self, title, year, author, genre, frequency, standard, duration, carrier, location):
        MusicPiece.__init__(self, title, year, author, genre)
        SoundRecord.__init__(self, frequency, standard, duration)
        self.carrier = carrier
        self.location = location

    def print(self):
        MusicPiece.print(self)
        SoundRecord.print(self)
        print(' carrier: ', self.carrier, ' location: ', self.location)

class Playlist():
    def __init__(self, records):
        self.records = records
        self.pattern = ''

    def create_random(self):
        result = list(self.records)
        random.shuffle(result)
        print("Random Playlist:")
        for i in result:
            i.print()
        return result

    def create_by_author(self, author):
        self.pattern = author
        result = []
        print("Playlist by author: ", author)
        for i in self.records:
            if author in i.author:
                result.append(i)
                i.print()
        return result
    
    def create_by_genre(self, genre):
        self.pattern = genre
        result = []
        print("Playlist by genre: ", genre)
        for i in self.records:
            if genre in i.genre:
                result.append(i)
                i.print()
        return result

records = []
records.append(MusicRecord("Yesterday", 1965, "McCartney", "chamber pop", 44100, "wav", '0:02:03', "CD", "Help!"))
records.append(MusicRecord("Help!", 1965, "Lennon, McCartney", "folk rock", 44100, "wav", '0:02:18', "CD", "Help!"))
records.append(MusicRecord("Day tripper", 1965, "Lennon, McCartney", "pop rock", 44100, "wav", '0:02:50', "CD", "Help!"))
records.append(MusicRecord("Ticket to ride", 1965, "Lennon, McCartney", "folk rock", 44100, "wav", '0:03:10', "CD", "Help!"))

p = Playlist(records)
p.create_by_author("Lennon")
p.create_by_genre("rock")
p.create_random()
