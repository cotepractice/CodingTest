#백준 #2252 줄 세우기
#NAVER 코테 대비
#위상정렬

from collections import deque

N,M = map(int,input().split())
connections = [0 for _ in range(N)] #들어오는 간선 개수
graph = [[] for _ in range(N)] #graph[a]=[b]이면 a->b

for m in range(M):
    a,b = map(int,input().split())
    graph[a-1].append(b-1) #a->b
    connections[b-1] += 1 #connections는 b에 들어오는 간선 개수

Q = deque() #들어오는 간선의 개수가 0인 경우에만 넣음
result = []

for i in range(N):
    #연결이 없으면 언제든 갈 수 있으므로 Q에 삽입
    if connections[i]==0:
        Q.append(i)

while Q:
    idx = Q.popleft()
    result.append(idx)

    #idx가 사라졌으니 idx->i로 가던 간선이 하나 줄어듬
    for i in graph[idx]:
        connections[i] -= 1
        if connections[i]==0:
            Q.append(i)

for i in result:
    print(i+1,end=" ")