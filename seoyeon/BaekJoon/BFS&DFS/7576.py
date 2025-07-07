#백준 #7576 토마토
from collections import deque

#BFS
def spread(spread_lst):
    global N,M,box,ans

    d_lst = [[0,1],[0,-1],[1,0],[-1,0]]
    Q = deque()
    for x,y in spread_lst:
        Q.append([x,y,1])
    visited=[[False for _ in range(M)]for _ in range(N)]
    
    while Q:
        xx,yy,depth = Q.popleft()
        visited[xx][yy]=True
        for dx,dy in d_lst:
            nx = xx+dx
            ny = yy+dy
            if 0<=nx<N and 0<=ny<M and visited[nx][ny]==False:
                if box[nx][ny]!=0 and box[nx][ny] < depth+1:
                    continue
                visited[nx][ny]=True
                box[nx][ny]=depth+1
                Q.append([nx,ny,depth+1])
        

M,N = map(int,input().split())
box = [[] for _ in range(N)]

for n in range(N):
    lst = list(map(int,input().split()))
    box[n] = lst

spread_xy=[]
for i in range(N):
    for j in range(M):
        if box[i][j]==1:
            spread_xy.append([i,j])
            
spread(spread_xy)

check = 0
ans = 0
for i in range(N):
    for j in range(M):
        if box[i][j]==0:
            check = 1
        else:
            ans=max(ans,box[i][j])

if check == 1:
    print(-1)
else:
    print(ans-1)