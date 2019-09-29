def kingmove():
    ask = input("Position : ")
    board = [['-'] * 8 for i in range(8)]
    row,column = ['a','b','c','d','e','f','g','h'],[8,7,6,5,4,3,2,1]

    while True :
        if len(ask) == 2:
            X = column.index(int(ask[1]))
            Y = row.index(str(ask[0].lower()))
            kingpossiblemove = [[X + 1, Y],
                                [X + 1, Y + 1],
                                [X, Y + 1],
                                [X - 1, Y + 1],
                                [X - 1, Y],
                                [X - 1, Y - 1],
                                [X, Y - 1],
                                [X + 1, Y - 1]]
            try:
                board[X][Y] = 'O'
                for i, c in kingpossiblemove:
                    try:
                        if i >= 0 and c >= 0:
                            board[i][c] = '+'
                    except:
                        pass
                for i in range(len(board)):
                    print(''.join(board[i]))
            except:
                pass
            break
        else:
            print("You need to input a position E.g b1")
            break
kingmove()

