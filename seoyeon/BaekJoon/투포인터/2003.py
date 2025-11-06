#백준 #2003 수들의 합2

#8:46-9:10

N,M=map(int,input().split())
a=list(map(int,input().split()))
dp=[0 for _ in range(N+1)]

for i in range(1,N+1):
    dp[i]=dp[i-1]+a[i-1]

start,end = 1,1 #start,end 포함
sum=dp[1]
cnt=0

while start<=end:

    #종결조건
    if end==N+1:
        break

    sum=dp[end]-dp[start-1]

    #sum이 M인 경우, cnt 증가&start와 end 업데이트(start와 end가 같은 수인 경우 end도 함께 업데이트)
    if sum==M:
        cnt+=1
        if start!=end:
            start+=1
        else:
            start+=1
            end+=1
    
    #sum이 M 미만인 경우, end 증가(범위 벗어나면 종결)
    elif sum<M:
        end+=1
    
    #sum이 M 초과인 경우, start 증가
    else:
        if start!=end:
            start+=1
        else:
            start+=1
            end+=1

print(cnt)