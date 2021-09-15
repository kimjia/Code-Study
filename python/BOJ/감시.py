import copy

n, m = map(int, input().split())
room = []
cctv = []  # cctv들의 좌표
# 0: 위, 1: 오, 2: 아래, 3: 왼
direction = {1: [[0], [1], [2], [3]],
             2: [[0, 2], [1, 3]],
             3: [[0, 1], [1, 2], [2, 3], [3, 0]],
             4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
             5: [[0, 1, 2, 3]]}
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
num_cctv = 0

for i in range(n):
    data = list(map(int, input().split()))
    room.append(data)
    for j in range(m):
        if 1 <= data[j] <= 5:
            cctv.append([i, j, data[j]])    # x좌표, y좌표, cctv 번호
            num_cctv += 1


def dfs(i, graph):  # i번째 cctv
    global answer
    if i == num_cctv:
        blind = 0
        for a in range(n):
            for b in range(m):
                if graph[a][b] == 0:
                    blind += 1
        answer = min(answer, blind)
        return

    x, y, num = cctv[i]
    for d_ in direction[num]:
        temp_room = [[0] * m for _ in range(n)]
        for p in range(n):
            for q in range(m):
                if graph[p][q] != 0:
                    temp_room[p][q] = graph[p][q]

        for d in d_:
            nx = x + dx[d]
            ny = y + dy[d]
            while 0 <= nx < n and 0 <= ny < m:
                if temp_room[nx][ny] == 6:
                    break
                elif temp_room[nx][ny] == 0:
                    temp_room[nx][ny] = '#'
                nx += dx[d]
                ny += dy[d]
        dfs(i+1, temp_room)


answer = n * m
dfs(0, room)
print(answer)
