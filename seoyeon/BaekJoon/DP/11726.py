#백준 #11726 2xn 타일링
#DP

#2*N 크기의 직사각형을 채우는 방법의 수 
N = int(input())

dp = [0 for _ in range(10001)]

dp[1]=1
dp[2]=2

for i in range(3,10001):
    dp[i] = dp[i-1]+dp[i-2]
print((dp[N])%10007)