#백준 14940 쉬운 최단거리
#DP & BFS 문제
from collections import deque

n, m = map(int, input().split())

maps = [[0 for _ in range(m)] for _ in range(n)]
dp = [[-1 for _ in range(m)] for _ in range(n)] #시작 위치로부터의 거리
visited = [[False for _ in range(m)] for _ in range(n)]
pos = [-1,-1] #시작 위치

for i in range(n):
    map_lst = list(map(int, input().split()))
    maps[i] = map_lst
    for j in range(m):
        if map_lst[j] == 2:
            pos = [i,j]

dp[pos[0]][pos[1]] = 0
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(pos,maps,visited,dp):
    visited[pos[0]][pos[1]]=True
    Q = deque() #maps[nx][ny]=1을 처음 방문하는 경우 Q에 넣음
    Q.append([pos[0],pos[1]])
    while Q:
        x,y = Q.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<n and 0<=ny<m:

                #갈 수 없는 땅
                if visited[nx][ny]==False and maps[nx][ny]==0:
                    dp[nx][ny] = 0
                    visited[nx][ny] = True
                #갈 수 있는 땅
                if visited[nx][ny]==False and maps[nx][ny]==1:
                    visited[nx][ny] = True
                    dp[nx][ny] = dp[x][y] + 1
                    Q.append([nx,ny])

    return dp

dp = bfs(pos,maps,visited,dp)

#[POINT] 방문하지 못한 땅이 갈 수 있는 땅인지, 갈 수 없는 땅인지에 따라 dp값이 달라짐

for i in range(n):
    for j in range(m):
        if dp[i][j]==-1 and maps[i][j]==0:
            print(0, end=" ")
        else:
            print(dp[i][j],end=" ")
    print()