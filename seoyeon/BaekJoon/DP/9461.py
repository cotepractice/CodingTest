#백준 #9461 파도반 수열
#DP

def solv(N):
    dp = [0 for _ in range(101)]
    
    dp[1],dp[2],dp[3] = 1,1,1
    dp[4]=dp[3]+dp[1]
    dp[5]=dp[4]
    dp[6]=dp[5]+dp[3]
    dp[7]=dp[6]+dp[2]
    dp[8]=dp[7]+dp[1]

    #처음 정의: 4~8까지
    for i in range(9,101):
        dp[i]=dp[i-1]+dp[i-5]
    return dp[N]

T = int(input())

for t in range(T):
    N=int(input())
    ans = solv(N)
    print(ans)