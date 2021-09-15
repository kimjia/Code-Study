n = int(input())
world = []
num_fish = 0

for i in range(n):
    data = list(map(int, input().split()))
    world.append(data)
    for j in range(n):
        if data[j] == 9:
            babyshark = [i, j]  # 아기상어 위치
            world[i][j] = 0
        elif data[j] > 0:
            num_fish += 1  # 물고기 수

eat = 0  # 아기상어가 먹은 물고기 수
babyshark_size = 2  # 아기상어 크기
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def search(x, y):
    global eat, num_fish, babyshark, babyshark_size
    visited = [[1]*n for _ in range(n)]
    q = [(x, y, 0)]
    while q:
        q = sorted(q, key = lambda x:(x[2], x[0], x[1]))
        x, y, dist = q.pop(0)
        visited[x][y] = babyshark_size  # 아기상어가 해당 칸에 방문했을 당시의 크기 저장(같은 크기인 상태로 같은 칸 중복 방문 방지)

        if world[x][y] > babyshark_size:  # 아기상어보다 큰 물고기가 있는 칸은 지나가지 못함
            continue
        if 0 < world[x][y] < babyshark_size:  # 아기상어가 먹을 수 있는 물고기가 있는 칸
            eat += 1
            num_fish -= 1
            if eat == babyshark_size:  # 아기상어 크기만큼 물고기를 먹으면 크기 1 증가
                eat = 0
                babyshark_size += 1
            babyshark = [x, y]  # 아기상어 위치 변경
            world[x][y] = 0
            return dist  # 이동한 거리(시간) 리턴
        if dist > n * n:  # 모든 칸을 다 살펴봤는데 먹을 수 있는 물고기가 없는 경우
            return -1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] < babyshark_size and (nx, ny, dist+1) not in q:
                q.append((nx, ny, dist+1))
    return -1  # q에 원소가 없는경우


count = 0
while num_fish > 0:  # 물고기를 다 먹거나, 더이상 물고기를 먹을 수 없을 때까지 반복
    ret = search(babyshark[0], babyshark[1])
    if ret == -1:
        break
    else:
        count += ret

print(count)