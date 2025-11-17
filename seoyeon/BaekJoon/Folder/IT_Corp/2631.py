#백준 #2631 줄세우기
N=int(input())
lst=[0]

for n in range(1,N+1):
    lst.append(int(input()))
    

dp = [1 for _ in range(N+1)]

#가장 긴 증가하는 수열 탐색
for i in range(1,N+1):
    for j in range(1,i):
        if lst[j]<lst[i]:
            dp[i]=max(dp[i],dp[j]+1)
print(N-max(dp))