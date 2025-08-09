import heapq

N,M = map(int,input().split())
connections = [[] for _ in range(N)] #connections[a]=[b1,b2,..] #a->b1,b2
connections_n = [0 for _ in range(N)] #먼저 푸는 것이 좋은 개수

for m in range(M):
    a,b = map(int,input().split()) #a->b
    connections[a-1].append(b-1)
    connections_n[b-1]+=1

heap = []
heapq.heapify(heap)

visited=[False for _ in range(N)]
answer = []
for i in range(N):
    if connections_n[i]==0:
        heapq.heappush(heap,i)

while heap:
    x = heapq.heappop(heap)
    answer.append(x+1)
    visited[x]=True

    lst = connections[x]
    lst.sort()

    for next in lst:
        connections_n[next] -= 1
        if visited[next]==False and connections_n[next]==0:
            visited[next]=True
            heapq.heappush(heap,next)

print(*answer)
