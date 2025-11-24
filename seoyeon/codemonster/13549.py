#백준 #13549 숨바꼭질3

#1. 7% 틀렸습니다
import heapq

N, K = map(int,input().split())

#*범위를 어떻게 설정해야 하는가
dp = [float("inf") for _ in range(200001)]

heap = []
heapq.heapify(heap)

heapq.heappush(heap, [0,N])

while heap:
    t,x = heapq.heappop(heap)
    
    if x==K:
        dp[x]=t
        print(dp[x])
        break
    if x>200001:
        continue
    
    dp[x]=t

    #뛰기
    if t<dp[2*t]:
        heapq.heappush(heap,[t,2*x])

    #걷기
    if 0<=x+1<=100000 and t+1<dp[x+1]:
        heapq.heappush(heap,[t+1,x+1]) #앞으로 이동
    if 0<=x-1<=100000 and t+1<dp[x-1]:
        heapq.heappush(heap,[t+1,x-1]) #뒤로 이동

