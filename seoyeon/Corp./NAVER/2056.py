#백준 #2056 작업
#위상정렬

N = int(input())

dp = [0 for _ in range(N+1)]

for i in range(1, N+1):
    lst = list(map(int,input().split()))
    work, count, pre = lst[0],lst[1],lst[2:]
    dp[i] = work
    for j in pre:
        dp[i] = max(dp[i], dp[j]+work)
print(max(dp))