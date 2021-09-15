from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    mountain = []
    highest = []
    max_height = 0
    for i in range(n):
        data = list(map(int, input().split()))
        mountain.append(data)
        for j in range(n):
            if data[j] > max_height:
                max_height = data[j]
                highest = [[i, j]]
            elif data[j] == max_height:
                highest.append([i, j])

    # print(max_height, highest)
    answer = 0
    # highest= [highest[2]]

    for mx, my in highest:
        # print("mx, my:", mx, my)
        for x in range(n):
            for y in range(n):
                # print("x, y:", x, y)
                if [x, y] != [mx, my]:
                    # visited = [[False] * n for _ in range(n)]
                    # visited[mx][my] = True
                    q = deque()
                    q.append([mx, my, max_height, 1, [[mx, my]]])
                    while q:
                        a, b, height, dist, road_list = q.popleft()
                        # print(a, b, height, dist, road_list)
                        answer = max(answer, dist)
                        for d in range(4):
                            na, nb = a + dx[d], b + dy[d]
                            if 0 <= na < n and 0 <= nb < n:
                                # visited[na][nb] = True
                                if [na, nb] == [x, y]:
                                    for dig in range(k+1):
                                        nh = mountain[na][nb] - dig
                                        if nh < 0:
                                            break
                                        if nh < height and [na, nb] not in road_list:
                                            q.append([na, nb, nh, dist + 1, road_list + [[na, nb]]])
                                elif mountain[na][nb] < height and [na, nb] not in road_list:
                                    q.append([na, nb, mountain[na][nb], dist + 1, road_list + [[na, nb]]])

    print('#' + str(test_case) + ' ' + str(answer))
