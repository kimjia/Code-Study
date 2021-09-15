from collections import deque

n, left, right = map(int, input().split())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))

visited = [[False] * n for _ in range(n)]
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
answer = 0


def bfs(ox, oy):  # ox, oy: 한 연합에서 국경선이 열리는 최초의 국가
    global move
    union = []  # (ox, oy)로부터 시작된 연합에 속하는 국가들의 좌표를 저장하는 리스트
    count = 1  # 연합에 속한 국가의 수
    total = A[ox][oy]  # 연합에 속한 국가들의 총 인구수
    q = deque()  # 방문할 국가들의 큐
    q.append([ox, oy])

    while q:
        x, y = q.pop()

        if visited[x][y]:  # 한 번 방문한 국가는 다시 방문하지 않음
            continue
        else:
            visited[x][y] = True

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx = x + dx  # 동서남북에 있는 국가들과 인구수를 비교하여 국경선을 열지 결정
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                sub = abs(A[x][y] - A[nx][ny])
                if left <= sub <= right and [nx, ny] not in union:  # 조건을 만족하는 국가와의 국경선 열기
                    union.append([nx, ny])
                    count += 1
                    total += A[nx][ny]
                    q.append([nx, ny])  # 그 국가와 이웃한 국가들도 방문

    if union:  # 만약 (ox, oy)로부터 시작하는 연합에 속하는 국가가 하나라도 존재하면
        population = int(total / count)
        A[ox][oy] = population
        for cx, cy in union:
            A[cx][cy] = population  # 해당 연합에 속하는 모든 국가의 인구수를 평균치로 바꿔줌
        move += 1
        return True
    else:  # 연합에 속하는 국가가 없으면 바로 함수 종료
        return False


while True:
    move = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j)  # 모든 나라 한번씩 방문

    visited = [[False] * n for _ in range(n)]
    if move == 0:  # 국경선이 하나도 열리지 않았으면 종료
        break
    answer += 1

print(answer)
