#백준 #1916 최소비용 구하기

#시간복잡도 O(M log N)
import heapq

N = int(input()) #N:도시개수
M = int(input()) #M:버스개수

#connections[x]=[[c,y],...] x에서 y로 가는 비용 c
connections = [[] for _ in range(N)]

for m in range(M):
    #s:출발도시,e:도착도시,c:버스비용
    s,e,c = map(int,input().split())
    connections[s-1].append([c,e-1])

#fx:출발점,fy:도착점
fx,fy = map(int,input().split())
fx -= 1
fy -= 1

costs = [float("inf") for _ in range(N)]

heap = []
heapq.heapify(heap)
heapq.heappush(heap,[0,fx])
costs[fx]=0

while heap:
    current_c, current_x = heapq.heappop(heap)

    #현재 비용이 costs에 저장된 최소 비용보다 크면 더이상 탐색 X
    if costs[current_x] < current_c:
        continue

    #연결된 다음 도시 탐색
    for next_c, next_x in connections[current_x]:
        cost = current_c + next_c
        if cost<costs[next_x]:
            costs[next_x]=cost
            heapq.heappush(heap,[cost,next_x])

print(costs[fy])