#백준 #1976 여행 가자
import heapq

N = int(input())
M = int(input())

#citys[i][j]=1은 i와 j 도시가 연결, 0은 연결되지 않음. 양방향
citys = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    citys[i]=list(map(int,input().split()))

plans=list(map(int,input().split()))

connections=[set() for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i==j:
            continue
        if citys[i][j]==1:
            connections[i].add(j)
            connections[j].add(i)

visited=[float("inf") for _ in range(N)]

#순서대로 주어질 때 가능한지
#Dijkstra
result="YES"

def solv():
    heap=[]
    heapq.heapify(heap)
    heapq.heappush(heap,[plans[0]-1,0])
    visited[plans[0]-1]=0

    while heap:
        current,distance = heapq.heappop(heap)

        for next in connections[current]:
            if visited[next]==float("inf"):
                visited[next]=distance+1
                heapq.heappush(heap,[next,distance+1])

solv()
print(visited)
for plan in plans:
    if visited[plan-1]==float("inf"):
        result="NO"
print(result)