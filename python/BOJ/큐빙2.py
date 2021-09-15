n = int(input())
moves = []
turns = []
for _ in range(n):
    moves.append(int(input()))
    turns.append(list(map(str, input().split())))


def rotate(side):
    if side == 'U':
        T, X, Y, Z, W = U, L, F, R, B
    elif side == 'L':
        T, X, Y, Z, W = L, F, U, B, D
    elif side == 'R':
        T, X, Y, Z, W = R, D, B, U, F
    elif side == 'F':
        T, X, Y, Z, W = F, U, L, D, R
    elif side == 'B':
        T, X, Y, Z, W = B, R, D, L, U
    elif side == 'D':
        T, X, Y, Z, W = D, B, R, F, L

    T[2], T[5], T[8], T[1], T[4], T[7], T[0], T[3], T[6] = \
        T[0], T[1], T[2], T[3], T[4], T[5], T[6], T[7], T[8]

    X[8], X[7], X[6], Y[6], Y[3], Y[0], Z[2], Z[5], Z[8], W[0], W[1], W[2] = Y[6], Y[3], Y[0], Z[2], Z[5], Z[8], W[0], W[1], W[2], X[8], X[7], X[6]


def print_color():
    for x in range(3):
        pr = ''
        for y in range(3):
            pr += U[x*3+y]
        print(pr)


for i in range(n):
    U = ['w'] * 9
    D = ['y'] * 9
    F = ['r'] * 9
    B = ['o'] * 9
    L = ['g'] * 9
    R = ['b'] * 9
    for t in turns[i]:
        side = t[0]
        direction = t[1]
        rotate(side)
        if direction == '-':
            rotate(side)
            rotate(side)

    print_color()

