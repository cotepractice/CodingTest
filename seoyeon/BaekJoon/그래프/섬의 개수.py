#백준 #4963 섬의 개수
#그래프 문제
#21:10-21:24

from collections import deque

#하상좌우+대각선4개
dx = [0,0,-1,1,-1,1,-1,1]
dy = [-1,1,0,0,1,1,-1,-1]

#bfs 사용
def bfs(x,y):
    Q = deque()
    Q.append((x,y))    
    
    while Q:
        i, j = Q.popleft()

        for k in range(8):
            nx = i+dx[k]
            ny = j+dy[k]

            if (0<=nx<h and 0<=ny<w):
                if (graph[nx][ny] == 1):
                    graph[nx][ny] = 0
                    Q.append((nx,ny))


while True:
    w,h = map(int, input().split())

    #종결조건
    if (w==0 and h==0):
        break

    #graph 정의
    graph = [[0 for _ in range(w)] for _ in range(h)]

    for i in range(h):
        graph[i] = list(map(int, input().split()))
    
    #제시한 문제 해결
    cnt = 0
    for i in range(h):
        for j in range(w):
            if (graph[i][j] == 1):
                cnt += 1
                bfs(i,j)
    print(cnt)