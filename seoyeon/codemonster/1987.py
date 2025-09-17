# #백준 #1987

# # 1. O(2^(R*C))
# # sys, pypy3 -> 63% 시간초과
# import sys

# input = sys.stdin.readline

# R, C = map(int,input().split())
# boards = ["" for _ in range(R)]

# for i in range(R):
#     board = input()
#     boards[i] = board

# ans = 0
# d = [[0,-1],[0,1],[-1,0],[1,0]]

# def dfs(visited,alpha,cnt,x,y):
#     global ans

#     if cnt>ans:
#         ans=cnt

#     for dx,dy in d:
#         nx = x+dx
#         ny = y+dy
#         if 0<=nx<R and 0<=ny<C and visited[nx][ny]==False:
#             if boards[nx][ny] not in alpha:
#                 visited[nx][ny]=True
#                 alpha[boards[nx][ny]]=0
#                 cnt += 1
#                 dfs(visited,alpha,cnt,nx,ny)
#                 #초기화. 다른 방향으로 가는 경우
#                 visited[nx][ny]=False
#                 del alpha[boards[nx][ny]]
#                 cnt -= 1
    
# visited = [[False for _ in range(C)] for _ in range(R)]
# # [0,0]에서 시작
# visited[0][0]=True
# alpha = dict() #현재까지 지난 알파벳 딕셔너리
# alpha[boards[0][0]]=0
# dfs(visited,alpha,1,0,0)

# print(ans)

#2. DFS 시간 복잡도 감소
from collections import deque
import sys

input = sys.stdin.readline

R, C = map(int,input().split())
boards = ["" for _ in range(R)]

for i in range(R):
    board = input()
    boards[i] = board

def bfs():
    max_depth = 0 #지날 수 있는 최대 칸 수

    Q = set() #set(). 중복 방지. Q = [[x1,y1,visited_alpha],...] 
    Q.add((0,0,boards[0][0]))

    d = [[0,-1],[0,1],[-1,0],[1,0]]
    while Q:
        x,y,visited_alpha = Q.pop()
        max_depth = max(max_depth, len(visited_alpha))

        if max_depth == 26: #알파벳이 총 26
            return 26

        for dx,dy in d:
            nx = x+dx
            ny = y+dy
            if 0<=nx<R and 0<=ny<C and boards[nx][ny] not in visited_alpha:
                Q.add((nx,ny,visited_alpha+boards[nx][ny]))
    return max_depth

print(bfs())