#백준 #10844 쉬운 계단 수
#14:19-15:11

#1. 시간복잡도 O(N*(10*2*N)).1<=N<=100 -> 시간초과 발생
#구현

# N = int(input())
# dp = [0 for _ in range(N+1)]

# def solv(k,lst):
#     #종결 조건
#     if len(lst)==k:
#         dp[k] += 1
#         return
    
#     last = lst[-1]
#     tmp1,tmp2 = lst[:],lst[:]
#     #인접한 모든 차이가 1
#     if 0<=last+1<=9:
#         tmp1.append(last+1)
#         solv(N,tmp1)
#     if 0<=last-1<=9:
#         tmp2.append(last-1)
#         solv(N,tmp2)

# #j:1~9까지의 수. 0으로 시작하는 수는 계단 수가 아님
# for j in range(1,10):
#     lst = [j]
#     solv(N,lst)
# print(dp[N])

#2. 시간복잡도 O(N)
#DP

N = int(input())

dp = [[0 for _ in range(10)] for _ in range(N)] #dp[i][j].i는 i-1 길이를 의미하는 자릿수, j는 끝나는 수

dp[0] = [0,1,1,1,1,1,1,1,1,1] #dp[0]은 N=1인 경우의 경우의 수. 0은 올 수 없으므로 dp[0][0]=0

for n in range(1,N):
    #k==0 or k==9인 경우 들어올 수 있는 경우가 하나밖에 없음
    dp[n][0]=dp[n-1][1]
    dp[n][9]=dp[n-1][8]
    #1<=k<=8인 경우 들어올 수 있는 경우의 수가 두개 (k-1,k+1)
    for k in range(1,9):
        dp[n][k] = dp[n-1][k-1]+dp[n-1][k+1]

print(sum(dp[N-1])%1000000000)