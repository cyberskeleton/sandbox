#hackaton
import random

def dec_add(func):
    def dec(*args, **kwargs):
        list = func(*args, **kwargs)
        brand_new_list = []
        for word in list:
            if not may_be_applied(len(word)):
                brand_new_list.append(word)
            else:
                brand_new_word = word.replace(word[0], str(chr(ord(word[0]) + 66)))
                brand_new_list.append(brand_new_word)
        return brand_new_list
    return dec

def dec_delete(func):
    def do_it(*args, **kwargs):
        list = func(*args, **kwargs)
        brand_new_list = []
        for word in list:
            if not may_be_applied(len(word)):
                brand_new_list.append(word)
            else:
                brand_new_word = word.replace(word[0], '', 1)
                brand_new_list.append(brand_new_word)
        return brand_new_list
    return do_it

def dec_insert(func):
    def pls_do(*args, **kwargs):
        list = func(*args, **kwargs)
        brand_new_list = []
        for word in list:
            if not may_be_applied(len(word)):
                brand_new_list.append(word)
            else:
                i = random.randint(65, 123)
                brand_new_word = word + chr(i)
                brand_new_list.append(brand_new_word)
        return brand_new_list
    return pls_do

def read_lines_from_file():
    f = open('text.txt', 'r')
    data = f.read().splitlines()
    random_line = random.choice(data)
    f.close()
    brand_new_file = open('brand_new.txt', 'w')
    brand_new_file.write(random_line)
    brand_new_file.close()

def may_be_applied(len):
    return random.randint(0, len) <= len//3

@dec_delete
@dec_insert
@dec_add
def get_list(filename):
    listok = []
    specials = [',', '.', ':', ';', '!', '?', '-']
    f = open(filename, 'r')
    for word in f.read().split():
        for i in word:
            if i in specials:
                word = word.replace(i, '')
        listok.append(word)
    f.close()
    return listok

read_lines_from_file()
print(get_list('brand_new.txt'))
# print(list_to_dict(get_list('brand_new.txt')))
