#백준 #1965 상자넣기
#DP

N = int(input())
box = list(map(int,input().split()))
dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if box[i]>box[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))