r, c, t = map(int, input().split())
room = []
purifier = []
for i in range(r):
    data = list(map(int, input().split()))
    for j in range(c):
        if data[j] == -1:
            purifier.append([i, j])
    room.append(data)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dx2 = [1, 0, -1, 0]
dy2 = [0, 1, 0, -1]

for time in range(t):
    temp_room = [[0] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if room[x][y] > 0:
                move = int(room[x][y]/5)
                for d1, d2 in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nx = x + d1
                    ny = y + d2
                    if 0 <= nx < r and 0 <= ny < c and room[nx][ny] >= 0:
                        temp_room[nx][ny] += move
                        temp_room[x][y] -= move

    for a in range(r):
        for b in range(c):
            room[a][b] += temp_room[a][b]

    px1, py1 = purifier[0]
    px2, py2 = purifier[1]
    x1, y1 = purifier[0]
    x2, y2 = purifier[1]
    for d in range(4):
        while True:
            nx1, ny1 = x1 + dx[d], y1 + dy[d]
            nx2, ny2 = x2 + dx2[d], y2 + dy2[d]
            in_range1, in_range2 = False, False
            if 0 <= nx1 <= px1 and 0 <= ny1 < c:
                room[x1][y1] = room[nx1][ny1]
                in_range1 = True
                x1, y1 = nx1, ny1
            if px2 <= nx2 < r and 0 <= ny2 < c:
                room[x2][y2] = room[nx2][ny2]
                in_range2 = True
                x2, y2 = nx2, ny2
            if not in_range1 and not in_range2:
                break

    room[px1][py1] = -1
    room[px2][py2] = -1
    room[px1][py1+1] = 0
    room[px2][py2+1] = 0

answer = 0
for i in range(r):
    for j in range(c):
        if room[i][j] > 0:
            answer += room[i][j]
print(answer)



