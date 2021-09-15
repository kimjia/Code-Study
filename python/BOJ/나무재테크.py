n, m, k = map(int, input().split())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))
tree = [[[] for _ in range(n)] for _ in range(n)]

tree_count = 0
for _ in range(m):
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)
    tree_count += 1

food = [[5] * n for _ in range(n)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for year in range(k):
    # 봄, 여름, 가을
    temp_tree = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                dead = 0
                tree[i][j].sort()  # 정렬 후 어린 나이부터 양분을 먹음
                for age in tree[i][j]:
                    if age > food[i][j]:
                        dead += age//2
                        tree_count -= 1
                    else:
                        food[i][j] -= age
                        age += 1
                        temp_tree[i][j].append(age)  # 살아있는 나무 정보 저장
                        if age % 5 == 0:  # 번식
                            for a, b in zip(dx, dy):
                                ni, nj = i + a, j + b
                                if 0 <= ni < n and 0 <= nj < n:
                                    temp_tree[ni][nj].append(1)
                                    tree_count += 1

                food[i][j] += dead

    if not tree:
        break

    # 겨울
    for i in range(n):
        for j in range(n):
            food[i][j] += A[i][j]
            tree[i][j] = temp_tree[i][j]


print(tree_count)
