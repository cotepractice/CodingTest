#백준 #11779 최소비용 구하기2
#다익스트라

import heapq

def solv(start):
    global distance,prev_node

    heap = [[0,start]] #[cost,index]
    heapq.heapify(heap)
    distance[start]=0

    while heap:
        cur_cost,cur_city = heapq.heappop(heap)

        #현재 위치의 가중치 cur_cost가 distance[cur_city]보다 큰 경우 패스
        if distance[cur_city] < cur_cost:
            continue
        #현재 위치에서 갈 수 있는 모든 거리 탐색
        for next_cost,next_city in cross[cur_city]:
            cost = cur_cost+next_cost
            #다음으로 갈 위치의 cost가 distance[next_city]보다 작은 경우만 아래 동작
            if cost < distance[next_city]:
                distance[next_city]=cost #distance 업데이트
                prev_node[next_city] = cur_city #이동 순서 출력을 위해 이전 노드 저장
                heapq.heappush(heap,[cost,next_city]) #다음 위치를 탐색하기 위해 heapq에 저장


N = int(input())
M = int(input())
cross = [[] for _ in range(N)] #cross[x]=[[cost,dest],..]
distance = [float("inf") for _ in range(N)] #distance[i]는 i까지의 최소 거리
prev_node = [0 for _ in range(N)] #순서 출력을 위한 리스트

for m in range(M):
    a,b,c = list(map(int,input().split()))
    cross[a-1].append([c,b-1]) 

start,end = map(int,input().split())

solv(start-1)

print(distance[end-1])

#이동 순서 출력 로직
path = [end-1]
now = end-1
while now != start-1:
    now = prev_node[now]
    path.append(now)
path.reverse()

print(len(path))
for i in range(len(path)):
    print(path[i]+1,end=" ")