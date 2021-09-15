block_list = {
    1:[1, 3, 0, 2],
    2:[3, 0, 1, 2],
    3:[2, 0, 3, 1],
    4:[1, 2, 3, 0],
    5:[1, 0, 3, 2]
}

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move(x, y, d):
    global score
    while True:

        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < n:
            x, y = nx, ny
            if board[nx][ny] == -1 or [nx, ny] == [start_x, start_y]:
                return -1, -1, -1
            elif board[nx][ny] == 0:
                continue
            elif board[nx][ny] <= 5:
                score += 1
                return x, y, block_list[board[nx][ny]][d]
            elif board[nx][ny] <= 10:
                return warmhole[board[nx][ny] + 10][0], warmhole[board[nx][ny] + 10][1], d
            else:
                return warmhole[board[nx][ny]-10][0], warmhole[board[nx][ny]-10][1], d

        else:
            score += 1
            if [x, y] == [start_x, start_y]:
                return -1, -1, -1
            if board[x][y] == 0:
                return x, y, backward(d)
            else:
                if 1 <= board[x][y] <= 5:
                    score += 1
                    return x, y, block_list[board[x][y]][backward(d)]
                elif board[x][y] > 10:
                    return warmhole[board[x][y] - 10][0], warmhole[board[x][y] - 10][1], backward(d)
                else:
                    return warmhole[board[x][y] + 10][0], warmhole[board[x][y] + 10][1], backward(d)


def backward(d):
    if d % 2 == 0:
        return d + 1
    else:
        return d - 1

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    warmhole = {}
    for i in range(n):
        for j in range(n):
            if board[i][j] > 5:
                if board[i][j] in warmhole:
                    warmhole[board[i][j] + 10] = [i, j]
                    board[i][j] += 10
                else:
                    warmhole[board[i][j]] = [i, j]
    answer = 0

    for x in range(n):
        for y in range(n):
            if board[x][y] == 0:
                start_x, start_y = x, y
                for d in range(4):
                    save_d = d
                    score = 0
                    while [x, y] != [-1, -1]:
                        x, y, d = move(x, y, d)
                    x, y, d = start_x, start_y, save_d
                    answer = max(answer, score)

    print('#'+str(test_case),answer)

