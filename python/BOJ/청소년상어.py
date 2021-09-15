from copy import deepcopy
board = []
shark = [0, 0]
shark_dir = 0
fish = [[0, 0] for _ in range(16)]

for i in range(4):
    data = list(map(int, input().split()))
    board.append([[data[0]-1, data[1]-1], [data[2]-1, data[3]-1], [data[4]-1, data[5]-1], [data[6]-1, data[7]-1]])
    for j in range(4):
        fish[data[j*2]-1] = [i, j]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

answer = 0


def dfs(x, y, result):
    global answer, shark, shark_dir, board, fish
    if x < 0 or x >= 4 or y < 0 or y >= 4 or board[x][y] == [-1, -1]:
        answer = max(answer, result)
        return

    # eat
    a, b = board[x][y]
    shark = [x, y]
    shark_dir = b
    board[x][y] = [-1, -1]  # 물고기가 먹힌 후에는 -1, -1
    fish[a] = [-1, -1]

    board = move(board)

    shark_save = list(shark)
    shark_dir_save = shark_dir
    board_save = deepcopy(board)
    fish_save = deepcopy(fish)

    for p in range(1, 4):
        nx = x + dx[shark_dir] * p
        ny = y + dy[shark_dir] * p
        dfs(nx, ny, result + a + 1)
        shark = list(shark_save)
        shark_dir = shark_dir_save
        board = deepcopy(board_save)
        fish = deepcopy(fish_save)

# 물고기 이동
def move(board):
    for i in range(16):
        if fish[i] != [-1, -1]:
            x, y = fish[i]
            a, b = board[x][y]
            for p in range(8):
                direction = (b+p)%8
                nx, ny = x + dx[direction], y + dy[direction]
                if 0 <= nx < 4 and 0 <= ny < 4 and [nx, ny] != shark:
                    na, nb = board[nx][ny]
                    if na != -1:
                        fish[na] = [x, y]
                    board[x][y][1] = direction
                    board[nx][ny], board[x][y] = board[x][y], board[nx][ny]
                    fish[i] = [nx, ny]
                    break
    return board


dfs(0, 0, 0)
print(answer)
