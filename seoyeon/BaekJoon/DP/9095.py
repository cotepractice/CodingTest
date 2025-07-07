#백준 #9095 1,2,3 더하기
#DP

T = int(input())

for t in range(T):
    N = int(input())
    dp = [0 for _ in range(N+1)] 
    
    for i in range(1,N+1):
        if i==1:
            dp[i]=1
        elif i==2:
            dp[i]=2
        elif i==3:
            dp[i]=4
        else:
            dp[i]=dp[i-1]+dp[i-2]+dp[i-3] #i가 가질 수 있는 경우의 수는 "i-1의 경우의 수" + "i-2의 경우의 수" + "i-3의 경우의 수'
    print(dp[N])