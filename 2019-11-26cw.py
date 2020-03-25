n = int(input('number of rows: '))
m = int(input('number of columns: '))
matrix = []
for i in range(n):
    row = input('input row: ')
    matrix.append(row)
print(matrix)
amount = 0
for i in range (0,m):
    if i % m == 1:
        el = matrix[i]
        rightel = matrix[(i + 1)-m]
        lowel = matrix[(i + m)-n]
        upel = matrix[(i + n)-m]
        if rightel == '1':
            if lowel == '1':
                if upel == '1':
                    el = '2'
print(matrix)
    #elif i % m == 0:
      #  el = matrix[i]
       # rightel = matrix[i + m]
       # lowel = 0
    #if t==1 and k==1:
     #   amount = amount+1
       # if rightel == '1' and lowel == '1':
           # amount += 1
    #elif t==1 and k != 1:
     #   amount =
