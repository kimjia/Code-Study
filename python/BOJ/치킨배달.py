from itertools import combinations

n, m = map(int, input().split())

house = []
chicken = []

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            house.append([i+1, j+1])
        elif data[j] == 2:
            chicken.append([i+1, j+1])

combination_result = list(combinations(chicken, m))

answer = 2 * n * n

for comb in combination_result:
    dist_sum = 0
    for h in house:
        dist = 2 * n
        for c in comb:
            new_dist = abs(c[0] - h[0]) + abs(c[1] - h[1])
            if new_dist < dist:
                dist = new_dist
        # dist = 치킨거리
        dist_sum += dist
        if dist_sum > answer:
            continue
    if dist_sum < answer:
        answer = dist_sum

print(answer)
