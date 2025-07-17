#백준 #1987

# 1. O(2^(R*C))
# sys, pypy3 -> 63% 시간초과
import sys

input = sys.stdin.readline

R, C = map(int,input().split())
boards = ["" for _ in range(R)]

for i in range(R):
    board = input()
    boards[i] = board

ans = 0
d = [[0,-1],[0,1],[-1,0],[1,0]]

def dfs(visited,alpha,cnt,x,y):
    global ans

    if cnt>ans:
        ans=cnt

    for dx,dy in d:
        nx = x+dx
        ny = y+dy
        if 0<=nx<R and 0<=ny<C and visited[nx][ny]==False:
            if boards[nx][ny] not in alpha:
                visited[nx][ny]=True
                alpha[boards[nx][ny]]=0
                cnt += 1
                dfs(visited,alpha,cnt,nx,ny)
                #초기화. 다른 방향으로 가는 경우
                visited[nx][ny]=False
                del alpha[boards[nx][ny]]
                cnt -= 1
    
visited = [[False for _ in range(C)] for _ in range(R)]
# [0,0]에서 시작
visited[0][0]=True
alpha = dict() #현재까지 지난 알파벳 딕셔너리
alpha[boards[0][0]]=0
dfs(visited,alpha,1,0,0)

print(ans)