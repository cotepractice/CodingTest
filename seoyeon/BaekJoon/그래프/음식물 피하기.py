#백준 #1743 음식물 피하기
#그래프 문제
#0:10

from collections import deque

n, m, k = map(int, input().split())

graph = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(k):
    r,c = map(int, input().split())

    graph[r-1][c-1] = 1

def bfs(i,j):
    cnt = 1
    Q = deque()
    Q.append((i,j))
    graph[i][j] = 0

    while Q:
        x,y = Q.popleft()
        dx=[0,0,-1,1]
        dy=[-1,1,0,0]
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if (0<=nx<n and 0<=ny<m):
                if (graph[nx][ny] == 1):
                    cnt += 1
                    graph[nx][ny] = 0
                    Q.append((nx,ny))
    return cnt


cnt_lst = []
for i in range(n):
    for j in range(m):
        if (graph[i][j] == 1):
            cnt_lst.append(bfs(i,j))
cnt_lst.sort(reverse=True)
print(cnt_lst[0])