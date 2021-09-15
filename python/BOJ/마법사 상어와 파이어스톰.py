from collections import deque

n, q = map(int, input().split())
A = []
for i in range(2 ** n):
    data = list(map(int, input().split()))
    A.append(data)

level_list = list(map(int, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for level in level_list:
    temp_A = [[0] * (2**n) for _ in range(2**n)]

    for start_x in range(0, 2 ** n, 2 ** level):  # 시계방향 회전
        for start_y in range(0, 2 ** n, 2 ** level):
            end_x = start_x + 2 ** level
            end_y = start_y + 2 ** level

            for x in range(2**level):
                for y in range(2**level):
                    temp_A[start_x + y][end_y - 1 - x] = A[start_x + x][start_y + y]

    A = temp_A
    temp_A = [[0] * (2 ** n) for _ in range(2 ** n)]

    for x in range(2 ** n):  # 얼음 양 감소
        for y in range(2 ** n):
            num_ice = 0
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < 2**n and 0 <= ny < 2**n and A[nx][ny] > 0:
                    num_ice += 1
            if num_ice < 3 and A[x][y] > 0:
                temp_A[x][y] = A[x][y]-1
            else:
                temp_A[x][y] = A[x][y]

    A = temp_A


visited = [[False] * (2**n) for _ in range(2**n)]
q = deque()
total_ice = 0
max_size = 0

for i in range(2**n):  # 얼음 덩어리 크기 계산
    for j in range(2**n):
        if A[i][j] == 0 or visited[i][j]:
            continue
        q.append([i, j])  # 좌표, size
        temp_size = 0

        while q:
            x, y = q.popleft()

            if visited[x][y]:
                continue

            visited[x][y] = True
            total_ice += A[x][y]
            temp_size += 1

            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < 2**n and 0 <= ny < 2**n:
                    if A[nx][ny] > 0:
                        q.append([nx, ny])

        max_size = max(max_size, temp_size)

print(total_ice)
print(max_size)
