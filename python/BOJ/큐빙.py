def rotate(side):  # 시계방향으로 한번 돌리기
    if side == 'U':
        SIDE = U
        X, Y, Z, W = L, F, R, B
    elif side == 'D':
        SIDE = D
        X, Y, Z, W = B, R, F, L
    elif side == 'F':
        SIDE = F
        X, Y, Z, W = U, L, D, R
    elif side == 'B':
        SIDE = B
        X, Y, Z, W = R, D, L, U
    elif side == 'L':
        SIDE = L
        X, Y, Z, W = F, U, B, D
    elif side == 'R':
        SIDE = R
        X, Y, Z, W = D, B, U, F

    SIDE[0][2], SIDE[1][2], SIDE[2][2], SIDE[2][1], SIDE[2][0], SIDE[1][0], SIDE[0][0], SIDE[0][1] \
        = SIDE[0][0], SIDE[0][1], SIDE[0][2], SIDE[1][2], SIDE[2][2], SIDE[2][1], SIDE[2][0], SIDE[1][0]

    X[2][2], X[2][1], X[2][0], Y[2][0], Y[1][0], Y[0][0], Z[0][2], Z[1][2], Z[2][2], W[0][0], W[0][1], W[0][2] \
        = Y[2][0], Y[1][0], Y[0][0], Z[0][2], Z[1][2], Z[2][2], W[0][0], W[0][1], W[0][2], X[2][2], X[2][1], X[2][0]


def print_color():
    for i in range(3):
        string = ''
        for j in range(3):
            string += U[i][j]
        print(string)


n = int(input())
move = []
turn_list = []
for i in range(n):
    move.append(int(input()))
    turn_list.append(list(map(str, input().split())))

for i in range(n):
    U = [['w'] * 3 for _ in range(3)]  # 윗면
    D = [['y'] * 3 for _ in range(3)]  # 아랫면
    F = [['r'] * 3 for _ in range(3)]  # 앞면
    B = [['o'] * 3 for _ in range(3)]  # 뒷면
    L = [['g'] * 3 for _ in range(3)]  # 왼쪽면
    R = [['b'] * 3 for _ in range(3)]  # 오른쪽면
    for turn in turn_list[i]:
        side = turn[0]  # 면
        direction = turn[1]  # 방향
        rotate(side)
        if direction == '-':  # 반시계방향 1번 = 시계방향 3번
            rotate(side)
            rotate(side)
    print_color()
