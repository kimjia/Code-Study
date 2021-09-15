from collections import deque

N = int(input())
K = int(input())
board = [[0] * N for _ in range(N)]

for _ in range(K):
    a, b = map(int, input().split())
    board[a-1][b-1] = 2  # 사과가 있는 곳 = 2

L = int(input())
moves = []
for _ in range(L):
    a, b = map(str, input().split())
    moves.append([int(a), b])

dx = [-1, 0, 1, 0]  # 위, 왼, 아, 오
dy = [0, -1, 0, 1]

time = 0
direction = 3
q = deque()
q.append([0, 0])
board[0][0] = 1  # 뱀이 위치한 곳 = 1
while True:
    if moves and time == moves[0][0]:
        if moves[0][1] == 'L':
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4
        moves.pop(0)
    time += 1
    x, y = q[-1]  # 머리 위치
    nx = x + dx[direction]
    ny = y + dy[direction]
    if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 1:  # 벽이나 몸에 부딪히는 경우 종료
        break
    else:
        q.append([nx, ny])
        if board[nx][ny] == 0:  # 새로운 머리 위치에 사과가 없는 경우 꼬리 이동
            tail_x, tail_y = q.popleft()
            board[tail_x][tail_y] = 0
        board[nx][ny] = 1

print(time)
