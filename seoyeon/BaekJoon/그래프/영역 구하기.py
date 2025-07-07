#백준 #2583 영역 구하기
#그래프 문제
#bfs로 풀어야할듯

import sys
from collections import deque

input = sys.stdin.readline

n,m,k = map(int, input().split())   #원래 풀던대로 n이 세로(y), m이 가로(x)로 풀 것

graph = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(k):
    a, b, c, d = map(int, input().split())

    for i in range(b,d):
        for j in range(a,c):
            graph[i][j] = 1 #graph[][] = 1인 경우 벽
    #print("graph",graph)

# def dfs(x,y,cnt):
#     #print("x,y",x,y)
#     cnt += 1
#     graph[x][y] = 1
#     dx = [0,0,-1,1]
#     dy = [-1,1,0,0]

#     for i in range(4):
#         nx = x+dx[i]
#         ny = y+dy[i]
#         print(x,y,"nxnt",nx,ny)
#         if (0<=nx<n and 0<=ny<m):
#             if (graph[nx][ny] == 0):
#                 print("dfs nxny",nx,ny)
#                 return dfs(nx,ny,cnt)

#     return cnt
            
def bfs(i,j):
    graph[i][j] = 1
    queue = deque()
    queue.append((i,j))
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    cnt = 1
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if (0<=nx<n and 0<=ny<m):
                if (graph[nx][ny] == 0):
                    #print("bfs", nx,ny)
                    graph[nx][ny] = 1
                    cnt += 1
                    queue.append((nx,ny))

    return cnt

cnt_lst = []
sum = 0
for i in range(n):
    for j in range(m):
        if (graph[i][j] == 0):
            sum += 1
            #print("for문",i,j)
            #print("cnt",dfs(i,j,0))
            #print("i,j",i,j,graph)
            cnt_lst.append(bfs(i,j))

cnt_lst.sort()

print(sum)
print(*cnt_lst)