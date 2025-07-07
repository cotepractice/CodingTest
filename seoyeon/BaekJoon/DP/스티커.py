#백준9465 스티커
#n==1, n==2인 경우 하지 않으면 런타임에러(Index Error) 발생. for문 안의 index가 존재하도록 유의할것!

import sys

T = int(input())

for _ in range(T):
    n = int(input())

    lst = []
    int_lst = []
    dp = [[0 for _ in range(n)] for _ in range(2)]  #dp는 해당 단계까지의 최댓값

    input = sys.stdin.readline
    for i in range(2):
        m = input().strip().split()
        lst.append(m)

    dp[0][0] = int(lst[0][0])
    dp[1][0] = int(lst[1][0])
    if (n == 1):
        print(max(dp[0][0], dp[1][0]))
        continue
    dp[0][1] = dp[1][0] + int(lst[0][1])
    dp[1][1] = dp[0][0] + int(lst[1][1])    
    
    if (n == 2):
        print(max(dp[0][n-1], dp[1][n-1]))
        continue

    for j in range(2,n):
        for i in range(2):
            if (i==0):
                dp[i][j] = max(dp[i+1][j-1]+int(lst[i][j]), dp[i][j-2]+int(lst[i][j]), dp[i+1][j-2]+int(lst[i][j]))
            else:
                dp[i][j] = max(dp[i-1][j-1]+int(lst[i][j]), dp[i][j-2]+int(lst[i][j]), dp[i-1][j-2]+int(lst[i][j]))
    
    print(max(dp[0][n-1], dp[1][n-1]))