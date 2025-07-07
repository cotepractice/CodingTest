#백준11048 이동하기

n, m = map(int, input().split())

rooms = [[0 for _ in range(m)] for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    rooms[i] = list(map(int, input().split()))


dp[0][0] = rooms[0][0]

for i in range(1,m):
    dp[0][i] = dp[0][i-1] + rooms[0][i]

for j in range(1,n):
    dp[j][0] = dp[j-1][0] + rooms[j][0]

for i in range(1,n):
    for j in range(1,m):
        dp[i][j] = max(dp[i-1][j]+rooms[i][j], dp[i][j-1]+rooms[i][j], dp[i-1][j-1]+rooms[i][j])

print(dp[n-1][m-1])