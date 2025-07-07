#백준 #4485 녹색 옷 입은 애가 젤다지?
#다익스트라

import heapq

def solv():
    global dp 

    heap = [(boards[0][0],0,0)]
    visited[0][0]=True
    heapq.heapify(heap)

    while heap:
        num, x,y = heapq.heappop(heap)
        dp[x][y] = num
        for dx,dy in d_lst:
            nx = x+dx
            ny = y+dy
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==False:
                visited[nx][ny]=True
                heapq.heappush(heap,(num+boards[nx][ny],nx,ny))

n = 1
while True:
    N = int(input())

    if N == 0:
        break
    boards = [[0 for _ in range(N)] for _ in range(N)]
    dp = [[float("inf") for _ in range(N)] for _ in range(N)]
    d_lst = [[0,1],[0,-1],[1,0],[-1,0]]
    visited = [[False for _ in range(N)] for _ in range(N)]

    for i in range(N):
        lst = list(map(int,input().split()))
        boards[i] = lst
    
    solv()
    
    print("Problem ",n,":",sep="",end=" ")
    print(dp[N-1][N-1])

    n+=1