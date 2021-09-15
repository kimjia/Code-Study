dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for test_case in range(1, T + 1):
    n, m, k = map(int, input().split())
    cell = [[0] * (m+k) for _ in range(n+k)]
    active = [[] for _ in range(11)]

    num_alive = 0
    for i in range(n):
        data = list(map(int, input().split()))
        for j in range(m):
            if data[j] > 0:
                num_alive += 1
                cell[i][j] = data[j]
                active[data[j]].append([i, j, data[j]])

    for time in range(k):
        for X in range(10, 0, -1):
            new = []
            dead = []
            for i in range(len(active[X])):
                active[X][i][2] -= 1
                x, y, life = active[X][i]
                if life == -1:
                    for d in range(4):
                        nx, ny = (x + dx[d]) % (n+k), (y + dy[d]) % (m+k)
                        if not cell[nx][ny]:
                            cell[nx][ny] = X
                            num_alive += 1
                            new.append([nx, ny, X])
                if life == -X:
                    dead.append(i)
                    num_alive -= 1

            for idx in sorted(dead, reverse=True):
                active[X].pop(idx)
            active[X].extend(new)

    print('#' + str(test_case) + ' ' + str(num_alive))
