n = int(input())
data = []

for _ in range(n):
    data.append(list(map(int, input().split())))   # t, p

dp = [0] * (n + 1)

for i in range(n-1, -1, -1):
    dp[i] = max(dp[i+1], data[i][1]+dp[i + data[i][0]]) if data[i][0] + i <= n else dp[i+1]

print(dp[0])
