#백준 #5014 스타트링크

#Dijkstra
#1)visited: 방문 처리
#2)dp: 최소 횟수 저장

import heapq

#F:총 F층, S:현재, G:목적지
#U,D 위로 U, 아래로 D
F, S, G, U, D = map(int,input().split())

heap=[]
heapq.heapify(heap)
heapq.heappush(heap,[0,S]) #[횟수, 현재 층]
visited = set()
visited.add(S)
dp = [float("inf") for _ in range(F+1)]
dp[S]=0

while heap:
    cnt,current = heapq.heappop(heap)

    for next in (current+U,current-D):
        # 방문 처리
        if next in visited:
            continue
        # 범위 내 존재해야 함
        # 방문한 적 없으면 방문 처리 후 삽입
        if 0<next<F+1:
            visited.add(next)
            dp[next]=cnt+1
            heapq.heappush(heap,[cnt+1,next])

if dp[G]==float("inf"):
    print("use the stairs")
else:
    print(dp[G])