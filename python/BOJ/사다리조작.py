n, m, h = map(int, input().split())
lines = [[0] * (n+1) for _ in range(h+1)]
for _ in range(m):
    a, b = map(int, input().split())
    lines[a][b] = 1

line_candidates = []
for i in range(1, h+1):
    for j in range(1, n):
        if lines[i][j] == 0 and lines[i][j-1] == 0 and lines[i][j+1] == 0:
            line_candidates.append((i, j))

answer = 4


def dfs(num, i):
    global answer
    if i >= len(line_candidates) or num >= answer:
        return

    success = True
    for x in range(1, n + 1):  ###############
        cur = x
        for y in range(1, h + 1):
            if lines[y][cur] == 1:
                cur += 1
            elif lines[y][cur-1] == 1:
                cur -= 1
        if cur != x:
            success = False
            break

    if success:
        answer = min(num, answer)
        return
    for idx in range(i+1, len(line_candidates)):
        x, y = line_candidates[idx]
        if lines[x][y-1] == 0 and lines[x][y+1] == 0:
            lines[x][y] = 1
            dfs(num+1, idx)
            lines[x][y] = 0


dfs(0, -1)
if answer < 4:
    print(answer)
else:
    print(-1)
