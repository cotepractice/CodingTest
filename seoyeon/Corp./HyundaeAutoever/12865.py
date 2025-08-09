N,K = map(int,input().split()) #N:물건개수, K:최대무게
dp = [[0 for _ in range(K+1)] for _ in range(N+1)] #dp 값은 최대 가치. K+1,N+1로 한 이유는 아무것도 담지 않은 빈 배낭 상태 초기화

items = [[-1,-1] for _ in range(N)]
for n in range(N):
    w,v = map(int,input().split())
    items[n]=[w,v]

for i in range(1,N+1):
    for j in range(1,K+1):
        if j>=items[i-1][0]:
            dp[i][j] = max(items[i-1][1]+dp[i-1][j-items[i-1][0]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
        
print(dp[N][K])