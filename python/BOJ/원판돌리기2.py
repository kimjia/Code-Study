n, m, t = map(int, input().split())
data = []
rotate_list = []
total = 0
num = n * m
data.append([0] * m)
for _ in range(n):
    temp = list(map(int, input().split()))
    data.append(temp)
    for a in temp:
        total += a

for _ in range(t):
    x, d, k = map(int, input().split())
    rotate_list.append([x, d, k])

top = [0] * (n+1)
dx = [-1, 1, 0, 0]   # 위, 아래에 있는 원판
dy = [0, 0, -1, 1]   # 같은 원판 위 왼쪽, 오른쪽


def rotate(x, d, k):   # n번 원판 d 방향 k번 회전
    if d == 0:   # 시계방향
        top[x] = (top[x] - k) % m
    else:   # 반시계방향
        top[x] = (top[x] + k) % m


def delete():
    global total, num, data
    deleted_any = False
    temp_data = [[0] * m for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(m):
            temp_data[i][j] = data[i][j]

    for i in range(1, n+1):
        for j in range(m):
            x = i
            y = (j + top[i]) % m

            if data[x][y]:
                # print("x, y, data[x][y]: ", x, y, data[x][y])
                deleted = False
                for d in range(4):
                    nx = x + dx[d]
                    if 0 < nx <= n:
                        ny = (j + dy[d] + top[nx]) % m
                        # print("nx, ny, data[nx][ny]: ", nx, ny, data[nx][ny])
                        if data[x][y] == data[nx][ny] and temp_data[nx][ny]:
                            # print(data[x][y])
                            total -= data[nx][ny]
                            num -= 1
                            temp_data[nx][ny] = 0
                            deleted = True
                            deleted_any = True

                if deleted:
                    if temp_data[x][y]:
                        total -= data[x][y]
                        num -= 1
                        temp_data[x][y] = 0
    if total == 0:
        return

    if not deleted_any:
        average = total/num
        # print(average)
        for i in range(1, n+1):
            for j in range(m):
                if data[i][j] > average:
                    data[i][j] -= 1
                    total -= 1
                elif 0 < data[i][j] < average:
                    data[i][j] += 1
                    total += 1
    else:
        data = temp_data


for x, d, k in rotate_list:
    save_x = x
    while x <= n:
        rotate(x, d, k)
        x += save_x
    # print(data)
    # print(top)
    delete()
    if total == 0:
        break
    # print(data)
    # print(top)


print(total)
