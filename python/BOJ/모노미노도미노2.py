n = int(input())
block_list = []
for _ in range(n):
    block_list.append(list(map(int, input().split())))

green = [[0] * 4 for _ in range(6)]
blue = [[0] * 4 for _ in range(6)]
result = 0

for t, x, y in block_list:
    # locate green
    if t == 1:
        nx = 5
        for r in range(1, 6):
            if green[r][y]:
                nx = r - 1
                break
        green[nx][y] = 1
    elif t == 2:
        nx = 5
        for r in range(1, 6):
            if green[r][y] or green[r][y+1]:
                nx = r - 1
                break
        green[nx][y] = 1
        green[nx][y+1] = 1
    else:
        nx = 5
        for r in range(1, 6):
            if green[r][y]:
                nx = r - 1
                break
        green[nx][y] = 1
        green[nx - 1][y] = 1

    # delete green
    index = 5
    while index >= 0:
        if sum(green[index]) == 4:
            green.pop(index)
            green.insert(0, [0] * 4)
            result += 1
        else:
            index -= 1

    if sum(green[0]) != 0:
        green.pop()
        green.insert(0, [0] * 4)
    if sum(green[1]) != 0:
        green.pop()
        green.insert(0, [0] * 4)

    # locate blue
    if t == 1:
        nx = 5
        for r in range(1, 6):
            if blue[r][x]:
                nx = r - 1
                break
        blue[nx][x] = 1
    elif t == 3:
        nx = 5
        for r in range(1, 6):
            if blue[r][x] or blue[r][x+1]:
                nx = r - 1
                break
        blue[nx][x] = 1
        blue[nx][x+1] = 1
    else:
        nx = 5
        for r in range(1, 6):
            if blue[r][x]:
                nx = r - 1
                break
        blue[nx][x] = 1
        blue[nx - 1][x] = 1

    # delete blue
    index = 5
    while index >= 0:
        if sum(blue[index]) == 4:
            blue.pop(index)
            blue.insert(0, [0] * 4)
            result += 1
        else:
            index -= 1

    if sum(blue[0]) != 0:
        blue.pop()
        blue.insert(0, [0] * 4)
    if sum(blue[1]) != 0:
        blue.pop()
        blue.insert(0, [0] * 4)


num = 0
for i in range(6):
    num += sum(blue[i])
    num += sum(green[i])
print(result)
print(num)
