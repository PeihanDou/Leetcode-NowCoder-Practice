n,m,p,q = list(map(int, input().split(' ')))
board = []
i,j = None, None
score = 0
for row in range(n):
    block = list(input())
    board.append(block)
    if 'S' in block:
        i,j = row, block.index('S')
actions = input()
for action in actions:
    if action == 'S':
        if i+1 >= n or board[i+1][j] == '#':
            i,j = i,j
        elif board[i+1][j] == 'O':
            score += p
            board[i+1][j] = '+'
            i,j = i+1,j
        elif board[i+1][j] == 'X':
            score -= q
            board[i+1][j] = '+'
            i,j = i+1,j
        elif board[i+1][j] == '+':
            i,j = i+1,j
    if action == 'W':
        if i-1 < 0 or board[i-1][j] == '#':
            i,j = i,j
        elif board[i-1][j] == 'O':
            score += p
            board[i-1][j] = '+'
            i,j = i-1,j
        elif board[i-1][j] == 'X':
            score -= q
            board[i-1][j] = '+'
            i,j = i-1,j
        elif board[i-1][j] == '+':
            i,j = i-1,j
    if action == 'A':
        if j-1 < 0 or board[i][j-1] == '#':
            i,j = i,j
        elif board[i][j-1] == 'O':
            score += p
            board[i][j-1] = '+'
            i,j = i, j-1
        elif board[i][j-1] == 'X':
            score -= q
            board[i][j-1] = '+'
            i,j = i,j-1
        elif board[i][j-1] == '+':
            i,j = i,j-1
    if action == 'D':
        if j+1 >= m or board[i][j+1] == '#':
            i,j = i,j
        elif board[i][j+1] == 'O':
            score += p
            board[i][j+1] = '+'
            i,j = i, j+1
        elif board[i][j+1] == 'X':
            score -= q
            board[i][j+1] = '+'
            i,j = i,j+1
        elif board[i][j+1] == '+':
            i,j = i,j+1
print(score)