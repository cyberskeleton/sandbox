import pickle
def create_b(filename):
    f = open(filename,'wb')
    n = int(input('quantity: '))
    book = {}
    for i in range(n):
        author = input('input author: ')
        title = input('input title: ')
        year = int(input('input year: '))
        book[title] = (author, year)
    pickle.dump(book,f)
    f.close()

def read_b(filename):
    f = open(filename,'rb')
    book = pickle.load(f)
    f.close()
    return book

def search_by_author_since_year(filename, author, year):
    book = read_b(filename)
    result = []
    for title, author_year in book.items():
        if author_year[0] == author and year <= author_year[1]:
            result.append(title)
    return result

def search_by_title(filename, title):
    book = read_b(filename)
    if title in book:
        return book[title]
    return None

filename = "book"
create_b(filename)
say = search_by_author_since_year(filename, input('input author: '), int(input('input year: ')))
for e in say:
    print('title by author: ', e)
sbt = search_by_title(filename, input('input title: '))
if sbt != None:
    print('author, year: ', sbt)
else:
    print('this book does not exist')
