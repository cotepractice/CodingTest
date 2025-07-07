#백준 #1806 부분합
from collections import defaultdict

N, S = map(int, input().split())

nums = list(map(int, input().split()))

start,end = 0,0

sum = 0
ans = float("inf")
while True:
    
    #합이 S보다 크면 start 증가 (길이 감소)
    if sum>=S:
        ans = min(ans, end-start)
        #print(start,end, sum,ans) #start부터 end-1까지의 합이 sum
        sum -= nums[start]
        start += 1
    
    elif end == N:
        break

    #합이 S보다 작으면 end 증가 (길이 증가)
    else:
        sum += nums[end]
        end += 1


if ans==float("inf"):
    print(0)
else:          
    print(ans)