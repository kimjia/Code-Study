from itertools import combinations
from collections import deque

n, m = map(int, input().split())
lab = []
virus = []
num_wall = 0
num_virus = 0
for i in range(n):
    data = list(map(int, input().split()))
    lab.append(data)
    for j in range(n):
        if data[j] == 2:
            virus.append([i, j])
            num_virus += 1
        elif data[j] == 1:
            num_wall += 1

candidates = list(combinations(virus, m))
answer = n*n+2

for c in candidates:
    temp_lab = [[-1] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if lab[i][j]:
                temp_lab[i][j] = lab[i][j]

    q = deque()
    time = 0
    for x, y in c:
        q.append([x, y, 0])
    temp_virus = num_virus
    visited = [[False] * n for _ in range(n)]
    max_time = 0
    while q:
        a, b, time = q.popleft()
        max_time = max(time, max_time)
        if time > answer:
            break
        if visited[a][b]:
            continue
        elif temp_lab[a][b] == -1:
            temp_virus += 1

        if temp_virus == n*n - num_wall:
            break
        visited[a][b] = True
        temp_lab[a][b] = time
        for da, db in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            na, nb = a + da, b + db
            if 0 <= na < n and 0 <= nb < n and not visited[na][nb] and temp_lab[na][nb] != 1:
                q.append([na, nb, time+1])

    if temp_virus == n * n - num_wall:
        answer = min(answer, max_time)

if answer < n*n+2:
    print(answer)
else:
    print(-1)