#백준1149 RGB거리
#알고리즘: DP

n = int(input())

dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    a, b, c = map(int, input().split())

    if (i==0):
        dp[i][0] = a
        dp[i][1] = b
        dp[i][2] = c
    else:
        dp[i][0] += min(dp[i-1][1]+a, dp[i-1][2]+a)
        dp[i][1] += min(dp[i-1][0]+b, dp[i-1][2]+b)
        dp[i][2] += min(dp[i-1][0]+c, dp[i-1][1]+c)

print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2]))