#백준 #10026 적록색약
#그래프 문제
#00:55

import sys
from collections import deque

T = int(input())

graph1 = [[0 for _ in range(T)] for _ in range(T)]
graph2 = [[0 for _ in range(T)] for _ in range(T)]

for i in range(T):
    graph1[i] = list(input())
    
#리스트 복사
for i in range(T):
    for j in range(T):
        graph2[i][j] = graph1[i][j]

def bfs(graph,i,j,alpha):
    Q = deque()
    Q.append((i,j))
    graph[i][j] = 0

    while Q:
        x, y = Q.popleft()

        dx = [0,0,-1,1]
        dy = [-1,1,0,0]
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if (0<=nx<T and 0<=ny<T):
                if (graph[nx][ny] == alpha):
                    graph[nx][ny] = 0
                    Q.append((nx,ny))
    return 
#기존 사람의 경우
cnt1 = 0
for i in range(T):
    for j in range(T):
        if (graph1[i][j] != 0):
            alpha = graph1[i][j]
            bfs(graph1, i,j,alpha)
            cnt1 += 1
            #print(graph)

#적록색약인 경우
#1. graph 변경
for i in range(T):
    for j in range(T):
        if (graph2[i][j] == "R"):
            graph2[i][j] = "G"

#2. count
cnt2 = 0
for i in range(T):
    for j in range(T):
        if (graph2[i][j] != 0):
            alpha = graph2[i][j]
            bfs(graph2,i,j,alpha)
            cnt2 += 1
            #print(graph)

print(cnt1, cnt2)