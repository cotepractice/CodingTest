#백준 #2178 미로탐색
#그래프 문제
#1:21
#최단 거리 문제는 BFS로 풀 것. BFS는 모든 깊이를 탐색하고 성공 유무가 결정되기에 적절하지 않음(운 좋으면 되고 안 좋으면 안 됨)

#1. sys input 사용하는 경우 오류 발생. 사용하지말것
#dx,dy에 따라 성공하는 예시가 다름. graph[n-1][m-2]가 0인 경우에 따라 나누어 테스트 케이스 모두 완료 => BUT 실패
#[1,0,-1,0],[0,1,0,-1]를 아래와 같이 하는 경우 예제입력1,3,4 성공, dx,dy를 [0,1,-1,0],[1,0,0,-1]로 하는 경우 2,3 성공   => WHY??

# n,m = map(int, input().split())

# graph = [[0 for _ in range(m)] for _ in range(n)]
# visited = [[False for _ in range(m)] for _ in range(n)]

# for i in range(n):
#     graph[i] = list(map(int,input()))

# dx = [1,0,-1,0]
# dy = [0,1,0,-1]
# #print("hi",graph[n-1][m-2])
# if (graph[n-1][m-2] == 0):
#     dx = [0,1,-1,0]
#     dy = [1,0,0,-1]

# def dfs(i,j,cnt):
#     #print("i,j",i,j)
#     cnt += 1
#     if (i == n-1 and j == m-1):
#         visited[i][j] = True
#         return 
#     #print("dx",dx)
#     #print("dy",dy)
#     for k in range(4):
#         x = i+dx[k]
#         y = j+dy[k]
#         #print("i,j in for", x,y)
        
#         if (x<0 or x>=n or y<0 or y>=m):
#             continue
#         if (graph[x][y] == 1 and visited[x][y]==False):
#             #print("dfs i,j",x,y)
#             visited[i][j] = True
#             dfs(x,y,cnt)
#             break   #하나의 방향으로 선택을 한 경우 다른 방향으로는 움직이지 않도록
        
# cnt = 0
# dfs(0,0,cnt)
# #print("visited",visited)
# answer = 0
# for i in range(n):
#     for j in range(m):
#         if (visited[i][j] == True):
#             answer += 1
# print(answer)

#2. bfs로 해결
#graph 정의 시 sys input 사용할 수 있음 !! => 대신 `input().rstrip()` 으로 사용해 맨 뒤의 \n 제거해야함
#graph[x][y]가 1인 경우 graph[x][y] = graph[i][j]+1로 설정
#dp와 비슷한 개념 존재하는 bfs

import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())

graph = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int,input().rstrip()))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(i,j):
    queue = deque()
    queue.append((i,j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]

            if (0<=X<n and 0<=Y<m and graph[X][Y]==1):
                queue.append((X,Y))
                graph[X][Y] = graph[x][y] + 1

    return graph[n-1][m-1]

#print("graph", graph)
print(bfs(0,0))
