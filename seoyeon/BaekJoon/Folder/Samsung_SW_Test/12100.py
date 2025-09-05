#백준 #12100 2048(Easy)
#15:55-

#상하좌우 네 방향 중 하나로 이동 가능
#같은 값을 가지는 두 블럭이 충돌하면 하나로 합쳐짐. 이때 하나로 합쳐진 값은 기존 값의 합이고 또 다시 합쳐질 수 없음
#이동하려고 하는 쪽의 칸이 먼저 합쳐짐
    #똑같은 수가 3개 있고, 위로 이동시키는 경우 위쪽 블럭이 먼저 합쳐짐

#출력:최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값
from collections import deque

N = int(input())
boards = [[[-1,False] for _ in range(N)] for _ in range(N)] #boards[i][j]=[n,False]

for i in range(N):
    lst = list(map(int,input().split()))
    for l in range(len(lst)):
        boards[i][l][0]=lst[l]

#블록 위치 저장
blocks_pos = []
for i in range(N):
    for j in range(N):
        if boards[i][j][0]!=0:
            blocks_pos.append([i,j])

answer = 0
# for i in range(N):
#     print(*boards)

#bfs 사용
#시간복잡도 O(N*N). 1<-N<=20
# 1) 상하좌우로 이동 -> for i in range(4)
# 2) 이동 move(x,y,d)
  # boards 값 이동: 다음 위치가 범위 내(0보다크고N보다작음)에 존재하고, 다음 위치가 현재의 값과 일치하는지에 따라 처리
  # 일치하는 경우 -> boards의 첫 번째 값 변경, True로 변경
  # 일치하지 않는 경우 -> 위치만 이동
# 3) 최대 5번 이동한 후 얻을 수 있는 가장 큰 블록 출력

#상하좌우
dir = [[-1,0],[1,0],[0,-1],[0,1]]


def move(d,tmp_boards):
    global blocks_pos

    tmp_blocks_pos = []

    #blocks_pos 정렬해 똑같은 수가 세 개 있는 경우, 이동하려고 하는 쪽의 칸이 먼저 합쳐짐
    if d==0:
        blocks_pos.sort() #x로 정렬
    elif d==1:
        blocks_pos.sort(reverse=True) #x 반대로 정렬
    elif d==2:
        blocks_pos.sort(key=lambda x:x[1]) #y로 정렬
    elif d==3:
        blocks_pos.sort(key=lambda x:x[1], reverse=True) #y로 반대로 정렬

    
    #블럭 하나씩 빼기
    for x,y in blocks_pos:
        #print("First x,y",x,y)
        tmp_x,tmp_y = x,y
        tmp_val = tmp_boards[x][y][0]
        tmp_yn = tmp_boards[x][y][1]

        #아래 해당 안 되면 계속 up
        #1)범위를 벗어난 경우
        #2)다른 블럭이 존재하는 경우
        #3)같은 블럭이어도 True이면 더 못 감. boards[nx][ny][1]==True: 
        while True:
            #print("HERE")
            if x+dir[d][0]<0 or x+dir[d][0]>=N or y+dir[d][1]<0 or y+dir[d][1]>=N:
                break
            next_val = tmp_boards[x+dir[d][0]][y+dir[d][1]][0]
            next_yn = tmp_boards[x+dir[d][0]][y+dir[d][1]][1]
            #print("next_val",next_val,"current_val",tmp_val)

            if (next_val!=0 and next_val!=tmp_val) or next_yn==True:
                break
            x += dir[d][0]
            y += dir[d][1]
        #print("Final movex,movey",x,y)
        tmp_blocks_pos.append([x,y]) #이동 위치 저장
        #현재 위치는 0이거나 합쳐질 수 있는 같은 값의 False 블럭
        #위치가 바뀐 경우만 진행
        if tmp_x!=x or tmp_y!=y:
            tmp_boards[tmp_x][tmp_y]=[0,False] #기존 위치 초기화 
            #이미 존재하는 블럭이 있는지 확인
            #1)존재X
            if tmp_boards[x][y][0]==0:
                tmp_boards[x][y]=[tmp_val,tmp_yn]
            #2)존재
            #같은 값의 블럭이므로 True 변경 + 값 업데이트
            else:
                tmp_boards[x][y]=[tmp_val*2,True]

    blocks_pos = tmp_blocks_pos[:]
    return tmp_boards
            

def find_answer(tmp_boards):
    global answer

    for i in range(N):
        for j in range(N):
            answer = max(answer,tmp_boards[i][j][0])
            
    return

def dfs(now_boards,cnt):
    
    if cnt>6:
        find_answer(now_boards)
        return

    #상하좌우 이동
    for i in range(4):
        tmp_boards = move(i,now_boards)
        dfs(tmp_boards,cnt+1)

    # tmp_boards = move(0,now_boards)
    # #ttmp_boards = move(2,tmp_boards)
    # #print("tmp_boards")
    # for i in range(N):
    #     print(*tmp_boards[i])
    


dfs(boards,0)
print(answer)

# 테케
# 4
# 0 0 2 0
# 0 0 0 0
# 2 0 0 0
# 0 0 0 0