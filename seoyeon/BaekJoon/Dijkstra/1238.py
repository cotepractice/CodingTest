#백준 #1238 파티
import heapq

# X 제외 도시 -> X로 이동
def dijkstra(start):
    distance = [float("inf") for _ in range(N)] #최단거리

    heap = [[0,start]]
    distance[start] = 0
    heapq.heapify(heap)

    while heap:
        cur_cost,cur_city = heapq.heappop(heap) 
    
        if cur_cost>distance[cur_city]:
            continue
        
        for next_city,next_cost in roads[cur_city]:
            cost = cur_cost+next_cost
            if cost<distance[next_city]:
                distance[next_city]=cost
                heapq.heappush(heap,[cost,next_city])

    return distance[X-1]

# X -> X 제외 도시로 이동
def back(start):
    distance = [float("inf") for _ in range(N)] #최단거리
    heap = [[0,start]]
    distance[start]=0
    heapq.heapify(heap)

    while heap:
        cur_cost,cur_city = heapq.heappop(heap)

        if cur_cost>distance[cur_city]:
            continue

        for next_city,next_cost in roads[cur_city]:
            cost = cur_cost+next_cost
            if cost<distance[next_city]:
                distance[next_city]=cost
                heapq.heappush(heap,[cost,next_city])
    return distance

N,M,X = map(int,input().split()) #N:마을,M:단방향도로개수,X:만날마을인덱스
roads = [[] for _ in range(N)] #roads[s]=[[e,t],...]
ans = [0 for _ in range(N)]  #X제외도시->X
ans_lst = [0 for _ in range(N)] #X->X제외도시

for m in range(M):
    s,e,t = map(int,input().split())
    roads[s-1].append([e-1,t])

for i in range(N):
    
    if i!=X-1:
        ans[i]=dijkstra(i)
    else:
        ans_lst=back(i)


result = [0 for _ in range(N)]

for i in range(N):
    result[i]=ans[i]+ans_lst[i]

print(max(result))