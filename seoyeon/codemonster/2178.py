#BFS

from collections import deque

N,M = map(int,input().split())
boards = [[] for _ in range(N)] #1: 이동할 수 있는 칸, 2: 이동할 수 없는 칸

for n in range(N):
    lst = list(map(int,input().rstrip()))
    boards[n] = lst

def bfs():

    d = [[0,-1],[0,1],[-1,0],[1,0]]
    visited = [[-1 for _ in range(M)] for _ in range(N)]

    Q = deque()
    Q.append([0,0])
    visited[0][0]=1

    while Q:
        x,y = Q.popleft()
        for dx,dy in d:
            nx,ny = x+dx,y+dy
            if 0<=nx<N and 0<=ny<M and boards[nx][ny]==1 and visited[nx][ny]==-1:
                visited[nx][ny] = visited[x][y]+1
                Q.append([nx,ny])

    print(visited[N-1][M-1])

bfs()