#백준 #2630 색종이 만들기
#16:00-17:25

#BFS
from collections import deque

N = int(input())
n_lst = [] #가능한 정사각형 길이 (긴 순서대로)
boards = [[0 for _ in range(N)] for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
result = [0,0] #하얀색개수,파란색개수

for i in range(N):
    lst = list(map(int,input().split()))
    boards[i]=lst

#n_lst 탐색
M = N
while M!=1:
    n_lst.append(M)
    M = M//2
n_lst.append(1)

#1.[x,y] 좌표로부터 오른쪽아래로 구성된 한 변의 길이가 n인 정사각형이 모두 동일한 색을 가지는지 확인하는 함수
#하나의 색으로 구성되지 않음:-1 출력, 흰색:0, 파란색:1
def bfs(x,y,n):
    global result
    #n=1인 경우 자기자신만 포함 -> result 업데이트
    if n==1:
        result[boards[x][y]] += 1
        return boards[x][y]

    #ex,ey는 가장 마지막 x,y 좌표. 탐색할 부분이 범위 넘어서면 탐색하지 않음
    ex,ey = x+n,y+n
    if ex>N or ey>N:
        return -1
    
    #bfs()에서 동일한 좌표 넣지 않으려는 목적
    small_visited=[[False for _ in range(N)] for _ in range(N)]

    Q=deque()
    Q.append([x,y])
    d = [[0,1],[1,0],[1,1]] # 시작위치를 [x,y]로 하고 오른쪽아래로 정사각형 생성
    color = boards[x][y] #시작위치 색상

    while Q:
        cx,cy = Q.popleft()
        for dx,dy in d:
            nx = cx+dx
            ny = cy+dy
            if 0<=nx<ex and 0<=ny<ey and small_visited[nx][ny]==False:
                small_visited[nx][ny]=True
                Q.append([nx,ny])
                if boards[nx][ny]!=color:
                    return -1

    #여기까지 온 거면 모두 같은 색인 것이므로 result 추가
    result[color] += 1

    return color

#[x,y]부터 시작하는 오른쪽아래 정사각형 방문처리
def check(x,y,n):
    global visited

    cx,cy = x,y
    ex,ey = x+n,y+n
    
    for i in range(cx,ex):
        for j in range(cy,ey):
            visited[i][j]=True
    
Q = deque()
Q.append([0,0,0])

while Q:
    cx,cy,idx = Q.popleft()

    if visited[cx][cy]==True:
        continue

    r = bfs(cx,cy,n_lst[idx])
    
    #정사각형이 모두 같은 색인 경우 -> 방문처리
    if r!=-1:
        check(cx,cy,n_lst[idx])
        continue
    
    #정사각형이 모두 같은 색이 아닌 경우, 정사각형 길이 N//2로 나누어 네 공간 탐색
    for k in range(4):
        if k==0:
            Q.append([cx,cy,idx+1])
        elif k==1:
            Q.append([cx,cy+n_lst[idx+1],idx+1])
        elif k==2:
            Q.append([cx+n_lst[idx+1],cy,idx+1])
        else:
            Q.append([cx+n_lst[idx+1],cy+n_lst[idx+1],idx+1])

print(*result,sep="\n")