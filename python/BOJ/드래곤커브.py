n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
answer_grid = []

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def rotate(x, y, grid):  # 시계방향 회전
    origin = len(grid)
    for k in range(origin):
        p, q = grid[k]
        i, j = p - x, q - y
        nx, ny = x - j, y + i
        if k == 0:
            rx, ry = nx, ny
        if 0 <= nx <= 100 and 0 <= ny <= 100 and [nx, ny] not in grid:
            grid.append([nx, ny])
            if [nx, ny] not in answer_grid:
                answer_grid.append([nx, ny])
    return rx, ry


for x, y, d, g in data:
    grid = []
    if [x, y] not in grid:
        grid.append([x, y])
        if [x, y] not in answer_grid:
            answer_grid.append([x, y])
    nx, ny = x + dx[d], y + dy[d]
    if 0 <= nx <= 100 and 0 <= ny <= 100 and [nx, ny] not in grid:
        grid.append([nx, ny])
        if [nx, ny] not in answer_grid:
            answer_grid.append([nx, ny])
    x, y = nx, ny
    for _ in range(g):
        x, y = rotate(x, y, grid)


answer = 0
answer_grid.sort()
for a, b in answer_grid:
    if [a, b+1] in answer_grid and [a+1, b] in answer_grid and [a+1, b+1] in answer_grid:
        answer += 1
print(answer)
