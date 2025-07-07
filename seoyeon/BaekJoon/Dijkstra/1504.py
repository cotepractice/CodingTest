#백준 #1504 특정한 최단 경로
import heapq

N,E = map(int,input().split())

edges = [[] for _ in range(N)]

for i in range(E):
    a,b,c = map(int,input().split())
    edges[a-1].append([c,b-1])
    edges[b-1].append([c,a-1])

u,v = map(int,input().split())

#start -> end로 가는 최단 거리
def dijkstra(start,end):
    distance = [float("inf") for _ in range(N)] #distance[i].start->i까지의 최단 거리

    Q = []
    heapq.heapify(Q)
    heapq.heappush(Q,[0,start-1])
    distance[start-1]=0

    while Q:
        current_cost, current_idx = heapq.heappop(Q)

        #최소거리이므로 current_cost가 큰 경우 패스
        if distance[current_idx]<current_cost:
            continue
        
        #현재 idx에서 넘어갈 수 있는 모든 idx 체크
        for next_cost, next_idx in edges[current_idx]:
            cost = next_cost+distance[current_idx] #이전 idx에서 현재 idx로 넘어오는 경우
            #이전에서 현재로 넘어오는 경우가 더 작은 경우 계속 진행
            if cost < distance[next_idx]:
                distance[next_idx]=cost
                heapq.heappush(Q,[cost,next_idx])

    return distance[end-1]

#방법1. 1->u->v->N
#방법2. 1->v->u->N

distance1 = dijkstra(1,u)+dijkstra(u,v)+dijkstra(v,N)
distance2 = dijkstra(1,v)+dijkstra(v,u)+dijkstra(u,N)

answer = min(distance1,distance2)

if answer == float("inf"):
    print(-1)
else:
    print(answer)