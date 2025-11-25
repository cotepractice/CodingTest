#백준 #13549 숨바꼭질3

import heapq

N, K = map(int,input().split())

dp = [float("inf") for _ in range(100001)]

heap = []
heapq.heapify(heap)

heapq.heappush(heap, [0,N])
dp[N]=0

while heap:
    t,x = heapq.heappop(heap)
    
    if dp[x]<t:
        continue

    #뛰기
    if 0<=x*2<=100000 and t<dp[2*x]:
        dp[x*2]=t
        heapq.heappush(heap,[t,2*x])

    #걷기
    if 0<=x+1<=100000 and t+1<dp[x+1]:
        dp[x+1]=t+1
        heapq.heappush(heap,[t+1,x+1]) #앞으로 이동
    if 0<=x-1<=100000 and t+1<dp[x-1]:
        dp[x-1]=t+1
        heapq.heappush(heap,[t+1,x-1]) #뒤로 이동



print(dp[K])