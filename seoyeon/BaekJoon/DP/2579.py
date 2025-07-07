#백준 #2579 계단 오르기
#DP

N = int(input())
steps = [0 for _ in range(301)]

for n in range(N):
    steps[n] = int(input())

dp = [0 for _ in range(301)] #계단의 개수는 300 이하.dp[i]는 i까지의 점수의 최댓값

dp[0]=steps[0]
dp[1]=steps[0]+steps[1]
dp[2]=max(steps[0]+steps[2],steps[1]+steps[2]) #

for i in range(3,N):
    dp[i]=max(dp[i-3]+steps[i-1]+steps[i], dp[i-2]+steps[i])

print(dp[N-1])