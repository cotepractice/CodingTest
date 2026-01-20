#백준 #2468 안전 영역
#그래프 문제

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, input().split()))
    
#bfs 함수
def bfs(i,j,height):

    Q = deque()
    Q.append((i,j))
    check_lst[i][j] = True

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    while Q:

        x,y = Q.popleft()
        for p in range(4):
            nx = x+dx[p]
            ny = y+dy[p]
            #범위 내 존재하면서 방문한 적 없는 경우 
            if (0<=nx<n and 0<=ny<n):
                if (graph[nx][ny] > height and check_lst[nx][ny] == False):
                    check_lst[nx][ny] = True

                    Q.append((nx,ny))

    return

sum_lst = [0 for _ in range(100)]

for k in range(100):    #높이가 최대 100인 정수

    check_lst = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if (graph[i][j] > k and check_lst[i][j] == False):
                bfs(i,j,k)
                sum_lst[k] += 1

sum_lst.sort(reverse=True)
print(sum_lst[0])
    