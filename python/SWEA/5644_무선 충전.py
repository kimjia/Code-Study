
dx = [0, -1, 0, 1, 0]
dy = [0, 0, 1, 0, -1]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    m, a = map(int, input().split())

    move_A = list(map(int, input().split()))
    move_B = list(map(int, input().split()))
    xA, yA = 0, 0
    xB, yB = 9, 9

    world = [[[] for _ in range(10)] for _ in range(10)]
    for i in range(a):
        y, x, c, p = map(int, input().split())
        for nx in range(x-1-c, x+c):
            for ny in range(y-1-c, y+c):
                if 0 <= nx < 10 and 0 <= ny < 10 and abs(x-1-nx)+abs(y-1-ny) <= c:
                    world[nx][ny].append([p, i])

    for i in range(10):
        for j in range(10):
            if world[i][j]:
                world[i][j].sort(reverse=True)

    answer = 0
    for time in range(m+1):
        # charge
        if not world[xA][yA] and not world[xB][yB]:
            pass
        elif world[xA][yA] and world[xB][yB]:
            max_charge = 0
            for p_A, num_A in world[xA][yA]:
                for p_B, num_B in world[xB][yB]:
                    if num_A == num_B:
                        charge = p_A
                    else:
                        charge = p_A + p_B
                    max_charge = max(max_charge, charge)
            answer += max_charge
        elif world[xA][yA]:
            answer += world[xA][yA][0][0]
        else:
            answer += world[xB][yB][0][0]

        if time == m:
            break

        # move
        xA, yA = xA + dx[move_A[time]], yA + dy[move_A[time]]
        xB, yB = xB + dx[move_B[time]], yB + dy[move_B[time]]

    print('#' + str(test_case) + ' ' + str(answer))