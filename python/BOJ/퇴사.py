n = int(input())
data = []

for _ in range(n):
    data.append(list(map(int, input().split())))


def counsel(day, money):  # 며칠째, 누적 금액
    if day > n - 1:
        return money
    elif day == n - 1:  # 마지막 날에는 기간 T가 1일인 경우에만 상담
        if data[day][0] <= 1:
            return money + data[day][1]
        else:
            return money

    remaining_day = n - day  # 남은 기간
    if data[day][0] > remaining_day:  # 상담하는데 걸리는 기간이 남은 기간보다 길면 상담 x
        return counsel(day+1, money)
    else:  # 상담을 하는 것과 하지 않는 경우 중 돈을 더 많이 버는 것 선택
        return max(counsel(day+data[day][0], money+data[day][1]), counsel(day+1, money))


print(counsel(0, 0))
