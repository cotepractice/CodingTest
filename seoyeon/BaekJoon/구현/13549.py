#백준 #13549 숨바꼭질3
#Dijkstra

from collections import deque

N,K = map(int,input().split())
visited = [-1 for _ in range(100001)]

Q = deque([])
Q.append(N)
visited[N]=0

while Q:
    index = Q.popleft()
    
    if index==K:
        break

    for next_index in (2*index,index-1,index+1): #Check. 2*index -> index-1 -> index+1 순서로 진행
        if 0<=next_index<100001 and visited[next_index]==-1:
            if next_index==2*index:
                visited[next_index]=visited[index]
                Q.append(next_index)
            else:
                visited[next_index]=visited[index]+1
                Q.append(next_index)

print(visited[K])