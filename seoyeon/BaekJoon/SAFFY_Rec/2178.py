#백준 #2178 미로 탐색

from collections import deque

def bfs(x,y,cnt):
    global visited 

    Q = deque()
    Q.append([x,y,cnt])
    visited[x][y]=True
    d_lst = [[0,1],[0,-1],[1,0],[-1,0]]

    while Q:
        xx,yy,c = Q.popleft()

        if xx==N-1 and yy==M-1:
            return c

        for dx,dy in d_lst:
            nx = xx+dx
            ny = yy+dy

            if 0<=nx<N and 0<=ny<M:
                if maps[nx][ny]=="1" and visited[nx][ny]==False:
                    visited[nx][ny]=True
                    Q.append([nx,ny,c+1])


N,M = map(int,input().split())
maps = [[] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

for n in range(N):
    lst = input()
    maps[n]=lst

ans = float("inf")
print(bfs(0,0,1))
