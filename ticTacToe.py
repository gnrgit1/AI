def ConstBoard(board):
    print("Current State Of Board : \n")
    for i in range(0, 9):
        if i > 0 and i % 3 == 0:
            print("\n")
        if board[i] == 0:
            print("- ", end=" ")
        elif board[i] == 1:
            print("O ", end=" ")
        elif board[i] == -1:
            print("X ", end=" ")
    print("\n")


def User1Turn(board):
    while True:
        pos = input("Enter X's position from [1...9]: ")
        pos = int(pos)
        if 1 <= pos <= 9 and board[pos - 1] == 0:
            board[pos - 1] = -1
            break
        else:
            print("Invalid move try again.")


def minimax(board, player):
    x = analyzeboard(board)
    if x != 0:
        return x * player
    pos = -1
    value = -2
    for i in range(0, 9):
        if board[i] == 0:
            board[i] = player
            score = -minimax(board, player * -1)
            if score > value:
                value = score
                pos = i
            board[i] = 0
    if pos == -1:
        return 0
    return value


def CompTurn(board):
    pos = -1
    value = -2
    for i in range(0, 9):
        if board[i] == 0:
            board[i] = 1
            score = -minimax(board, -1)
            board[i] = 0
            if score > value:
                value = score
                pos = i
    board[pos] = 1


def analyzeboard(board):
    cb = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]  # Wc
    for i in range(0, 8):
        if board[cb[i][0]] != 0 and board[cb[i][0]] == board[cb[i][1]] and board[cb[i][0]] == board[cb[i][2]]:
            return board[cb[i][2]]
    return 0


def main():
    print("You will be  playing as X and the Computer will be O.")
    
 
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]


    player = int(input("Enter 1 to play first , 2 to play second : "))
    

    for i in range(0, 9):
        if analyzeboard(board) != 0:
            break
        if (i + player) % 2 == 0:
            CompTurn(board)  
        else:
            ConstBoard(board)
            User1Turn(board)  
    
   
    x = analyzeboard(board)
    ConstBoard(board)
    
    if x == 0:
        print("It's a Draw!")
    elif x == -1:
        print("You Win (X)!")
    elif x == 1:
        print("Computer Wins (O)!")


main()
