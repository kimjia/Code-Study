n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

# 현재 좌표를 (0, 0)이라 했을 때, 모든 경우의 수에서의 블럭들의 상대위치
tetromino = [  # 모든 경우의 수 (총 19가지)
    [(0, 0), (0, 1), (1, 0), (1, 1)],  # ㅁ
    [(0, 0), (0, 1), (0, 2), (0, 3)],  # ㅡ
    [(0, 0), (1, 0), (2, 0), (3, 0)],  # ㅣ
    [(0, 0), (0, 1), (1, 1), (2, 1)],  # 7
    [(0, 0), (0, 1), (1, 0), (2, 0)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],  # ㄴ
    [(0, 0), (0, 1), (0, 2), (-1, 2)],  #
    [(0, 0), (0, -1), (-1, 0), (0, 1)],  # ㅗ
    [(0, 0), (-1, 0), (1, 0), (0, 1)],  # ㅏ
    [(0, 0), (0, -1), (0, 1), (1, 0)],  # ㅜ
    [(0, 0), (0, -1), (-1, 0), (1, 0)],  # ㅓ
    [(0, 0), (1, 0), (2, 0), (2, 1)],  # L
    [(0, 0), (1, 0), (2, 0), (2, -1)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],  # ㄱ
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (-1, 1), (-1, 2)],
    [(0, 0), (1, 0), (1, -1), (2, -1)],
    [(0, 0), (0, 1), (1, 1), (1, 2)],  # ㄹ
]

answer = 0
for x in range(n):
    for y in range(m):
        for candidate in tetromino:  # 모든 좌표, 모든 경우의수에서 정수 합을 구함
            result = 0
            for move in candidate:
                nx = x + move[0]
                ny = y + move[1]
                if 0 <= nx < n and 0 <= ny < m:
                    result += data[nx][ny]
                else:
                    continue
            answer = max(answer, result)

print(answer)

