#백준 #2293 동전 1
#DP

N,K = map(int,input().split())
coins = []
dp = [0 for _ in range(K+1)] #dp[i]는 i를 만들 수 있는 동전의 경우의 수

for n in range(N):
    coin = int(input())
    coins.append(coin)

dp[0]=1 

for coin in coins:
    for i in range(coin,K+1):
        if i-coin>=0: #coin 크기만큼 이전의 dp와 동일
            dp[i] += dp[i-coin]

print(dp[K])