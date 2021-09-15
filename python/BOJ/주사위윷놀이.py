board = [[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],
         [10, 13, 16, 19, 25, 30, 35, 40],
         [0, 20, 22, 24, 25, 30, 35, 40],
         [30, 28, 27, 26, 25, 30, 35, 40],
         [0]]

dice = list(map(int, input().split()))

pieces = [[0, 0], [0, 0], [0, 0], [0, 0]]
answer = 0


def dfs(i, result):
    global answer, pieces
    if i == 10:
        answer = max(answer, result)
        return

    moved = []
    for x in range(4):
        if pieces[x] == [4, 0] or pieces[x] in moved:
            continue
        save_x = pieces[x]
        moved.append(save_x)

        overlap, add = move(x, dice[i])
        if not overlap:
            dfs(i+1, result + add)
            pieces[x] = save_x


def move(x, num):  # x 번째 말을 num만큼 이동
    global pieces
    a, b = pieces[x]
    na = a
    nb = b + num
    if nb >= len(board[a]):
        pieces[x] = [4, 0]
        return False, 0

    if a == 0:
        if board[a][nb] == 10:
            na, nb = 1, 0
        elif board[a][nb] == 20:
            na, nb = 2, 1
        elif board[a][nb] == 30:
            na, nb = 3, 0

    for i in range(4):
        if x == i:
            continue
        p, q = pieces[i]
        if [p, q] == [na, nb]:
            return True, 0
        elif board[p][q] == board[na][nb]:
            if board[p][q] != 40 and q != nb:
                continue
            else:
                return True, 0

    pieces[x] = [na, nb]
    return False, board[na][nb]


dfs(0, 0)
print(answer)
