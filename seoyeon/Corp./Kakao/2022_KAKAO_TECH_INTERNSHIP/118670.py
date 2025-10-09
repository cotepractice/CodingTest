#1. 시간 초과
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

#2. 시간초과 해결
#15:30-
import copy
from collections import deque,defaultdict

N,M = 0,0

def solution(rc, operations):
    global N,M
    answer = []
    
    N = len(rc)
    M = len(rc[0])
    
    #rows는 rc[n][1:M-1] 가장 앞 원소와 마지막 원소 제외
    #제외된 원소는 right_cols, left_cols에 포함
    rows = deque(deque(rc[i][1:M-1]) for i in range(N))
    right_cols = deque(rc[i][M-1] for i in range(N))
    left_cols = deque(rc[i][0] for i in range(N-1,-1,-1))
    
    for o in operations:
        #연산1:가장자리 회전
        if o=="Rotate":
            # print("Rotate B")
            # print(rows)
            # print(right_cols)
            # print(left_cols)
            
            rows[0].appendleft(left_cols.pop()) #left_cols 마지막 원소 빼서 rows[0]에
            right_cols.appendleft(rows[0].pop()) #rows[0] 마지막 원소 빼서 right_cols에
            rows[N-1].append(right_cols.pop()) #right_cols 마지막 원소 빼서 rows[N-1]에
            left_cols.appendleft(rows[N-1].popleft()) #rows[N-1] 마지막 원소 빼서 left_cols에 

            # print("Rotate A")
            # print(rows)
            # print(right_cols)
            # print(left_cols)
        #연산2:마지막 행을 맨 위로 
        #1.rows: 맨 뒤 원소를 빼서 앞에 넣기
        #2.right_cols, left_cols 
        if o=="ShiftRow":
            # print("ShiftRow B")
            # print(rows)
            # print(right_cols)
            # print(left_cols)
            
            row_lst = rows.pop()
            rows.appendleft(row_lst)
            right_cols.appendleft(right_cols.pop())
            left_cols.append(left_cols.popleft())
            # print("ShiftRow A")
            # print(rows)
            # print(right_cols)
            # print(left_cols)
    
    for k in range(N):
        ans=[]
        ans.append(left_cols.pop())
        ans.extend(rows[k])
        ans.append(right_cols.popleft())
        answer.append(ans)
    
    return answer