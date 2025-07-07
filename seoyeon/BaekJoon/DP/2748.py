#백준 #2748 피보나치 수2

N = int(input())
dp = [0 for _ in range(91)]
dp[1],dp[2]=1,1

for i in range(3,91):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[N])