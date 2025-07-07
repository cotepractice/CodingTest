# 백준12865 평범한 배낭

n, k = map(int, input().split())    #n은 물건 수, k는 버틸수있는 무게

bag = [[0,0]]
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]  #가로 k, 세로 n

for i in range(n):
    W, V = map(int, input().split())
    bag.append((W,V))

for i in range(1, n+1):
    for j in range(1, k+1):
        w = bag[i][0]
        v = bag[i][1]

        if (j<w):   #물건이 버틸수있는무게보다 큰 경우
            dp[i][j] = dp[i-1][j]
        else:       #넣을 수 있는 경우, 넣던가 넣지 않던가 선택
            dp[i][j] = max(dp[i-1][j], v+dp[i-1][j-w])

print(dp[n][k])