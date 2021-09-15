def dfs(row, num):
    global answer, film

    if num >= answer:
        return

    for col in range(w):
        success = False
        length = 1
        for depth in range(1, d):
            if film[depth][col] == film[depth-1][col]:
                length += 1
            else:
                length = 1
            if length >= k:
                success = True
                break

        if not success:
            break

    else:
        answer = min(answer, num)
        return

    if row == d:
        return

    temp_film = [[0]*w for _ in range(d)]
    for i in range(d):
        temp_film[i] = list(film[i])

    dfs(row+1, num)
    for i in range(d):
        film[i] = list(temp_film[i])

    if film[row].count(0) < w:
        film[row] = [0] * w
        dfs(row+1, num+1)
    for i in range(d):
        film[i] = list(temp_film[i])

    if film[row].count(1) < w:
        film[row] = [1] * w
        dfs(row+1, num+1)

    for i in range(d):
        film[i] = list(temp_film[i])


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    d, w, k = map(int, input().split())
    film = []
    for i in range(d):
        film.append(list(map(int, input().split())))

    answer = d
    dfs(0, 0)
    print('#'+str(test_case)+' '+str(answer))