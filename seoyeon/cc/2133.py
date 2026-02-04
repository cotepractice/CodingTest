#백준 #2133 타일채우기

n = int(input())

dp = [0]*(n+1)

#홀수인 경우는 항상 0
if n % 2 != 0:
    print(0)
#n=2인 경우 가능한 경우의 수 3
#n=4인 경우 가능한 경우의 수 2
else:
    dp[2] = 3
    
    for i in range(4, n+1, 2):
        dp[i] = dp[i-2] * 3 + 2
        for j in range(2, i-2, 2):
            dp[i] += dp[j] * 2

    print(dp[n])