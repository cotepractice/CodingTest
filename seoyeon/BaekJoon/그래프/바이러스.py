#백준 #2606 바이러스
#그래프
#DFS 사용 => 양방향 연결인지 단방향 연결인지 확인

import sys
from collections import deque

n = int(input())
T = int(input())
graph = [[] for _ in range(n)]
visited = [False for _ in range(n)]

for i in range(T):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)  #컴퓨터 node를 1~n까지가 아닌 0~(n-1)까지
    graph[b-1].append(a-1)  #"양방향"으로 연결

def dfs(graph, v, visited):
    #하나의 v 방문 처리
    visited[v] = True

    #해당 v와 연결된 vertex 방문 처리
    for k in graph[v]:
        if (visited[k] == False):
            visited[k] = True
            dfs(graph,k,visited)

dfs(graph, 0, visited)

cnt = 0
for j in range(1,n):    #index 0은 해당하지 않으므로 1부터
    if visited[j] == True:
        cnt += 1
print(cnt)