from itertools import combinations

n = int(input())
members = []
for i in range(n):
    members.append(i)

S = []
for _ in range(n):
    S.append(list(map(int, input().split())))

combination = list(combinations(members, n//2))

answer = 100 * n
for start in combination:
    link = []    #####
    for k in range(n):
        if k not in start:
            link.append(k)
    start_stat = 0
    link_stat = 0
    start_comb = list(combinations(start, 2))
    link_comb = list(combinations(link, 2))
    for x, y in start_comb:
        start_stat += S[x][y]
        start_stat += S[y][x]
    for a, b in link_comb:
        link_stat += S[a][b]
        link_stat += S[b][a]
    sub = abs(start_stat - link_stat)
    answer = min(sub, answer)

print(answer)
