#백준 2931 가스관
from collections import deque

def solv(prev_x,prev_y,x,y,p):
    lst = []
    if p==pipe[0]:
        if prev_x>x:
            lst.append([x-1,y]) #위로
        else:
            lst.append([x+1,y]) #아래로
    elif p==pipe[1]:
        if prev_y>y:
            lst.append([x,y-1]) #왼쪽
        else:
            lst.append([x,y+1]) #오른쪽
    elif p==pipe[2]:
        if prev_x>x and prev_y==y: #아래->위로 들어옴
            lst.append([x,y-1])
            lst.append([x,y+1])
            lst.append([x-1,y])
        elif prev_x<x and prev_y==y: #위->아래로 들어옴
            lst.append([x,y-1])
            lst.append([x,y+1])
            lst.append([x+1,y])
        elif prev_x==x and prev_y>y: #오른쪽->왼쪽으로 들어옴
            lst.append([x,y-1])
            lst.append([x+1,y])
            lst.append([x-1,y])
        elif prev_x==x and prev_y<y: #왼쪽->오른쪽으로 들어옴
            lst.append([x-1,y])
            lst.append([x+1,y])
            lst.append([x,y+1])
        

    elif p==pipe[3]:
        if prev_y>y: #왼쪽->오른쪽
            lst.append([x+1,y])
        else:
            lst.append([x,y+1])

    elif p==pipe[4]:
        if prev_x<x: #위->아래
            lst.append([x,y+1])
        else:
            lst.append([x-1,y])
    elif p==pipe[5]:
        if prev_y<y: #왼쪽->오른쪽
            lst.append([x-1,y])
        else:
            lst.append([x,y-1])

    elif p==pipe[6]:
        if prev_x>x: #위->아래
            lst.append([x,y-1])
        else:
            lst.append([x+1,y])

    return lst

def bfs(i,j):
    global board,ans

    d_lst = [[-1,0],[1,0],[0,-1],[0,1]]
    Q = deque()

    for dx,dy in d_lst:
        nx = i+dx
        ny = j+dy
        if 0<=nx<R and 0<=ny<C and board[nx][ny]!="." and visited[nx][ny]==False:
            visited[nx][ny]=True
            Q.append([i,j,nx,ny,board[nx][ny]])

    
    while Q:
        prev_x,prev_y,x,y,p = Q.popleft()

        lsts = solv(prev_x,prev_y,x,y,p)
        for lst in lsts:
            nx,ny = lst[0],lst[1]
            if 0<=nx<R and 0<=ny<C:
                if board[nx][ny] in pipe and visited[nx][ny]==False:
                    visited[nx][ny]=True
                    Q.append([x,y,nx,ny,board[nx][ny]])
                if board[nx][ny] == ".":
                    ans = [nx,ny]


R, C = map(int,input().split())
board = [list(input()) for _ in range(R)]
pipe = ["|","-","+","1","2","3","4"]
visited = [[False for _ in range(C)] for _ in range(R)]

ans = [-1,-1]
start = [-1,-1]
end = [-1,-1]
for i in range(R):
    for j in range(C):
        if board[i][j]=="M":
            start[0],start[1] = i,j
        elif board[i][j]=="Z":
            end[0],end[1] = i,j

bfs(start[0],start[1])
bfs(end[0],end[1])

d_lst = [[-1,0],[1,0],[0,-1],[0,1]]

x,y = ans[0],ans[1]
ans_d = [False,False,False,False] #상하좌우
for dx,dy in d_lst:
    nx = x+dx
    ny = y+dy
    if 0<=nx<R and 0<=ny<C:
        #상하좌우 순서
        if nx<x and ny==y:
            if board[nx][ny]=="|" or board[nx][ny]=="+" or board[nx][ny]=="1" or board[nx][ny]=="4":
                ans_d[0]=True
        elif nx>x and ny==y:
            if board[nx][ny]=="|" or board[nx][ny]=="+" or board[nx][ny]=="2" or board[nx][ny]=="3":
                ans_d[1]=True
        elif nx==x and ny<y:
            if board[nx][ny]=="-" or board[nx][ny]=="+" or board[nx][ny]=="1" or board[nx][ny]=="2":
                ans_d[2]=True
        elif nx==x and ny>y:
             if board[nx][ny]=="-" or board[nx][ny]=="+" or board[nx][ny]=="3" or board[nx][ny]=="4":
                ans_d[3]=True           

ans_p = ""
if ans_d[0]==ans_d[1]==ans_d[2]==ans_d[3]==True:
    ans_p="+"
elif ans_d[0]==ans_d[1]==True:
    ans_p="|"
elif ans_d[2]==ans_d[3]==True:
    ans_p="-"
elif ans_d[1]==ans_d[3]==True:
    ans_p="1"
elif ans_d[0]==ans_d[3]==True:
    ans_p="2"
elif ans_d[2]==ans_d[0]==True:
    ans_p="3"
elif ans_d[1]==ans_d[2]==True:
    ans_p="4"

print(ans[0]+1,ans[1]+1,ans_p)