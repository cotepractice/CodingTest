#백준 #2293 동전1

#n가지 종류 동전을 통해 k원 만들기
#해당 종류 동전은 무제한 사용 가능
n, k = map(int,input().split())
coins = [0 for _ in range(n)]

for i in range(n):
    c = int(input())
    coins[i]=c

#dp[n]=m. n원 만드는 경우의 수 m
dp = [0 for _ in range(k+1)]
dp[0]=1 #0원을 만들 수 있는 경우의 수 1

for coin in coins:
    for j in range(coin, k+1):
        if j-coin>=0:
            dp[j]=dp[j]+dp[j-coin]

print(dp[k])
