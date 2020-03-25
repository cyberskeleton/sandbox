def copy_file(source, target):
    target.write(source.read())
    source.close()
    target.close()

copy_file(open('f2.txt', 'r+'), open('h.txt', 'w'))
copy_file(open('f1.txt', 'r+'), open('f2.txt', 'w'))
copy_file(open('h.txt', 'r+'), open('f1.txt', 'w'))
