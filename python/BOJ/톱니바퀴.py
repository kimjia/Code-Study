gear = []
for _ in range(4):
    input_str = input()
    gear.append([int(i) for i in input_str])

k = int(input())
rotate_list = [[0] * 4 for _ in range(k)]
data = []
for i in range(k):
    a, b = map(int, input().split())
    rotate_list[i][a - 1] = b
    data.append([a, b])

# 0번이 top


def rotate(num, direction):  # 톱니 회전시키기 num번째(0~3) 톱니 direction(1, -1) 방향으로
    temp = [0]*8
    for i in range(8):
        if direction == 1:  # 시계방향
            if i == 7:
                temp[0] = gear[num][i]
            else:
                temp[i+1] = gear[num][i]
        elif direction == -1:  # 반시계방향
            if i == 0:
                temp[7] = gear[num][i]
            else:
                temp[i-1] = gear[num][i]
        else:
            temp = list(gear[num])
    gear[num] = list(temp)


def change_direction(direction):
    if direction == -1:
        return 1
    else:
        return -1


def side_gear(n, num, d):  # 회전한 톱니와 이웃한 톱니 회전 여부 결정
    if num < 0 or num >= 4:
        return
    else:
        if d == 'left':  # 처음 회전한 톱니보다 왼쪽에 있는 톱니
            if rotate_list[n][num+1] == 0:
                return
            right = gear[num+1][6]
            left = gear[num][2]
            if right != left:
                rotate_list[n][num] = change_direction(rotate_list[n][num+1])
            else:
                return
        else:  # 처음 회전한 톱니보다 오른쪽에 있는 톱니
            if rotate_list[n][num-1] == 0:
                return
            left = gear[num-1][2]
            right = gear[num][6]
            if right != left:
                rotate_list[n][num] = change_direction(rotate_list[n][num - 1])
            else:
                return


for n in range(k):
    num, direction = data[n]
    num -= 1
    for x in range(1, 4):
        side_gear(n, num - x, 'left')
        side_gear(n, num + x, 'right')
    for i in range(4):
        rotate(i, rotate_list[n][i])\

answer = 0
for i in range(4):
    if gear[i][0] == 1:
        answer += 2 ** i
print(answer)
