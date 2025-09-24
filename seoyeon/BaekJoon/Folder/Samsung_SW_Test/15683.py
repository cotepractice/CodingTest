#백준 #15683 감시
#20:28-21:41

#1~5는 CCTV, 6은 벽
#벽은 통과할 수 없지만, CCTV는 통과 가능
#CCTV는 항상 90도 방향으로 회전 가능
#출력: 사각 지대의 최소 크기
import copy

N,M = map(int,input().split())
boards = [[-1 for _ in range(M)] for _ in range(N)]
cctvs = []
answer = float("inf")

for i in range(N):
    boards[i]=list(map(int,input().split()))
    for j in range(M):
        if 1<=boards[i][j]<=5:
            cctvs.append([boards[i][j],i,j])

#시간복잡도 O(4^len(cctvs)) = O(4^8)

def left(x,y,boards):
    y-=1
    while y>=0:
        if boards[x][y]==6:
            return boards
        if boards[x][y]==0:
            boards[x][y]=-1
        y-=1
    return boards

def right(x,y,boards):
    y+=1
    while y<M:
        if boards[x][y]==6:
            return boards
        if boards[x][y]==0:
            boards[x][y]=-1
        y+=1
    return boards

def up(x,y,boards):
    x-=1
    while x>=0:
        if boards[x][y]==6:
            return boards
        if boards[x][y]==0:
            boards[x][y]=-1
        x-=1
    return boards

def down(x,y,boards):
    x+=1
    while x<N:
        if boards[x][y]==6:
            return boards
        if boards[x][y]==0:
            boards[x][y]=-1
        x+=1
    return boards

def check(boards):

    ans = 0
    for i in range(N):
        for j in range(M):
            if boards[i][j]==0:
                ans += 1
    return ans

def cctv1(x,y,boards,k):
    if k==0:
        boards=up(x,y,boards)
    elif k==1:
        boards=down(x,y,boards)
    elif k==2:
        boards=left(x,y,boards)
    else:
        boards=right(x,y,boards)
    return boards

def cctv2(x,y,boards,k):

    if k==0:
        boards=up(x,y,boards)
        boards=down(x,y,boards)
    else:
        boards=left(x,y,boards)
        boards=right(x,y,boards)

    return boards

def cctv3(x,y,boards,k):
    if k==0:
        boards=up(x,y,boards)
        boards=right(x,y,boards)
    elif k==1:
        boards=right(x,y,boards)
        boards=down(x,y,boards)
    elif k==2:
        boards=left(x,y,boards)
        boards=down(x,y,boards)
    else:
        boards=left(x,y,boards)
        boards=up(x,y,boards)
    return boards

def cctv4(x,y,boards,k):
    if k==0:
        boards=left(x,y,boards)
        boards=up(x,y,boards)
        boards=right(x,y,boards)
    elif k==1:
        boards=up(x,y,boards)
        boards=right(x,y,boards)
        boards=down(x,y,boards)
    elif k==2:
        boards=right(x,y,boards)
        boards=down(x,y,boards)
        boards=left(x,y,boards)
    else:
        boards=down(x,y,boards)
        boards=left(x,y,boards)
        boards=up(x,y,boards)
    return boards

def cctv5(x,y,boards):
    boards=up(x,y,boards)
    boards=down(x,y,boards)
    boards=left(x,y,boards)
    boards=right(x,y,boards)
    return boards

# #idx번째의 cctv. 
def dfs(idx,boards_lst):
    global answer

    if idx==len(cctvs):
        ans = check(boards_lst)
        answer = min(answer, ans)
        return 

    if cctvs[idx][0]==1:
        for k in range(4):
            tmp_boards = copy.deepcopy(boards_lst)
            dfs(idx+1,cctv1(cctvs[idx][1],cctvs[idx][2],tmp_boards,k))
    elif cctvs[idx][0]==2:
        for k in range(2):
            tmp_boards = copy.deepcopy(boards_lst)
            dfs(idx+1,cctv2(cctvs[idx][1],cctvs[idx][2],tmp_boards,k))

    elif cctvs[idx][0]==3:
        for k in range(4):
            tmp_boards = copy.deepcopy(boards_lst)
            dfs(idx+1,cctv3(cctvs[idx][1],cctvs[idx][2],tmp_boards,k))
    elif cctvs[idx][0]==4:
        for k in range(4):
            tmp_boards = copy.deepcopy(boards_lst)
            dfs(idx+1,cctv4(cctvs[idx][1],cctvs[idx][2],tmp_boards,k))
    elif cctvs[idx][0]==5:
        tmp_boards = copy.deepcopy(boards_lst)
        dfs(idx+1,cctv5(cctvs[idx][1],cctvs[idx][2],tmp_boards))

dfs(0,boards)
print(answer)