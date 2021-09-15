n = int(input())
A = []
for i in range(n):
    data = list(map(int, input().split()))
    A.append(data)

answer = 0
center = (n + 1) // 2 - 1
x, y = center, center
length_list = []
for i in range(1, n):
    length_list.append(i)
    length_list.append(i)
length_list.append(n-1)

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


# 모래 이동
def move_sand(nx, ny, d, percent):
    global answer
    # d: 왼, 아래, 오, 위
    if percent == 5:
        px1, py1 = nx + 2 * dx[d[3]], ny + 2 * dy[d[3]]
        px2, py2 = -10, -10
    elif percent == 1:
        px1, py1 = nx + dx[d[1]] + dx[d[0]], ny + dy[d[1]] + dy[d[0]]
        px2, py2 = nx + dx[d[1]] + dx[d[2]], ny + dy[d[1]] + dy[d[2]]
    elif percent == 2:
        px1, py1 = nx + 2 * dx[d[0]], ny + 2 * dy[d[0]]
        px2, py2 = nx + 2 * dx[d[2]], ny + 2 * dy[d[2]]
    elif percent == 7:
        px1, py1 = nx + dx[d[0]], ny + dy[d[0]]
        px2, py2 = nx + dx[d[2]], ny + dy[d[2]]
    else:  # percent == 10
        px1, py1 = nx + dx[d[3]] + dx[d[0]], ny + dy[d[3]] + dy[d[0]]
        px2, py2 = nx + dx[d[3]] + dx[d[2]], ny + dy[d[3]] + dy[d[2]]

    if 0 <= px1 < n and 0 <= py1 < n:
        A[px1][py1] += int(sand_save * percent / 100)
    else:
        answer += int(sand_save * percent / 100)
    A[nx][ny] -= int(sand_save * percent / 100)

    if px2 == -10:
        return

    if 0 <= px2 < n and 0 <= py2 < n:
        A[px2][py2] += int(sand_save * percent / 100)
    else:
        answer += int(sand_save * percent / 100)
    A[nx][ny] -= int(sand_save * percent / 100)


for num, length in enumerate(length_list):
    d = num % 4
    d_left = (d + 1) % 4  # 아래
    d_right = (d - 1) % 4  # 위
    d_bottom = (d + 2) % 4  # 오

    direction = [d_left, d_bottom, d_right, d]

    for k in range(length):
        # x, y에서 nx, ny로 이동 -> nx, ny의 모래들이 흩어짐
        nx, ny = x + dx[d], y + dy[d]
        sand_save = A[nx][ny]

        move_sand(nx, ny, direction, 2)
        move_sand(nx, ny, direction, 7)
        move_sand(nx, ny, direction, 1)
        move_sand(nx, ny, direction, 10)
        move_sand(nx, ny, direction, 5)

        # alpha
        ax, ay = nx + dx[d], ny + dy[d]
        if 0 <= ax < n and 0 <= ay < n:
            A[ax][ay] += A[nx][ny]
        else:
            answer += A[nx][ny]

        A[nx][ny] = A[x][y]
        x, y = nx, ny


print(answer)
