n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]

max_block = 0


def move(d, temp_board, i):
    global max_block
    if i >= 5:
        for x in range(n):
            max_block = max(max_block, max(temp_board[x]))
        return

    not_moved = 0
    added = [[False] * n for _ in range(n)]
    board = [[0]*n for _ in range(n)]
    for a in range(n):
        for b in range(n):
            board[a][b] = temp_board[a][b]

    if d == 0: #상
        for y in range(n):
            for x in range(1, n):
                if board[x][y] == 0:
                    not_moved += 1
                    continue
                nx, ny = x + dx[d], y + dy[d]
                if board[nx][ny] == 0:
                    while nx > 0 and board[nx][ny] == 0:
                        nx = nx + dx[d]

                if board[nx][ny] == 0:
                    board[nx][ny] = board[x][y]
                    board[x][y] = 0
                elif not added[nx][ny] and board[nx][ny] == board[x][y]:
                    board[nx][ny] *= 2
                    board[x][y] = 0
                    added[nx][ny] = True
                else:
                    nx = nx - dx[d]
                    if nx != x:
                        board[nx][ny] = board[x][y]
                        board[x][y] = 0
                    else:
                        not_moved += 1

    elif d == 1: #하
        for y in range(n):
            for x in range(n-2, -1, -1):
                if board[x][y] == 0:
                    not_moved += 1
                    continue
                nx, ny = x + dx[d], y + dy[d]
                if board[nx][ny] == 0:
                    while nx < n-1 and board[nx][ny] == 0:
                        nx = nx + dx[d]

                if board[nx][ny] == 0:
                    board[nx][ny] = board[x][y]
                    board[x][y] = 0
                elif not added[nx][ny] and board[nx][ny] == board[x][y]:
                    board[nx][ny] *= 2
                    board[x][y] = 0
                    added[nx][ny] = True
                else:
                    nx = nx - dx[d]
                    if nx != x:
                        board[nx][ny] = board[x][y]
                        board[x][y] = 0
                    else:
                        not_moved += 1

    elif d == 2: #좌
        for x in range(n):
            for y in range(1, n):
                if board[x][y] == 0:
                    not_moved += 1
                    continue
                nx, ny = x + dx[d], y + dy[d]
                if board[nx][ny] == 0:
                    while ny > 0 and board[nx][ny] == 0:
                        ny = ny + dy[d]
                if board[nx][ny] == 0:
                    board[nx][ny] = board[x][y]
                    board[x][y] = 0
                elif not added[nx][ny] and board[nx][ny] == board[x][y]:
                    board[nx][ny] *= 2
                    board[x][y] = 0
                    added[nx][ny] = True
                else:
                    ny = ny - dy[d]
                    if ny != y:
                        board[nx][ny] = board[x][y]
                        board[x][y] = 0
                    else:
                        not_moved += 1

    elif d == 3: #우
        for x in range(n):
            for y in range(n-2, -1, -1):
                if board[x][y] == 0:
                    not_moved += 1
                    continue
                nx, ny = x + dx[d], y + dy[d]
                if board[nx][ny] == 0:
                    while ny < n-1 and board[nx][ny] == 0:
                        ny = ny + dy[d]

                if board[nx][ny] == 0:
                    board[nx][ny] = board[x][y]
                    board[x][y] = 0
                elif not added[nx][ny] and board[nx][ny] == board[x][y]:
                    board[nx][ny] *= 2
                    board[x][y] = 0
                    added[nx][ny] = True
                else:
                    ny = ny - dy[d]
                    if ny != y:
                        board[nx][ny] = board[x][y]
                        board[x][y] = 0
                    else:
                        not_moved += 1

    if not_moved == n * (n-1):
        move(0, board, 5)
    else:
        for direction in range(4):
            move(direction, board, i+1)


for d in range(4):
    move(d, board, 0)
print(max_block)
