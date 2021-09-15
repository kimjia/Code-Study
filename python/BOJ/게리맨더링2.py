n = int(input())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))

d = []
for i in range(1, n):
    d.append(i)
answer = 100000

for d1 in range(1, n-1):
    for d2 in range(1, n-d1):
        for x in range(n-d1-d2):
            for y in range(d1, n-d2):
                population = [0, 0, 0, 0, 0]
                visited = [[False] * n for _ in range(n)]
                visited[x][y] = True
                population[4] += A[x][y]
                visited[x+d1+d2][y+d2-d1] = True
                population[4] += A[x+d1+d2][y+d2-d1]
                q = []
                for i in range(1, d1+1):
                    q.append([x+i, y-i])
                    q.append([x+d2+i, y+d2-i])
                q.pop()
                for i in range(1, d2+1):
                    q.append([x+i, y+i])
                    q.append([x+d1+i, y-d1+i])
                q.pop()
                q.sort(reverse=True)

                while q:
                    x1, y1 = q.pop()
                    x2, y2 = q.pop()
                    while y1 <= y2:
                        visited[x1][y1] = True
                        population[4] += A[x1][y1]
                        y1 += 1

                for r in range(n):
                    for c in range(n):
                        if visited[r][c]:
                            continue
                        if r < x + d1 and c <= y:
                            population[0] += A[r][c]
                        elif r <= x + d2 and y < c <= n-1:
                            population[1] += A[r][c]
                        elif x+d1 <= r <= n-1 and c < y-d1+d2:
                            population[2] += A[r][c]
                        else:
                            population[3] += A[r][c]

                answer = min(answer, max(population) - min(population))

print(answer)