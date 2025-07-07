#백준 #1463 1로 만들기
#DP

N = int(input())

dp = [0 for _ in range(N+1)]

#시작: 1은 0. 2부터 시작
#종료: 최종적으로 원하는 값이 N이므로 N+1까지
for i in range(2,N+1):
    #1 증가
    dp[i]=dp[i-1]+1
    #1 증가와 2 나누기 중 최솟값
    if i%2==0:
        dp[i] = min(dp[i],dp[i//2]+1)
    #앞의 계산과 3 나누기 중 최솟값
    if i%3==0:
        dp[i] = min(dp[i],dp[i//3]+1)

print(dp[N])