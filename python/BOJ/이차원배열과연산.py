r, c, k = map(int, input().split())
A = []
for _ in range(3):
    data = list(map(int, input().split()))
    A.append(data)

r -= 1
c -= 1


def calculate():
    row, col = len(A), len(A[0])
    max_row = 0
    for i in range(row):

        A[i] = sorted(A[i])
        new_row = []
        num = 1
        last = A[i][0]
        for j in range(col-1):
            if A[i][j] != A[i][j + 1]:
                if A[i][j] != 0:
                    new_row.append([num, A[i][j]])
                last = A[i][j+1]
                num = 1
            else:
                num += 1
        if last != 0:
            new_row.append([num, last])

        A[i] = []
        if new_row:
            new_row.sort()
            for a, b in new_row:
                A[i].append(b)
                A[i].append(a)
        max_row = max(max_row, len(A[i]))

    for i in range(row):
        while len(A[i]) < max_row:
            A[i].append(0)


time = 0
while time <= 100:
    row, col = len(A), len(A[0])
    if 0 <= r < row and 0 <= c < col and A[r][c] == k:
        print(time)
        break

    if row >= col:
        calculate()

    else:
        A = list(zip(*A))  # 시계방향 회전
        A = list(zip(*A))
        A = list(zip(*A))
        calculate()
        A = list(zip(*A))

    time += 1

else:
    print(-1)
