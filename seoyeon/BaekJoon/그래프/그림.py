#백준 #1926 그림
#그래프문제
from collections import deque

n,m = map(int, input().split())

graph = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, input().split()))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

#bfs
def bfs(x,y):
    cnt = 1
    Q = deque()
    graph[x][y] = 0
    Q.append((x,y))

    while Q:
        x,y = Q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if (0<=nx<n and 0<=ny<m):
                if (graph[nx][ny] == 1):
                    graph[nx][ny] = 0
                    cnt += 1
                    Q.append((nx,ny))

    return cnt

result = 0
cnt = 0
for i in range(n):
    for j in range(m):
        if (graph[i][j] == 1):
            count = bfs(i,j)
            cnt += 1
            if (count > result):
                result = count
print(cnt)
print(result)