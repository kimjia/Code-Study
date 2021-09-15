from collections import deque

n, m = map(int, input().split())
board = []
rx, ry, bx, by = 0, 0, 0, 0

for i in range(n):
    data = list(input())
    board.append(data)
    for j in range(m):
        if board[i][j] == 'B':
            bx, by = i, j
        elif board[i][j] == 'R':
            rx, ry = i, j

dx = [0, 0, -1, 1]  # 왼, 오, 위, 아래
dy = [-1, 1, 0, 0]


def move(x, y, direction):
    move_count = 0
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if board[nx][ny] == 'O':  # 구멍 위치 도달한 경우 세번째 리턴값 = -1
            return nx, ny, -1
        elif board[nx][ny] != '#':
            x = nx
            y = ny
            move_count += 1
            continue
        else:  # 벽 도달
            break
    return x, y, move_count  # 벽에 도달한 경우 세번째 리턴값 = 이동한 횟수


def bfs():
    global rx, ry, bx, by
    q = deque()
    q.append([rx, ry, bx, by])
    visited = {(rx, ry, bx, by): 0}  # {(빨간 구슬 좌표, 파란 구슬 좌표):몇번째 이동에 도달했는지}
    while q:
        rx, ry, bx, by = q.popleft()
        for d in range(4):
            nrx, nry, rmove = move(rx, ry, d)
            nbx, nby, bmove = move(bx, by, d)

            if bmove == -1:  # 파란 구슬이 탈출한 경우
                continue
            elif rmove == -1:  # 빨간 구슬만 탈출한 경우
                print(visited[rx, ry, bx, by] + 1)  # 몇 번 이동해서 탈출했는지 출력
                return

            if nrx == nbx and nry == nby:  # 두 구슬이 같은 위치에 있는 경우
                if rmove > bmove:  # 더 많이 이동한 구슬을 한 칸 뒤로 이동시킴
                    nrx, nry = nrx - dx[d], nry - dy[d]
                else:
                    nbx, nby = nbx - dx[d], nby - dy[d]

            if (nrx, nry, nbx, nby) not in visited:  # visited 딕셔너리 업데이트
                visited[nrx, nry, nbx, nby] = visited[rx, ry, bx, by] + 1
                q.append([nrx, nry, nbx, nby])

        if not q or visited[rx, ry, bx, by] >= 10:  # 10번 이내에 탈출하지 못했거나, 모든 경우의수로 이동해도 탈출할 수 없는 경우
            print(-1)
            return


bfs()
