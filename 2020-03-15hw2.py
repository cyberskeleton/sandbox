# 17.14
# Нехай результатом функції f є список деяких елементів. Побудувати
# декоратор, який модифікує цей список так, щоб він не містив повторів.
# Перевірити роботу декоратора для функції, яка повертає список слів, що
# містяться у текстовому файлі.

def filter_duplicates(func):
    def filter_list(*args, **kwargs):
        my_list = func(*args, **kwargs)
        return list(dict.fromkeys(my_list))
    return filter_list

@filter_duplicates
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

print(get_list('tokill/text.txt'))
