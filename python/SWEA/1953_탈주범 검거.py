from collections import deque

tunnel_list = {
    1:[0,1,2,3],
    2:[0,1],
    3:[2,3],
    4:[0,3],
    5:[1,3],
    6:[1,2],
    7:[0,2]
}
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m, r, c, l = map(int, input().split())
    world = []
    for _ in range(n):
        world.append(list(map(int, input().split())))

    visited = [[False] * m for _ in range(n)]
    visited[r][c] = True
    q = deque()
    q.append([r, c, 1])
    num_visited = 1
    while q:
        x, y, time = q.popleft()

        if time == l:
            continue
        tunnel_type = world[x][y]
        for d in tunnel_list[tunnel_type]:
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and world[nx][ny] > 0:
                if (d % 2 == 0 and (d+1) in tunnel_list[world[nx][ny]]) or (d % 2 == 1 and (d-1) in tunnel_list[world[nx][ny]]):
                    num_visited += 1
                    visited[nx][ny] = True
                    q.append([nx, ny, time+1])

    print('#' + str(test_case) + ' ' + str(num_visited))
