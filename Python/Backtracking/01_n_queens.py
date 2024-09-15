def isQueenSafe(board, row, col, n):
    for i in range(row - 1, -1, -1):
        if board[i][col] == 1:
            return False
        
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    i = row - 1
    j = col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def nQueensPos(board, n, row, pos):
    
    if row == n:
        return [pos]

    result = []
    for j in range(n):
        if isQueenSafe(board, row, j, n):
            board[row][j] = 1
            result.extend(nQueensPos(board, n, row + 1, pos+[(row, j)]))
            board[row][j] = 0

    return result

n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]
pos = []
for solution in nQueensPos(board, n, 0, pos):
    print(solution)