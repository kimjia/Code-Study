from itertools import combinations

n = int(input())
members = []
for i in range(n):
    members.append(i)

S = []
for _ in range(n):
    S.append(list(map(int, input().split())))

start = []
link = []
answer = 100 * n


def dfs(i):
    global start, link, answer
    if len(start) > n//2 or len(link) > n//2:
        return
    if len(start) == n//2 and len(link) == n//2:
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
        return

    start.append(i)
    dfs(i+1)
    start.pop()
    link.append(i)
    dfs(i+1)
    link.pop()


dfs(0)
print(answer)
