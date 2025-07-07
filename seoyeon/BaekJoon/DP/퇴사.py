#백준 #14501 퇴사
#DP
#16:37-17:10

n = int(input())

lst = [0 for _ in range(n)]
dp = [0 for _ in range(n+1)]    #날짜 초과하는 경우 기본값인 0이 필요하므로 n+1까지

for i in range(n):
    t, p = map(int, input().split())

    lst[i] = (t,p)

#Top-Down: 거꾸로 뒤에서 계산
for i in range(n-1,-1,-1):
    #날짜를 넘는 경우 dp[n+1] 값 가져오기
    if (i+lst[i][0] > n):
        dp[i] = dp[i+1]
    #i일에 상담을 하는 것과 상담 안 하는 것 중 큰 값 선택
    #상담 안 하는 것: dp[i+1]
    #상담하는 것: lst[i][1] + dp[i+lst[i][0]] <-상담하는 날짜동안에는 상담 못하므로 이전 dp값과 현재 상담 가치의 합
    else:
        dp[i] = max(dp[i+1], lst[i][1] + dp[i+lst[i][0]])

print(dp[0])