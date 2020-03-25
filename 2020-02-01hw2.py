def copy_file(source, target):
    target.write(source.read())
    source.close()
    target.close()

copy_file(open('tokill/f2.txt', 'r+'), open('h.txt', 'w'))
copy_file(open('tokill/f1.txt', 'r+'), open('tokill/f2.txt', 'w'))
copy_file(open('h.txt', 'r+'), open('tokill/f1.txt', 'w'))
