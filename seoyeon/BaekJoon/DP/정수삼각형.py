#백준1932 정수삼각형
#DP문제

n = int(input())

triangle = []
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    triangle.append(input().split())

#dp[i][j]는 i번째 입력받은 수들 중 j 인덱스의 수를 넣었을 때의 합
dp[0][0] = int(triangle[0][0])
idx = 0 #높게 선택된 index

for i in range(1,n):
    for j in range(i+1):
        #처음
        triangle_n = int(triangle[i][j])
        if (j==0):
            dp[i][j] = dp[i-1][j]+triangle_n
        elif (j==i):
            dp[i][j] = dp[i-1][j-1]+triangle_n
        else:
            dp[i][j] = max(dp[i-1][j-1]+triangle_n, dp[i-1][j]+triangle_n)

print(max(dp[n-1]))