#1113 수영장 만들기
from collections import deque

N, M = map(int,input().split())
boards = [[] for _ in range(N)]

for n in range(N):
    board = input()
    boards[n] = board

d = [[0,-1],[0,1],[1,0],[-1,0]]

def dfs(x,y,height,visited):
    
    for dx,dy in d:
        nx,ny = x+dx,y+dy
        if 0<=nx<N and 0<=ny<M:
            if int(boards[nx][ny])<height and visited[nx][ny]==False:
                visited[nx][ny]=True
                dfs(nx,ny,height,visited)
            elif int(boards[nx][ny])>height and visited[nx][ny]==False:
                visited[nx][ny]=True

#물이 고이는지 확인
def cal(visited):
    for i in range(N):
        if visited[i][0]==True:
            return False
        elif visited[i][M-1]==True:
            return False

    for j in range(M):
        if visited[0][j]==True:
            return False
        elif visited[N-1][j]==True:
            return False
        
    return True

def cal_cnt(k):
    cnt = 0
    for i in range(1,N-1):
        for j in range(1,M-1):
            if visited[i][j]==True:
                cnt += k-int(boards[i][j])
    return cnt

#k:벽
ans = 0
for k in range(2,10):
    #print("k",k)
    for i in range(1,N-1):
        for j in range(1,M-1):
            visited=[[False for _ in range(M)] for _ in range(N)]
            visited[i][j]=True
            dfs(i,j,k,visited)
            if (cal(visited)):
                cnt = cal_cnt(k)
                #print("cnt",cnt)
                ans = max(ans,cnt)
                
print(ans)