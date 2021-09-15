r, c, m = map(int, input().split())
shark = [[[] for _ in range(c)] for _ in range(r)]
for _ in range(m):
    a, b, s, d, z = map(int, input().split())
    shark[a-1][b-1] = [s, d, z]

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]


def shark_move():  # 상어 이동
    global shark
    new_shark = [[[] for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if shark[i][j]:
                s, d, z = shark[i][j]
                x, y = i, j
                # 속력에 맞게 이동
                if d <= 2:  # 상하이동
                    same = s // (2 * (r-1))
                    rest = s % (2 * (r-1))
                else:  # 좌우이동
                    same = s // (2 * (c - 1))
                    rest = s % (2 * (c - 1))
                # if same % 2 == 1:
                #     if d % 2 == 0:
                #         d -= 1
                #     else:
                #         d += 1
                while rest > 0:
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < r and 0 <= ny < c:
                        x, y = nx, ny
                        rest -= 1
                    else:
                        if d % 2 == 0:
                            d -= 1
                        else:
                            d += 1
                # 이동 후 위치 저장
                if new_shark[x][y]:  # 상어가 여러 마리 있는 경우 가장 큰 상어만 남김
                    if z > new_shark[x][y][2]:
                        new_shark[x][y] = [s, d, z]
                else:
                    new_shark[x][y] = [s, d, z]

    shark = new_shark


answer = 0
for t in range(c):
    for row in range(r):
        if shark[row][t]:  # 땅에서 가장 가까운 상어 잡기
            s, d, z = shark[row][t]
            answer += z
            shark[row][t] = []
            break
    shark_move()

print(answer)
