#백준 #15989 1,2,3 더하기 4

#1.Greedy. 시간초과
# T = int(input())

# for _ in range(T):
#     N = int(input())
#     ans = 0

#     sum = N
#     n3 = sum//3+1
    
#     for i in range(n3):
#         sum = N-3*i
#         n2 = (sum//2)+1
#         for j in range(n2):
#             sum2 = sum- j*2
#             if sum2>=0:
#                 ans += 1

#     print(ans)

#2. DP

T = int(input())

dp = [1 for _ in range(10001)] #dp[i]는 i를 만들 수 있는 경우의 수

for i in range(2,10001):
    dp[i] += dp[i-2]
for i in range(3,10001):
    dp[i] += dp[i-3]

for _ in range(T):
    N = int(input())
    print(dp[N])