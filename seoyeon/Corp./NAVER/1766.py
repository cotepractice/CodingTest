#백준 #1766 문제집
#위상정렬

import heapq

N,M = map(int,input().split())

connections = [0 for _ in range(N+1)] #connections[k]는 k 풀기 전에 풀어야 하는 문제 개수
graph = [[] for _ in range(N+1)] #graph[x]=[y] x 푼 후 y 풀기. x->y

for m in range(M):
    a,b = map(int,input().split()) #a->b
    connections[b] += 1
    graph[a].append(b)

Q = [] #heapq 사용해 정렬. Q에 있는 값은 풀어도 되는(먼저 풀어야 할 문제가 이미 다 풀린) 문제 인덱스
for i in range(1,N+1):
    if connections[i]==0:
        heapq.heappush(Q,i)
        
result = []

while Q:
    current = heapq.heappop(Q)
    result.append(current)

    for g in range(len(graph[current])):
        next = graph[current][g]
        connections[next] -= 1
        if connections[next]==0:
            heapq.heappush(Q,next)

print(*result)