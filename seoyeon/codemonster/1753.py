#Dijkstra

import heapq,sys

input = sys.stdin.readline

V, E = map(int,input().split())

v = [i for i in range(V)]
edges = [[] for _ in range(V)] #edges[x]=[[y,w],...] #x->y까지 w만큼 소요
distance = [float("inf") for _ in range(V)]

K = int(input())
distance[K-1]=0

for _ in range(E):
    u,v,w = map(int,input().split()) #u->v
    edges[u-1].append([w,v-1])

def dijkstra(start):

    heap = []
    heapq.heapify(heap)
    heapq.heappush(heap, [0,start])

    #최단거리가 짧은 순서대로 진행
    while heap:
        current_cost, current_index = heapq.heappop(heap)

        if current_cost > distance[current_index]:
            continue

        for next_cost,next_index in edges[current_index]:
            cost = current_cost+next_cost #next는 [y,w]
            if cost<distance[next_index]:
                distance[next_index] = cost
                heapq.heappush(heap,[cost,next_index])

dijkstra(K-1)

for i in range(V):
    if distance[i]==float("inf"):
        print("INF")
    else:
        print(distance[i])
