#백준 #14503 로봇 청소기
#22:52-23:11

#각 칸은 벽 또는 빈 칸
#1. 청소되지 않은 경우 현재 칸 청소
#2. 주변 4칸 중 청소되지 않은 빈칸이 없는 경우
## 바라보는 방향을 유지한 채 한 칸 후진할 수 있다면 한 칸 후진 후 1번으로 돌아감
## 바라보는 방향의 뒷 칸이 벽이라 후진할 수 없으면 작동을 멈춤 => 종결조건
#3. 주변 4칸 중 청소되지 않은 빈칸이 있는 경우
## 반시계 방향으로 90도 회전 
## 바라보는 방향을 기준으로 앞 쪽 칸이 청소되지 않은 빈칸인 경우 한 칸 전진
## 1번으로 돌아감

N,M = map(int,input().split())
#로봇 청소기 좌표 (r,c), 청소기가 바라보는 방향 d
r,c,d = map(int,input().split()) 
#방향 동->북->서->남 (반시계 방향으로 90도 회전 시 d_index 1 증가)
dir = [[0,1],[-1,0],[0,-1],[1,0]]

#boards 값이 0: 청소되지 않은 빈칸, 1: 벽
boards = [[-1 for _ in range(M)] for _ in range(N)]

for i in range(N):
    board = list(map(int,input().split()))
    boards[i] = board

cx,cy = r,c
#d는 "북,동,남,서" 
#d_index는 현재 바라보는 방향 
if d==0:
    d_index=1
elif d==1:
    d_index=0
elif d==2:
    d_index=3
else:
    d_index=2

answer = 0
while True:
    #1. 현재 칸이 청소되지 않은 경우 청소
    if boards[cx][cy]==0:
        boards[cx][cy]=2
        answer += 1
    
    #2. 주변 4칸 중 청소되지 않은 빈 칸
    cnt = 0
    for dx,dy in dir:
        nx = cx+dx
        ny = cy+dy
        if 0<=nx<N and 0<=ny<M and boards[nx][ny]==0:
            cnt += 1
    ## 4칸 중 빈칸이 없는 경우 
    if cnt==0:
        nd = (d_index+2)%4
        nx = cx+dir[nd][0]
        ny = cy+dir[nd][1]
        #후진은 벽만 아니면 가능 (빈 칸이거나 청소되어 있는 경우)
        if 0<=nx<N and 0<=ny<M and boards[nx][ny]!=1:
            cx,cy = nx,ny
        else:
            break
    
    ## 빈칸 있는 경우
    else:
        d_index = (d_index+1)%4
        nx = cx+dir[d_index][0]
        ny = cy+dir[d_index][1]
        if 0<=nx<N and 0<=ny<M and boards[nx][ny]==0:
            cx,cy = nx,ny

print(answer)