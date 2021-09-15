dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

n, m, x, y, k = map(int, input().split())
dice = [0, 0, 0, 0, 0, 0]

world = []
for _ in range(n):
    data = list(map(int, input().split()))
    world.append(data)

move = list(map(int,input().split()))

# 윗면 0, 동쪽 1, 서쪽 2, 북쪽 3, 남쪽 4, 아랫면 5


def roll_dice(dice, direction):
    new_dice = [0, 0, 0, 0, 0, 0]
    if direction == 1: # 동
        new_dice[0] = dice[2]
        new_dice[1] = dice[0]
        new_dice[2] = dice[5]
        new_dice[3] = dice[3]
        new_dice[4] = dice[4]
        new_dice[5] = dice[1]
    elif direction == 2: # 서
        new_dice[0] = dice[1]
        new_dice[1] = dice[5]
        new_dice[2] = dice[0]
        new_dice[3] = dice[3]
        new_dice[4] = dice[4]
        new_dice[5] = dice[2]
    elif direction == 3: # 북
        new_dice[0] = dice[4]
        new_dice[1] = dice[1]
        new_dice[2] = dice[2]
        new_dice[3] = dice[0]
        new_dice[4] = dice[5]
        new_dice[5] = dice[3]
    else: # 남
        new_dice[0] = dice[3]
        new_dice[1] = dice[1]
        new_dice[2] = dice[2]
        new_dice[3] = dice[5]
        new_dice[4] = dice[0]
        new_dice[5] = dice[4]

    return new_dice


for d in move:
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx <= (n-1) and 0 <= ny <= (m-1):
        dice = roll_dice(dice, d)
        if world[nx][ny] == 0:
            world[nx][ny] = dice[5]
        else:
            dice[5] = world[nx][ny]
            world[nx][ny] = 0
        print(dice[0])
        x = nx
        y = ny
    else:
        continue

