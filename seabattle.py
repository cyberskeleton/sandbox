def setboard():
    board = []
    count = 1
    numrow = ' a ' ' b ' ' c ' ' d ' ' e ' ' f ' ' g ' ' h ' ' i ' ' j '
    board.append(numrow)
    for i in range(10):
        row = count, ' * ' ' * ' ' * ' ' * ' ' * ' ' * ' ' * ' ' * ' ' * ' ' * '.split()
        board.append(row)
        count += 1
    for row in board:
        print(' '.join([str(i) for i in row]))

def placeship(board):
    x = input('input letter: ')
    y = input('input number: ')
    for j in range(1, 10):
        for i in range(1, 11):
            if board[i][0] == x:
                if board[0][j] == y:
                    board[i][j] = 0
                print('hit')
            else:
                print('miss')


def shoot():
    count = 10
    board = setboard()
    x = input('input letter: ')
    y = input('input number: ')
    for i in range(1, count + 1):
        if board[count][i] == x:
            board[i] = 0
            ans = 'hit! '
        else:
            ans = 'miss :('
        print(ans)
