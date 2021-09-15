from collections import deque

n, m, gas = map(int, input().split())
world = []
for i in range(n):
    data = list(map(int, input().split()))
    world.append(data)

x, y = map(int, input().split())
taxi = [x-1, y-1]

people_start = []
people_end = []
for i in range(m):
    a, b, c, d = list(map(int, input().split()))
    people_start.append([a-1, b-1])
    world[a-1][b-1] = 2 + i  # 손님
    people_end.append([c-1, d-1])

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

finished_num = 0
while finished_num < m:
    visited = [[False] * n for _ in range(n)]
    q = deque()
    q.append([0, taxi[0], taxi[1]])
    min_dist = 0

    # 손님찾기 (가장 가까운 곳 중 행번호, 열번호 작은 승객)
    while q:
        q = deque(sorted(q))
        dist, x, y = q.popleft()
        if visited[x][y]:
            continue
        visited[x][y] = True

        if world[x][y] > 1:
            guest_num = world[x][y] - 2
            min_dist = dist
            break

        if dist > gas:
            print(-1)
            exit(0)

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and world[nx][ny] != 1:
                q.append([dist + 1, nx, ny])
    else:
        print(-1)
        exit(0)

    taxi = [x, y]
    world[x][y] = 0
    gas -= dist

    # 도착지까지 최소 거리계산
    ax, ay = people_end[guest_num]
    visited = [[False] * n for _ in range(n)]
    q = deque()
    q.append([0, taxi[0], taxi[1]])
    while q:
        dist, x, y = q.popleft()
        if visited[x][y]:
            continue
        visited[x][y] = True

        if [x, y] == [ax, ay]:
            break

        if dist > gas:
            print(-1)
            exit(0)

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and world[nx][ny] != 1:
                q.append([dist + 1, nx, ny])
    else:
        print(-1)
        exit(0)

    # 도착한 경우
    taxi = [x, y]
    gas += dist
    finished_num += 1

print(gas)

