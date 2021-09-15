N, L = map(int, input().split())
world = []
for _ in range(N):
    world.append(list(map(int, input().split())))
count = 0


def count_road(direction):  # 지나갈 수 있는 길의 개수 세기
    global count
    for i in range(N):
        length = 1  # 높이가 같고, 경사로가 놓이지 않은 칸 중에 (j-1번째 칸까지) 연속된 칸의 개수
        need_slope = False
        for j in range(1, N):  # j번째 칸과 j-1번째 칸의 높이 비교
            if direction == 0:  # 가로방향
                sub = world[i][j] - world[i][j-1]
            else:  # 세로방향
                sub = world[j][i] - world[j-1][i]
            if sub > 1 or sub < -1:  # 이웃한 칸의 높이가 2 이상 차이나는 경우 종료
                break
            else:
                if need_slope and length >= L:  # 경사로를 설치할 수 있는 경우에 경사로 설치
                    need_slope = False
                    length = 0
                if sub == 0:  # 같은 높이의 칸이 몇개인지 기록
                    length += 1
                elif sub == 1:  # j번째 칸이 j-1번째 칸보다 1 높은 경우
                    if need_slope or length < L:  # 2-1-2처럼 이전에 높이가 한칸 낮아졌지만 경사로가 설치되지 않았거나,
                        break                     # 연속된 낮은 칸수가 적어서 경사로를 설치할 수 없는 경우 종료
                    length = 1
                elif sub == -1:  # j번째 칸이 j-1번째 칸보다 1 낮은 경우
                    if need_slope:  # 마찬가지로 이전에 높이가 한칸 낮아졌지만 경사로가 설치되지 않은 경우에 종료
                        break
                    need_slope = True   # 높->낮 높이변화가 일어난 경우 이후에 경사로 설치가 필요함
                    length = 1

            if j == N - 1 and ((not need_slope) or (need_slope and length == L)):   # j=N-1까지 종료되지 않은 경우에, 마지막에 경사로가 필요하면 설치
                count += 1


count_road(0)
count_road(1)
print(count)
