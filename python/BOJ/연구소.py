from itertools import combinations

n, m = map(int, input().split())

safe = []
virus = []
world = []
temp_world = [[0]*m for _ in range(n)]

for i in range(n):
    data = list(map(int, input().split()))
    world.append(data)
    for j in range(m):
        if data[j] == 0:
            safe.append([i, j])
        elif data[j] == 2:
            virus.append([i, j])


combination = list(combinations(safe, 3))  # 벽을 세울 좌표 3개 뽑기


def dfs(x, y):  # 인접한 영역을 따라 바이러스가 퍼짐
    if x < 0 or y < 0 or x > n-1 or y > m-1 or temp_world[x][y] == 1 or visited[x][y]:
        return

    visited[x][y] = True
    temp_world[x][y] = 2

    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)


def count_safe():  # 안전 영역 크기 계산
    count = 0
    for i in range(n):
        for j in range(m):
            if temp_world[i][j] == 0:
                count += 1

    return count


answer = 0

for candidate in combination:  # 모든 경우의수 중에 안전 영역의 크기가 가장 큰 경우 찾기
    for i in range(n):
        for j in range(m):
            temp_world[i][j] = world[i][j]

    for a, b in candidate:
        temp_world[a][b] = 1  # 벽 3개 세우기

    visited = [[False] * m for _ in range(n)]

    for vx, vy in virus:  # temp_world에 바이러스가 퍼진 후의 지도 모습이 저장됨
        dfs(vx, vy)

    answer = max(answer, count_safe())

print(answer)
