from collections import deque

n, m, k = map(int, input().split())
grid = [[[0, 0] for _ in range(n)] for _ in range(n)]

# 상어 위치
shark_pos = [[-1, -1] for _ in range(m+1)]
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j]:
            shark_pos[data[j]] = [i, j]
            grid[i][j] = [data[j], k]

# 상어 방향
shark_dir = [0]
shark_dir.extend(list(map(int, input().split())))

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

# 방향 우선순의
decide_dir = [[[0, 0, 0, 0] for _ in range(5)] for _ in range(m + 1)]
for i in range(1, m + 1):
    decide_dir[i][1] = list(map(int, input().split()))
    decide_dir[i][2] = list(map(int, input().split()))
    decide_dir[i][3] = list(map(int, input().split()))
    decide_dir[i][4] = list(map(int, input().split()))

time = 1
num_shark = m
while time <= 1000:
    endflag = False
    # 이동 + 냄새 뿌리기
    temp_grid = [[[0, 0] for _ in range(n)] for _ in range(n)]
    for i in range(1, m+1):
        x, y = shark_pos[i]
        if x == -1:
            continue
        direction = decide_dir[i][shark_dir[i]]
        move_list = deque()
        move_x, move_y, move_dir = -1, -1, -1
        for d in direction:
            nx, ny = x + dx[d], y + dy[d]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if grid[nx][ny] == [0, 0]:  # 아무 냄새가 없는 칸
                move_list.appendleft([nx, ny, d])
                break
            elif grid[nx][ny][0] == i:  # 자신의 냄새가 있는 칸
                move_list.append([nx, ny, d])
        if move_list:
            move_x, move_y, move_dir = move_list[0]

        if move_x != -1:  # 이동
            # 이동하고자 하는 칸에 상어가 있을 때, 둘중 하나 쫓아냄
            if temp_grid[move_x][move_y] != [0, 0]:
                save_num = min(i, temp_grid[move_x][move_y][0])  # 남아있는 상어번호
                out_num = max(i, temp_grid[move_x][move_y][0])  # 쫓겨나는 상어번호

                shark_pos[out_num] = [-1, -1]
                shark_dir[out_num] = -1
                num_shark -= 1
                temp_grid[move_x][move_y] = [save_num, k]

                if save_num == i:
                    shark_pos[save_num] = [move_x, move_y]
                    shark_dir[save_num] = move_dir
                if num_shark == 1:
                    print(time)
                    exit(0)
                    endflag = True
                    break
            else:  # 이동하고자 하는 칸이 비어있을 때
                temp_grid[move_x][move_y] = [i, k]  # 이동 + 냄새 뿌리기
                shark_pos[i] = [move_x, move_y]
                shark_dir[i] = move_dir
    if endflag:
        break

    # 복사 & 숫자 하나 감소
    for i in range(n):
        for j in range(n):
            if temp_grid[i][j] != [0, 0]:
                grid[i][j] = temp_grid[i][j]
            elif grid[i][j][1] > 1:
                grid[i][j][1] -= 1
            elif grid[i][j][1] == 1:
                grid[i][j] = [0, 0]

    time += 1

else:
    print(-1)
