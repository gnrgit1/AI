# Perfect

def printSolution():
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


def isSafe(row, col):
    # checking current row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False
        
    # checking diagonals on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):

        if board[i][j] == 1:
            return False
    
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True


def solveNQ(col):
    next = False
    # global nextStep
    # def nextStep():
    #     next = True
    
    # print(board) # print the board on gui
    # a = input()
    # while True:
    #     if next == True:
    #         next = False
    #         break

    
    if col>=N:
        return True
    
    for i in range(N):
        if isSafe(i, col):

            # print("   |   ")
            # print("   |   ")
            # print("   V   ")
            # printSolution()
            board[i][col] = 1

            if solveNQ(col+1) == True:
                return True
            
            board[i][col] = 0
    
    return False


if __name__ == "__main__":
    global N
    N = int(input("Enter the number of queens: "))

    # global steps
    # steps = []

    global board
    board = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(0)
        board.append(row)
    
    if solveNQ(0) == False:
        print("Solution doesn't exist")

    # print("   |   ")
    # print("   |   ")
    # print("   V   ")
    printSolution()

    # for step in steps:
    #     print(step)
