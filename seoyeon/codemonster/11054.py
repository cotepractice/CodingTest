#백준 #11054 가장 긴 바이토닉 부분 수열

N = int(input())
A = list(map(int,input().split()))

increase_dp = [1 for _ in range(N)] #increase_dp[i]는 i까지 증가하는 수열 개수
decrease_dp = [1 for _ in range(N)] #decrease_dp[i]는 i까지 감소하는 수열 개수

for i in range(N):
    for j in range(i):
        #A[i]>A[j]인 경우, increase_dp[j]는 j 인덱스까지 증가하는 수열 개수에 1 증가
        if A[i]>A[j]:
            increase_dp[i] = max(increase_dp[i], increase_dp[j]+1)

for i in range(N-1,-1,-1):
    for j in range(N-1,i,-1):
        if A[i]>A[j]:
            decrease_dp[i] = max(decrease_dp[i], decrease_dp[j]+1)

dp = [0 for _ in range(N)]

for i in range(N):
    dp[i] = increase_dp[i]+decrease_dp[i]-1 #가장 큰 수가 중복 increase+decrease)
print(max(dp))