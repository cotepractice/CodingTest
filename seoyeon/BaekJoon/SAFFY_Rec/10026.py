#백준 #10026 적록색약
from collections import deque

def bfs(x,y,color):
    global visited

    d_lst = [[0,-1],[0,1],[-1,0],[1,0]]
    Q = deque()
    Q.append([x,y])
    visited[x][y]=True

    while Q:
        xx,yy = Q.popleft()
        for dx,dy in d_lst:
            nx = xx+dx
            ny = yy+dy

            if 0<=nx<N and 0<=ny<N and maps[nx][ny]==color and visited[nx][ny]==False:
                visited[nx][ny]=True
                Q.append([nx,ny])

def color_bfs(x,y,color):
    global visited

    d_lst = [[0,-1],[0,1],[-1,0],[1,0]]
    Q = deque()
    Q.append([x,y])
    visited[x][y]=True


    while Q:
        xx,yy = Q.popleft()
        for dx,dy in d_lst:
            nx = xx+dx
            ny = yy+dy
            if color=="R" or color=="G":
                #print("nx,ny",nx,ny)
                if 0<=nx<N and 0<=ny<N and (maps[nx][ny]=="R" or maps[nx][ny]=="G") and visited[nx][ny]==False:
                    visited[nx][ny]=True
                    Q.append([nx,ny]) 
            else:
                if 0<=nx<N and 0<=ny<N and maps[nx][ny]==color and visited[nx][ny]==False:
                    visited[nx][ny]=True
                    Q.append([nx,ny]) 

N = int(input())
maps = ["" for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]

for i in range(N):
    lst = input()
    maps[i] = lst

ans = [0,0]
for i in range(N):
    for j in range(N):
        if visited[i][j]==False:
            ans[0] += 1
            bfs(i,j,maps[i][j])

visited = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j]==False:
            ans[1] += 1
            color_bfs(i,j,maps[i][j])

print(*ans)