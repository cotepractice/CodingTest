#15:58-17:23
#연결요소: 그래프 내에서 서로 도달 가능한 정점의 덩어리

# #[1] DFS
# import sys
# sys.setrecursionlimit(10000) #RecursionError 해결:Python이 정한 최대 깊이를 더 깊게 변경

# input = sys.stdin.readline #시간초과 해결

# N, M = map(int,input().split())

# edges = [[] for _ in range(N)]
# visited = [False for _ in range(N)]

# def dfs(edges,i,visited):
#     next_lst = edges[i]
#     for next in next_lst:
#         if visited[next]==False:
#             visited[next]=True
#             dfs(edges,next,visited)

# for _ in range(M):
#     u, v = map(int,input().split())
#     #양방향
#     edges[u-1].append(v-1)
#     edges[v-1].append(u-1)

# ans = 0

# for i in range(N):
#     if visited[i]==False:
#         visited[i]=True
#         dfs(edges,i,visited)
#         ans += 1

# print(ans)

#[2] BFS
import sys
from collections import deque

sys.setrecursionlimit(10000)

input = sys.stdin.readline

N, M = map(int,input().split())

edges = [[] for _ in range(N)]
visited = [False for _ in range(N)]

for _ in range(M):
    u, v = map(int,input().split())
    #양방향
    edges[u-1].append(v-1)
    edges[v-1].append(u-1)

def bfs(idx,visited):
    Q = deque()
    Q.append(idx)

    while Q:
        x = Q.popleft()
        for next in edges[x]:
            if visited[next]==False:
                visited[next]=True
                Q.append(next)

ans = 0

for i in range(N):
    if visited[i]==False:
        visited[i]=True
        bfs(i,visited)
        ans += 1
        
print(ans)