#백준 #1916 최소비용 구하기
#Dijkstra
import heapq

def dijkstra(start):
    global distance

    heap = [[0,start]] #[cost,city_idx]
    heapq.heapify(heap)
    distance[start] = 0
    
    while heap:
        cur_cost,cur_city = heapq.heappop(heap)
        
        #현재 cost가 distance보다 크면 패스 -> 최소 거리 탐색
        if cur_cost > distance[cur_city]:
            continue
        #갈 수 있는 모든 city 탐색
        for next_city,next_cost in bus[cur_city]:
            cost = cur_cost+next_cost
            if cost < distance[next_city]:
                distance[next_city] = cost
                heapq.heappush(heap,[cost,next_city])

N = int(input())
M = int(input())
bus = [[] for _ in range(N)]
distance = [float("inf") for _ in range(N)]

for m in range(M):
    s,e,c = map(int,input().split())
    bus[s-1].append([e-1,c])

start_city, end_city = map(int,input().split())

dijkstra(start_city-1)

print(distance[end_city-1])