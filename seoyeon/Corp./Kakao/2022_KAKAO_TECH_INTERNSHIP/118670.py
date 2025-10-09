#15:30-
import copy
from collections import deque

def shiftrow(boards):

    tmp_boards = [[0 for _ in range(M)] for _ in range(N)]
    tmp_boards[0] = boards[N-1]
    for i in range(N-1):
        tmp_boards[i+1]=boards[i]

    return tmp_boards
    
#행렬의 바깥쪽에 있는 원소를 시계 방향으로 한 칸 회전
def rotate(boards):
        
    tmp_boards=copy.deepcopy(boards)
    Q = deque()
    
    for k in range(M):
        Q.append([0,k,boards[0][k]])
    for k in range(1,N):
        Q.append([k,M-1,boards[k][M-1]])
    for k in range(M-2,-1,-1):
        Q.append([N-1,k,boards[N-1][k]])
    for k in range(N-2,0,-1):
        Q.append([k,0,boards[k][0]])
    
    #맨 뒤 원소 앞으로
    x,y,val=Q.pop()
    
    tmp_boards[0][0]=val
    d=[[0,1],[1,0],[0,-1],[-1,0]]
    d_idx=0
    
    while Q:
        dx,dy = d[d_idx][0],d[d_idx][1]
        x,y,val = Q.popleft()
        
        nx,ny = x+dx,y+dy
        
        tmp_boards[nx][ny]=val
        
        #끝인 경우, d_idx 변경
        if d_idx==0 and ny==M-1:
            d_idx+=1
        elif d_idx==1 and nx==N-1:
            d_idx+=1
        elif d_idx==2 and ny==0:
            d_idx+=1
        elif d_idx==3 and nx==0:
            break

    return tmp_boards

        
N,M = 0,0
def solution(rc, operations):
    global N,M
    
    N = len(rc)
    M = len(rc[0])
    
    for o in operations:
        if o=="Rotate":
            rc=rotate(rc)
        if o=="ShiftRow":
            rc=shiftrow(rc)
    
    return rc