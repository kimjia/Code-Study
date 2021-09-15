n, m, k = map(int, input().split())
grid = [[[0, 0, -1] for _ in range(n)] for _ in range(n)]
num_fireball = [[0] * n for _ in range(n)]

for i in range(m):
    r, c, m, s, d = map(int, input().split())
    grid[r-1][c-1] = [m, s, d]
    num_fireball[r-1][c-1] = 1

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]  # 방향: 0~7

for time in range(k):
    temp_grid = [[[0, 0, -1] for _ in range(n)] for _ in range(n)]
    temp_num = [[0] * n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if grid[x][y] != [0, 0, -1]:
                m, s, d = grid[x][y]
                for i in range(4):
                    if grid[x][y][2] == -1:  # 합쳐지지 않은 칸은 한번만
                        continue
                    elif grid[x][y][2] < 8:  # 합쳐지지 않은 칸 (원래 방향대로)
                        nx, ny = (x + s * dx[d]) % n, (y + s * dy[d]) % n
                        grid[x][y][2] = -1
                        mass, speed = m, s
                        direction = d
                    else:
                        mass = m // 5
                        speed = s // num_fireball[x][y]  # 4개로 쪼개기
                        if 10 <= grid[x][y][2] <= 11:  # 짝수만/홀수만: 0, 2, 4, 6
                            direction = 2 * i
                            nx, ny = (x + speed * dx[direction]) % n, (y + speed * dy[direction]) % n
                        else:  # 13
                            direction = 2 * i + 1
                            nx, ny = (x + speed * dx[direction]) % n, (y + speed * dy[direction]) % n

                    if mass == 0:
                        continue

                    temp_grid[nx][ny][0] += mass
                    temp_grid[nx][ny][1] += speed
                    temp_num[nx][ny] += 1

                    # -1: 아직 안정함, 11: 홀수만, 10: 짝수만 (0, 2, 4, 6), 13: 나머지 (1, 3, 5, 7)
                    if temp_grid[nx][ny][2] == 13:
                        continue
                    elif temp_grid[nx][ny][2] == -1:  # 아직 안 정함
                        temp_grid[nx][ny][2] = direction
                    elif temp_grid[nx][ny][2] < 8:  # 하나만 들어있던 경우
                        if temp_grid[nx][ny][2] % 2 == direction % 2:
                            temp_grid[nx][ny][2] = direction % 2 + 10
                        else:
                            temp_grid[nx][ny][2] = 13
                    elif temp_grid[nx][ny][2] != (direction % 2 + 10):  # 두개 이상 들어있던 경우
                        temp_grid[nx][ny][2] = 13

    num_fireball = temp_num
    grid = temp_grid

answer = 0
for x in range(n):
    for y in range(n):
        if num_fireball[x][y] > 1:
            answer += (grid[x][y][0] // 5 * 4)
        else:
            answer += grid[x][y][0]
print(answer)
