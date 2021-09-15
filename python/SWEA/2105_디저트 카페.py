dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]


def check(x, y, a, b):
    global answer
    cafe_list = [world[x][y]]
    for move in range(1, a + 1):
        x1, y1 = x + move * dx[0], y + move * dy[0]
        if 0 <= x1 < n and 0 <= y1 < n and world[x1][y1] not in cafe_list:
            cafe_list.append(world[x1][y1])
        else:
            return
    for move in range(1, b + 1):
        x2, y2 = x1 + move * dx[1], y1 + move * dy[1]
        if 0 <= x2 < n and 0 <= y2 < n and world[x2][y2] not in cafe_list:
            cafe_list.append(world[x2][y2])
        else:
            return
    for move in range(1, a + 1):
        x3, y3 = x2 + move * dx[2], y2 + move * dy[2]
        if 0 <= x3 < n and 0 <= y3 < n and world[x3][y3] not in cafe_list:
            cafe_list.append(world[x3][y3])
        else:
            return
    for move in range(1, b):
        x4, y4 = x3 + move * dx[3], y3 + move * dy[3]
        if 0 <= x4 < n and 0 <= y4 < n and world[x4][y4] not in cafe_list:
            cafe_list.append(world[x4][y4])
        else:
            return

    answer = max(answer, 2*(a+b))


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    world = []
    for _ in range(n):
        world.append(list(map(int, input().split())))

    answer = -1
    for x in range(n-1):
        for y in range(1, n-1):
            for a in range(1, n-y):
                for b in range(1, y+1):
                    check(x, y, a, b)

    print('#' + str(test_case) + ' ' + str(answer))
