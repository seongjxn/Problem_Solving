N = int(input())
board = [list(input()) for _ in range(N)]
count = 0

# board의 인접 지뢰 개수 정수 변환
for i in range(N) :
    for j in range(N) :
        if (board[i][j] != '#') :
            board[i][j] = int(board[i][j])


if board[0][0] == 1 :
    count += 1
    board[1][1] = '*'
else :
    board[1][1] = ' '

if board[0][N - 1] == 1 :
    count += 1
    board[1][N - 2] = '*'
else :
    board[1][N - 2] = ' '
        
if board[N - 1][0] == 1 :
    count += 1
    board[N - 2][1] = '*'
else :
    board[N - 2][1] = ' '

if board[N - 1][N - 1] == 1 :
    count += 1
    board[N - 2][N - 2] = '*'
else :
    board[N - 2][N - 2] = ' '

for i in range(1, N - 1) :
    if (board[1][i] == '#') :
        if (board[1][i - 1] == '*') :
            if (board[0][i - 1] == 2) and (board[1][i - 2] != '*') or (board[0][i - 1] == 3) and (board[1][i - 2] == '*') :
                board[1][i] = '*'
                count += 1
            else :
                board[1][i] = ' '
        elif (board[1][i - 1] == ' ') :
            if (board[0][i - 1] == 1) and (board[1][i - 2] != '*') or (board[0][i - 1] == 2) and (board[1][i - 2] == '*') :
                board[1][i] = '*'
                count += 1
            else :
                board[1][i] = ' '
        else :
            continue

for i in range(1, N - 1) :
    if (board[i][1] == '#') :
        if (board[i - 1][1] == '*') :
            if (board[i - 1][0] == 2) and (board[i - 2][1] != '*') or (board[i - 1][0] == 3) and (board[i - 2][1] == '*') :
                board[i][1] = '*'
                count += 1
            else :
                board[i][1] = ' '
        elif (board[i - 1][1] == ' ') :
            if (board[i - 1][0] == 1) and (board[i - 2][1] != '*') or (board[i - 1][0] == 2) and (board[i - 2][1] == '*') :
                board[i][1] = '*'
                count += 1
            else :
                board[i][1] = ' '
        else :
            continue

for i in range(1, N - 1) :
    if (board[i][N - 2] == '#') :
        if (board[i - 1][N - 2] == '*') :
            if (board[i - 1][N - 1] == 2) and (board[i - 2][N - 2] != '*') or (board[i - 1][N - 1] == 3) and (board[i - 2][N - 2] == '*') :
                board[i][N - 2] = '*'
                count += 1
            else :
                board[i][N - 2] = ' '
        elif (board[i - 1][N - 2] == ' ') :
            if (board[i - 1][N - 1] == 1) and (board[i - 2][N - 2] != '*') or (board[i - 1][N - 1] == 2) and (board[i - 2][N - 2] == '*') :
                board[i][N - 2] = '*'
                count += 1
            else :
                board[i][N - 2] = ' '
        else :
            continue

for i in range(1, N - 1) :
    if (board[N - 2][i] == '#') :
        if (board[N - 2][i - 1] == '*') :
            if (board[N - 1][i - 1] == 2) and (board[N - 2][i - 2] != '*') or (board[N - 1][i - 1] == 3) and (board[N - 2][i - 2] == '*') :
                board[N - 2][i] = '*'
                count += 1
            else :
                board[N - 2][i] = ' '
        elif (board[N - 2][i - 1] == ' ') :
            if (board[N - 1][i - 1] == 1) and (board[N - 2][i - 2] != '*') or (board[N - 1][i - 1] == 2) and (board[N - 2][i - 2] == '*') :
                board[N - 2][i] = '*'
                count += 1
            else :
                board[N - 2][i] = ' '
        else :
            continue

for i in range(2, N - 2) :
    for j in range(2, N - 2) :
        if (board[i][j] == '#') :
            board[i][j] = '*'
            count += 1

print(count)