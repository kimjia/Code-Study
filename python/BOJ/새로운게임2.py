n, k = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

piece = []
position = [[[] for _ in range(n)] for _ in range(n)]
for i in range(k):
    x, y, d = map(int, input().split())
    piece.append([x-1, y-1, d-1])
    position[x-1][y-1].append(i)

turn = 1
end_flag = False

while turn <= 1000:
    if end_flag:
        break
    for i in range(k):
        x, y, d = piece[i]
        nx, ny = x + dx[d], y + dy[d]
        if nx < 0 or nx > n-1 or ny < 0 or ny > n-1 or board[nx][ny] == 2:  # 범위 밖 또는 파란색 -> 방향전환
            if d % 2 == 0:
                d += 1
            else:
                d -= 1
            nx, ny = x + dx[d], y + dy[d]
            piece[i][2] = d

        if nx < 0 or nx > n-1 or ny < 0 or ny > n-1 or board[nx][ny] == 2:  # 범위를 벗어나거나 또 파란색
            continue

        else:
            temp = []
            p = position[x][y].pop()
            temp.append(p)
            piece[p][0], piece[p][1] = nx, ny
            while p != i:  # 맨 위에있는 말부터 pop 하고 위치 이동
                p = position[x][y].pop()
                piece[p][0], piece[p][1] = nx, ny
                temp.append(p)

            if board[nx][ny] == 0:  # 흰색인 경우 순서뒤집기 (기존에 쌓여있던 순서)
                temp.reverse()

            position[nx][ny].extend(temp)
            if len(position[nx][ny]) >= 4:
                print(turn)
                end_flag = True
                break
    turn += 1

else:
    print(-1)
