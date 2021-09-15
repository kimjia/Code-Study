
def count(direction):
    global answer
    for k in range(n):
        length = 1
        need_slope = False
        for i in range(n-1):
            if need_slope and length >= x:
                need_slope = False
                length = 0

            if direction == 0:  # 가로
                h1 = world[k][i]
                h2 = world[k][i+1]
            else:  # 세로
                h1 = world[i][k]
                h2 = world[i+1][k]

            if abs(h1 - h2) > 1:
                break

            if h1 == h2:
                length += 1
            else:
                if need_slope:
                    break
                if h1 < h2:
                    if length >= x:
                        length = 1
                    else:
                        break
                if h1 > h2:
                    need_slope = True
                    length = 1

        else:
            if not need_slope or (need_slope and length >= x):
                answer += 1


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, x = map(int, input().split())
    world = []
    for _ in range(n):
        world.append(list(map(int, input().split())))

    answer = 0
    count(0)
    count(1)
    print('#' + str(test_case) + ' '+ str(answer))
