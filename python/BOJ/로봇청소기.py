dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
 
n, m = map(int, input().split())
x, y, d = map(int, input().split())
world = []
for _ in range(n):
    data = list(map(int, input().split()))
    world.append(data)


def rotate(d): # 왼쪽 방향 리턴
    if d == 0:
        return 3
    else:
        return d - 1


def backward(d): # 뒤쪽 방향 리턴
    if d == 2:
        return 0
    elif d == 3:
        return 1
    else:
        return d + 2


count = 0
found = False

while True:
    if world[x][y] == 0: # 현재 칸이 청소되지 않은 상태이면 청소
        world[x][y] = 2
        count += 1

    found = False
    for _ in range(4): # 왼쪽 방향으로 돌면서 앞에 청소되지 않은 곳이 있는지 확인
        d = rotate(d)  # 왼쪽 방향
        nx = x + dx[d]
        ny = y + dy[d]
        if world[nx][ny] == 0:  # 청소가 되지 않은 칸이 있으면 그 칸으로 이동 (found)
            x = nx
            y = ny
            found = True
            break

    if not found: # 모든 방향에 갈 곳이 없을 때
        back_d = backward(d) # 뒤쪽 체크
        back_x = x + dx[back_d]
        back_y = y + dy[back_d]
        if world[back_x][back_y] == 1: # 뒤쪽도 벽으로 막혀있는 경우
            break
        else:
            x = back_x
            y = back_y


print(count)