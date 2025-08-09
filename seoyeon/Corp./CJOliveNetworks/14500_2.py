N,M = map(int,input().split())
boards = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    boards[i]=list(map(int,input().split()))

visited=[[False for _ in range(M)] for _ in range(N)]
answer = 0

def dfs(visited,x,y,depth,sum):
    global answer
    d=[[0,1],[0,-1],[1,0],[-1,0]]
    if depth==4:
        answer = max(answer,sum)
        return
    for dx,dy in d:
        nx = x+dx
        ny = y+dy
        if 0<=nx<N and 0<=ny<M and visited[nx][ny]==False:
            visited[nx][ny]=True
            dfs(visited,nx,ny,depth+1,sum+boards[nx][ny])
            visited[nx][ny]=False
def solve(x,y):
    global answer
    #상하좌우 탐색
    d = [[0,1],[0,-1],[1,0],[-1,0]]
    d_lst = []
    
    for dx,dy in d:
        nx = x+dx
        ny = y+dy
        if 0<=nx<N and 0<=ny<M:
            d_lst.append(boards[nx][ny])
    
    if len(d_lst)==4:
        d_lst.sort()
        del d_lst[0]
    if len(d_lst)==3:
        answer = max(answer,boards[x][y]+sum(d_lst))
    return

for i in range(N):
    for j in range(M):
        visited[i][j]=True
        dfs(visited,i,j,1,boards[i][j])
        solve(i,j)
        visited[i][j]=False
print(answer)