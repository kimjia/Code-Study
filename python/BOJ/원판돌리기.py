n, m, t = map(int, input().split())
data = [[0] * m]
rotate_list = []
total = 0
num = n * m
for _ in range(n):
    temp = list(map(int, input().split()))
    data.append(temp)
    for a in temp:
        total += a

for _ in range(t):
    x, d, k = map(int, input().split())
    rotate_list.append([x, d, k])

dx = [-1, 1, 0, 0]   # 위, 아래에 있는 원판
dy = [0, 0, -1, 1]   # 같은 원판 위 왼쪽, 오른쪽


def rotate(x, d, k):   # n번 원판 d 방향 k번 회전
    global data
    temp = [0] * m
    if k >= m:
        k %= m
    if d == 0:   # 시계방향
        for j in range(m):
            temp[j] = data[x][(j-k)%m]
    else:   # 반시계방향
        for j in range(m):
            temp[j] = data[x][(j + k) %m]
    data[x] = temp


def delete():
    global total, num, data
    deleted_any = False
    temp_data = [[0] * m for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(m):
            temp_data[i][j] = data[i][j]

    for x in range(1, n+1):
        for y in range(m):
            if data[x][y]:
                deleted = False
                for d in range(4):
                    nx, ny = x + dx[d], (y + dy[d]) % m
                    # 하나 삭제할 때마다 total과 num 수정
                    if 0 < nx <= n and temp_data[nx][ny] and data[x][y] == data[nx][ny]:
                        total -= data[nx][ny]
                        num -= 1
                        temp_data[nx][ny] = 0
                        deleted = True

                if deleted and temp_data[x][y]:
                    total -= data[x][y]
                    num -= 1
                    temp_data[x][y] = 0
                    deleted_any = True

    if total == 0:
        return

    if not deleted_any:  # 삭제된 수가 없으면 평균 구해서 계산
        average = total/num
        for i in range(1, n+1):
            for j in range(m):
                if 0 < data[i][j] < average:
                    data[i][j] += 1
                    total += 1
                elif data[i][j] > average:
                    data[i][j] -= 1
                    total -= 1
    else:
        data = temp_data


for x, d, k in rotate_list:
    save_x = x
    while x <= n:
        rotate(x, d, k)
        x += save_x
    delete()
    if total == 0:
        break

print(total)
