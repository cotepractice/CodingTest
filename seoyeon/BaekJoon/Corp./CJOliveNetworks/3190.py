from collections import deque
N = int(input())
K = int(input())

boards = [[0 for _ in range(N)] for _ in range(N)] #boards 0:아무것도없음,1:뱀,2:사과
boards[0][0]=1
tails = [0,0]
Q=deque()

for k in range(K):
    kx,ky = map(int,input().split())
    boards[kx-1][ky-1]=2
    
L = int(input())
direction_lst = [[] for _ in range(L)]
for l in range(L):
    lx,ly = input().split()
    direction_lst[l] = [int(lx),ly]

#상하좌우
current_d = 0
current_pos = [0,0]

#우하좌상
d = [[0,1],[1,0],[0,-1],[-1,0]]

t = 0
d_idx = 0
while True:
    t+=1

    next_x,next_y = current_pos[0]+d[current_d][0], current_pos[1]+d[current_d][1]

    #종결 조건1
    if next_x<0 or next_x>=N or next_y<0 or next_y>=N:
        break
    #머리 넣기
    Q.append([next_x,next_y])
    current_pos = [next_x,next_y]
    
    #종결 조건2
    if boards[next_x][next_y]==1:
        break
    elif boards[next_x][next_y]==0:
        boards[tails[0]][tails[1]]=0
        tails = Q.popleft()

    boards[next_x][next_y]=1

    if d_idx>=L:
        continue
    if direction_lst[d_idx][0]==t:
        if direction_lst[d_idx][1]=="L":
            current_d -= 1
            if current_d<0:
                current_d += 4
        else:
            current_d += 1
            if current_d>=4:
                current_d -= 4
        d_idx += 1
print(t)