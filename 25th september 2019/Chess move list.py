board = [['-'] * 8 for i in range(8)]
row, column = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], [8, 7, 6, 5, 4, 3, 2, 1]

def kingmove():
    ask = input("Position : ")
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

def knightmove():
    ask = input("Position : ")
    while True :
        if len(ask) == 2:
            X = column.index(int(ask[1]))
            Y = row.index(str(ask[0].lower()))
            knightpossiblemove = [[X + 2, Y + 1],
                                [X + 2, Y - 1],
                                [X + 1, Y + 2],
                                [X + 1, Y + 2],
                                [X - 2, Y - 1],
                                [X - 2, Y + 1],
                                [X - 1, Y + 2],
                                [X - 1, Y - 2]]
            try:
                board[X][Y] = 'O'
                for i, c in knightpossiblemove:
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

def pawnmove():
    ask = input("Position : ")
    while True :
        if len(ask) == 2:
            X = column.index(int(ask[1]))
            Y = row.index(str(ask[0].lower()))
            pawnpossiblemove = [[X + 1, Y ],
                                [X + 1, Y ],
                                [X + 1, Y ],
                                [X + 1, Y ],
                                [X - 1, Y],
                                [X - 1, Y],
                                [X - 1, Y],
                                [X - 1, Y]]
            try:
                board[X][Y] = 'O'
                for i, c in pawnpossiblemove:
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

def rookmove():
    ask = input("Position : ")
    while True :
        if len(ask) == 2:
            X = column.index(int(ask[1]))
            Y = row.index(str(ask[0].lower()))
            rookpossiblemove = [[X + 1, Y],
                                [X + 2, Y],
                                [X + 3, Y],
                                [X + 4, Y],
                                [X + 5, Y],
                                [X + 6, Y],
                                [X + 7, Y],
                                [X + 8, Y],
                                [X - 1, Y],
                                [X - 2, Y],
                                [X - 3, Y],
                                [X - 4, Y],
                                [X - 5, Y],
                                [X - 6, Y],
                                [X - 7, Y],
                                [X - 8, Y],
                                [X, Y + 1],
                                [X, Y + 2],
                                [X, Y + 3],
                                [X, Y + 4],
                                [X, Y + 5],
                                [X, Y + 6],
                                [X, Y + 7],
                                [X, Y + 8],
                                [X, Y - 1],
                                [X, Y - 2],
                                [X, Y - 3],
                                [X, Y - 4],
                                [X, Y - 5],
                                [X, Y - 6],
                                [X, Y - 7],
                                [X, Y - 8]]
            try:
                board[X][Y] = 'O'
                for i, c in rookpossiblemove:
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
def bishopmove():
    ask = input("Position : ")
    while True :
        if len(ask) == 2:
            X = column.index(int(ask[1]))
            Y = row.index(str(ask[0].lower()))
            bishoppossiblemove =[[X + 1, Y-1],
                                [X + 2, Y-2],
                                [X + 3, Y-3],
                                [X + 4, Y-4],
                                [X + 5, Y-5],
                                [X + 6, Y-6],
                                [X + 7, Y-7],
                                [X + 8, Y-8],
                                [X - 1, Y+1],
                                [X - 2, Y+2],
                                [X - 3, Y+3],
                                [X - 4, Y+4],
                                [X - 5, Y+5],
                                [X - 6, Y+6],
                                [X - 7, Y+7],
                                [X - 8, Y+8],
                                [X + 1, Y+1],
                                [X + 2, Y+2],
                                [X + 3, Y+3],
                                [X + 4, Y+4],
                                [X + 5, Y+5],
                                [X + 6, Y+6],
                                [X + 7, Y+7],
                                [X + 8, Y+8],
                                [X - 1, Y-1],
                                [X - 2, Y-2],
                                [X - 3, Y-3],
                                [X - 4, Y-4],
                                [X - 5, Y-5],
                                [X - 6, Y-6],
                                [X - 7, Y-7],
                                [X - 8, Y-8]]
            try:
                board[X][Y] = 'O'
                for i, c in bishoppossiblemove:
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
def queenmove():
    ask = input("Position : ")
    while True :
        if len(ask) == 2:
            X = column.index(int(ask[1]))
            Y = row.index(str(ask[0].lower()))
            queenpossiblemove =[[X + 1, Y-1],
                                [X + 2, Y-2],
                                [X + 3, Y-3],
                                [X + 4, Y-4],
                                [X + 5, Y-5],
                                [X + 6, Y-6],
                                [X + 7, Y-7],
                                [X + 8, Y-8],
                                [X - 1, Y+1],
                                [X - 2, Y+2],
                                [X - 3, Y+3],
                                [X - 4, Y+4],
                                [X - 5, Y+5],
                                [X - 6, Y+6],
                                [X - 7, Y+7],
                                [X - 8, Y+8],
                                [X + 1, Y+1],
                                [X + 2, Y+2],
                                [X + 3, Y+3],
                                [X + 4, Y+4],
                                [X + 5, Y+5],
                                [X + 6, Y+6],
                                [X + 7, Y+7],
                                [X + 8, Y+8],
                                [X - 1, Y-1],
                                [X - 2, Y-2],
                                [X - 3, Y-3],
                                [X - 4, Y-4],
                                [X - 5, Y-5],
                                [X - 6, Y-6],
                                [X - 7, Y-7],
                                [X - 8, Y-8],
                                [X + 1, Y],
                                [X + 1, Y + 1],
                                [X, Y + 1],
                                [X - 1, Y + 1],
                                [X - 1, Y],
                                [X - 1, Y - 1],
                                [X, Y - 1],
                                [X + 1, Y - 1]]
            try:
                board[X][Y] = 'O'
                for i, c in queenpossiblemove:
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
def menu():
    steps = ("1. King move list \n""2. Knight move list\n""3. Pawn move list\n""4. Rook move list\n""5. Bishop move list\n""6. Queen move list\n""7. Exit\n")
    choice = input(steps)
    return int(choice)
while True:
    try:
        choice = menu()
        if choice == 1:
            kingmove()
            del board
            board = [['-'] * 8 for i in range(8)]
        elif choice == 2:
            knightmove()
            del board
            board = [['-'] * 8 for i in range(8)]
        elif choice == 3:
            pawnmove()
            del board
            board = [['-'] * 8 for i in range(8)]
        elif choice == 4:
            rookmove()
            del board
            board = [['-'] * 8 for i in range(8)]
        elif choice == 5:
            bishopmove()
            del board
            board = [['-'] * 8 for i in range(8)]
        elif choice == 6:
            queenmove()
            del board
            board = [['-'] * 8 for i in range(8)]
        elif choice == 7:
            break

    except ValueError:
        continue