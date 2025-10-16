#백준 #20922 겹치는 건 싫어
#투 포인터 알고리즘
from collections import defaultdict

N, K = map(int, input().split())
nums = list(map(int, input().split()))

start, end = 0,0

cnt = defaultdict(int) #수열에 존재하는 각 정수의 개수
ans = 0
while end<N:

     #조건:앞에서부터 end와 동일한 값이 start로 나올때까지 탐색. nums[start]가 나올 때까지 start 증가
    if cnt[nums[end]] >= K:
        cnt[nums[start]] -= 1 #end와 동일한 start의 cnt[nums[start]]를 줄여 K 미만으로 줄임
        start += 1
    #K보다 커지지 않으면, end를 계속 증가하면서 최대 길이(ans) 갱신
    else: 
        cnt[nums[end]] += 1
        end += 1
        ans = max(ans, end-start)

print(ans)