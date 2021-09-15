
from copy import deepcopy
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(idx, i, num_break):
    global answer, board

    q = deque()
    for x in range(h):
        if board[x][idx] > 0:
            q.append([x, idx])
            break

    add_break = 0
    visited = [[False] * w for _ in range(h)]
    while q:
        x, y = q.popleft()
        if board[x][y] == 0 or visited[x][y]:
            continue
        visited[x][y] = True
        number = board[x][y] - 1
        add_break += 1
        board[x][y] = 0
        for d in range(4):
            for mul in range(1, number + 1):
                nx, ny = x + mul * dx[d], y + mul * dy[d]
                if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and board[nx][ny] > 0:
                    q.append([nx, ny])

    for col in range(w):
        cur = h-1
        for row in range(h-1, -1, -1):
            if board[row][col] > 0:
                board[cur][col] = board[row][col]
                cur -= 1
        for row in range(cur+1):
            board[row][col] = 0

    if i == n-1:
        answer = max(answer, num_break + add_break)
        return

    temp_board = deepcopy(board)
    for next_idx in range(w):
        dfs(next_idx, i+1, num_break + add_break)
        board = deepcopy(temp_board)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, w, h = map(int, input().split())
    total_block = 0
    board = []
    for _ in range(h):
        data = list(map(int, input().split()))
        board.append(data)
        total_block += (w - data.count(0))
    answer = 0
    temp_board = deepcopy(board)
    for f in range(w):
        dfs(f, 0, 0)
        board = deepcopy(temp_board)
    print('#'+str(test_case)+' '+str(total_block-answer))
