#백준 #1463 1로 만들기

# #1. 시간초과
# N = int(input())

# dp = [float("inf") for _ in range(N+1)]

# def solv(num,cnt):
#     dp[num] = min(dp[num],cnt)

#     if num<=1:
#         return

#     if num%3==0:
#         solv(num//3,cnt+1)
#     if num%2==0:
#         solv(num//2,cnt+1)
#     solv(num-1,cnt+1)

# solv(N,0)
# print(dp[1])

#2. DP
N = int(input())
dp = [float("inf") for _ in range(1000001)] #dp[x].x에서 1을 만들 수 있는 최솟값
#직접 생각
dp[1]=0
dp[2]=1
dp[3]=1

for i in range(4,N+1):
    dp[i] = min(dp[i],dp[i-1]+1)
    if i%3==0:
        dp[i]=min(dp[i],dp[i//3]+1)
    if i%2==0:
        dp[i]=min(dp[i],dp[i//2]+1)
print(dp[N])