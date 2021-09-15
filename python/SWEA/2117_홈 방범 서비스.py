def cal():
    global answer
    for x in range(n):
        for y in range(n):
            for k in range(1, n + 2):
                price = k * k + (k - 1) * (k - 1)
                num_house = 0

                for nx in range(max(0, x - (k - 1)), min(n, x + k)):
                    for ny in range(max(0, y - (k - 1)), min(n, y + k)):
                        # print(nx, ny)
                        if abs(nx - x) + abs(ny - y) < k and city[nx][ny] == 1:
                            # print("add")
                            num_house += 1

                profit = num_house * m - price
                # print(x, y, k, num_house, profit)
                if profit >= 0:
                    answer = max(answer, num_house)
                    if answer == total_house:
                        return


T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    city = []
    total_house = 0
    for i in range(n):
        city.append(list(map(int, input().split())))
        total_house += sum(city[i])

    answer = 1
    cal()
    print('#'+str(test_case)+' '+str(answer))

