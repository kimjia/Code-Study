# 2021.04.17 PM 8:11 ~ 8:37

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m, k = map(int, input().split())
    cell = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
    for i in range(k):
        x, y, num, d = map(int, input().split())
        cell[x][y] = [num, d, num]

    for time in range(m):
        temp_cell = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
        for x in range(n):
            for y in range(n):
                if cell[x][y] != [0, 0, 0]:
                    num, d = cell[x][y][0], cell[x][y][1]
                    nx, ny = x + dx[d], y + dy[d]
                    if nx == 0 or nx == n-1 or ny == 0 or ny == n-1:
                        num //= 2
                        if d % 2 == 0:
                            d -= 1
                        else:
                            d += 1
                    if temp_cell[nx][ny] != [0, 0, 0]:
                        if temp_cell[nx][ny][2] > num:
                            temp_cell[nx][ny][0] += num
                        else:
                            temp_cell[nx][ny][0] += num
                            temp_cell[nx][ny][1] = d
                            temp_cell[nx][ny][2] = num
                    else:
                        temp_cell[nx][ny] = [num, d, num]
        cell = temp_cell

    answer = 0
    for x in range(n):
        for y in range(n):
            answer += cell[x][y][0]

    print('#' + str(test_case) + ' ' + str(answer))