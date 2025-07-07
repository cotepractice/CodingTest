#백준 #2636 치즈
#BFS

#0을 -1로 만드는 bfs 함수
def func():

    global matrix,N,M
    
    Q = deque() #탐색할 수 있는 곳,matrix[x][y]=0
    melt = deque() #녹는 곳,matrix[x][y]=1
    visited = [[False for _ in range(M)] for _ in range(N)]

    Q.append([0,0])
    d_lst = [[0,1],[0,-1],[1,0],[-1,0]]
    while Q:
        x,y = Q.popleft()
        for dx,dy in d_lst:
            nx = x+dx
            ny = y+dy
            if 0<=nx<N and 0<=ny<M and visited[nx][ny]==False:
                visited[nx][ny]=True
                if matrix[nx][ny]==0:
                    Q.append([nx,ny])
                elif matrix[nx][ny]==1:
                    melt.append([nx,ny])
    cnt = 0
    while melt:
        x,y = melt.popleft()
        matrix[x][y] = 0
        cnt += 1

    return cnt

from collections import deque

N, M = map(int,input().split())
ans = [0,0] #ans[0]:치즈가 모두 녹는데 걸리는 시간,ans[1]:모두 녹기 한 시간 전 남아있는 치즈 조각 개수 

matrix = [[-1 for _ in range(M)] for _ in range(N)] 

for i in range(N):
    lst = list(map(int,input().split()))
    matrix[i]=lst

#처음
while True:
    cheese = func()
    
    if cheese>0:
        ans[0] += 1
        ans[1] = cheese
    else:
        break

print(*ans,sep="\n")