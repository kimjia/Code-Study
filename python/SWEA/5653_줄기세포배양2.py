dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for test_case in range(1, T + 1):
    n, m, k = map(int, input().split())
    cell = [[[] for _ in range(m + 2*k + 1)] for _ in range(n + 2*k + 1)]
    num_alive = 0
    min_x, min_y, max_x, max_y = k, k, k+n, k+m
    for i in range(n):
        data = list(map(int, input().split()))
        for j in range(m):
            if data[j] > 0:
                num_alive += 1
                cell[k + i][k + j] = [data[j], data[j], data[j]]

    for time in range(k):
        # for row in range(len(cell)):
        #     print(cell[row])

        temp_cell = [[[] for _ in range(m + 2 * k + 1)] for _ in range(n + 2 * k + 1)]
        for x in range(min_x, max_x+1):
            for y in range(min_y, max_y+1):
                if cell[x][y]:
                    a, b, c = cell[x][y]
                    if [a, b, c] == [0, 0, 0]:
                        temp_cell[x][y] = [0, 0, 0]
                        continue
                    elif b > 0:
                        temp_cell[x][y] = [a, b-1, c]
                    elif c > 0:
                        if c == a:
                            for d in range(4):
                                nx, ny = x + dx[d], y + dy[d]
                                min_x = min(min_x, nx)
                                min_y = min(min_y, ny)
                                max_x = max(max_x, nx)
                                max_y = max(max_y, ny)
                                if not temp_cell[nx][ny] and not cell[nx][ny]:
                                    temp_cell[nx][ny] = [a, a, a]
                                    num_alive += 1
                                elif temp_cell[nx][ny]:
                                    na, nb, nc = temp_cell[nx][ny]
                                    if a > na > 0 and na == nb == nc:
                                        temp_cell[nx][ny] = [a, a, a]
                        if c == 1:
                            temp_cell[x][y] = [0, 0, 0]
                            num_alive -= 1
                        else:
                            temp_cell[x][y] = [a, b, c - 1]

        cell = temp_cell

    print('#' + str(test_case) + ' ' + str(num_alive))
