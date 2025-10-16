#백준 #5972 택배 배송
#20:13-20:27

#Dijkstra
from collections import deque
import heapq

N,M=map(int,input().split())
connections = [[] for _ in range(N)]

for m in range(M):
    a,b,c = list(map(int,input().split()))
    connections[a-1].append([b-1,c])
    connections[b-1].append([a-1,c])

visited = set()
distance = [float("inf") for _ in range(N)]

heap = []
heapq.heapify(heap)
heapq.heappush(heap, [0,0]) #[cost,index]
distance=[float("inf") for _ in range(N)]
distance[0]=0

while heap:
    cost,idx = heapq.heappop(heap)

    for next,next_cost in connections[idx]:
        all_cost=cost+next_cost
        if all_cost<distance[next]:
            distance[next]=all_cost
            heapq.heappush(heap,[all_cost,next])

print(distance[N-1])

# 엣지 비용이 다른 경우에는 꼭 heap 사용해야 함! 아래는 BFS로, 가중치가 모두 같은 경우 해당
# Q = deque()
# Q.append([0,0]) #[cost,index]
# distance[0]=0
# visited.add(0)

# while Q:
#     cost,idx = Q.popleft()

#     for next,next_cost in connections[idx]:
#         all_cost = cost+next_cost
#         if all_cost<distance[next] and next not in visited:
#             visited.add(next)
#             distance[next]=all_cost
#             Q.append([all_cost,next])