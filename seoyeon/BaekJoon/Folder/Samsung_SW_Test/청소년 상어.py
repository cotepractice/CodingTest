#백준 #19236 청소년상어
#삼성 SW 역량 테스트 기출
from collections import deque
import copy

space = [[[0,0] for _ in range(4)] for _ in range(4)]
d = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]


for k in range(4):
    lst = []
    lst = list(map(int, input().split()))
    for l in range(8):
        if l%2==0:
            a,b = lst[l], lst[l+1]-1    #b는 1부터 시작하므로. d 인덱스와 맞추기 위해
            space[k][l//2] = [a,b]

def move_fish(shark_x, shark_y, space):
    for k in range(1,17):
        x,y = -1,-1
        for i in range(4):
            for j in range(4):
                if space[i][j][0] == k:
                    x,y = i,j

        if (x==-1 and y==-1):
            continue
        
        fish_d = space[x][y][1]
        
        for l in range(8):
            
            fish_d_idx = (fish_d + l) % 8
            
            nx = x+d[fish_d_idx][0]
            ny = y+d[fish_d_idx][1]

            if 0<=nx<=3 and 0<=ny<=3:
                #상어 위치는 이동할 수 없음
                if nx==shark_x and ny==shark_y:
                    continue
                
                space[x][y][1] = fish_d_idx
                space[x][y], space[nx][ny] = space[nx][ny], space[x][y]
                
                break

    return space

def dfs(x,y,cnt,space):
    global result
    cnt += space[x][y][0]
    shark_d = space[x][y][1]
    space[x][y] = [-1,-1]
    result = max(result, cnt)

    #1. 물고기 이동
    space = move_fish(x,y,space)

    #2. 상어 이동
    for k in range(1,5):
        nx = x+d[shark_d][0]*k
        ny = y+d[shark_d][1]*k

        if 0<=nx<=3 and 0<=ny<=3:
            if space[nx][ny][0] > 0:
                dfs(nx,ny,cnt,copy.deepcopy(space))


result = 0
dfs(0,0,0,space)
print(result)