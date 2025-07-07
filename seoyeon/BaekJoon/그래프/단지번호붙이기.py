#백준 #2667 단지번호붙이기 
#그래프 알고리즘
#01:40 소요

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [[0 for _ in range(n)] for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
for k in range(n):
    line = list(input())
    graph[k] = line

def dfs(i,j,visited,count):
    visited[i][j] = count
    i = int(i)
    j = int(j)
    
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
        
    for k in range(4):
        di = i + dx[k]
        dj = j + dy[k]

        if (di<=-1 or di>=n or dj<=-1 or dj>=n):
            continue

        if (graph[di][dj] == '1' and visited[di][dj] == 0):
            dfs(di,dj,visited,count)

count = 1

for i in range(n):
    for j in range(n):
        if (graph[i][j] != '\n' and int(graph[i][j]) > 0 and visited[i][j] == 0):
            dfs(i,j,visited,count)
            count += 1

count -= 1  #마지막에 올라간 count는 세면 안 됨
cnt_lst = [0 for _ in range(count)]

for i in range(n):
    for j in range(n):
        if (visited[i][j] != 0):
            cnt_lst[visited[i][j]-1] += 1

print(count)
cnt_lst.sort()
print(*cnt_lst, sep="\n")
