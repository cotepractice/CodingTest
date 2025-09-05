#백준 #12100 2048(Easy)

#상하좌우 네 방향 중 하나로 이동 가능
#같은 값을 가지는 두 블럭이 충돌하면 하나로 합쳐짐. 이때 하나로 합쳐진 값은 기존 값의 합이고 또 다시 합쳐질 수 없음
#이동하려고 하는 쪽의 칸이 먼저 합쳐짐
    #똑같은 수가 3개 있고, 위로 이동시키는 경우 위쪽 블럭이 먼저 합쳐짐

#출력:최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값
from copy import deepcopy

N = int(input())
boards = [[-1 for _ in range(N)] for _ in range(N)] #boards[i][j]=[n,False]

for i in range(N):
    lst = list(map(int,input().split()))
    boards[i]=lst

answer = 0

#2. 가장 끝 위치 max_pos부터 블럭 하나씩 넣기
def move(d,tmp_boards):
    #상하좌우 순서

    #1.상. 뒤에서 합쳐질 수도 있으므로 i=N-1부터 감소
    if d==0:
        
        for j in range(N):
            move_pos = 0
            for i in range(N): #가장 위 블럭부터 이동
                #블럭이 존재하는 경우 이동
                if tmp_boards[i][j]!=0:
                    #기존 블럭 값 저장 및 기존 블럭 위치 초기화
                    tmp_val = tmp_boards[i][j] 
                    tmp_boards[i][j]=0        
                    
                    #i==move_pos의 boards 값이 0인 경우, 그대로 이동
                    if tmp_boards[move_pos][j]==0:
                        tmp_boards[move_pos][j]=tmp_val
                    #i==move_pos의 boards 값이 tmp_val과 일치하면 합치고, move_pos 증가
                    #한 번에 한 번만 합칠 수 있기 때문
                    elif tmp_boards[move_pos][j]==tmp_val:
                        tmp_boards[move_pos][j]=tmp_val*2
                        move_pos += 1 #순서 중요. 한 번 합쳐졌으므로 현재 단계에서는 더 합쳐질 수 없으므로 다음 위치로 이동해야 함
                    #그렇지 않은 경우, 블럭 값이 다른 것이므로 이후 위치(move_pos+=1)에 값 저장
                    else:
                        move_pos += 1 #순서 중요
                        tmp_boards[move_pos][j]=tmp_val
                    
    #2. 하. 
    elif d==1:

        for j in range(N):
            move_pos = N-1
            for i in range(N-1,-1,-1):
                if tmp_boards[i][j]!=0:
                    tmp_val = tmp_boards[i][j]
                    tmp_boards[i][j]=0
                    #move_pos의 boards 값에 따라 boards 업데이트
                    if tmp_boards[move_pos][j]==0:
                        tmp_boards[move_pos][j]=tmp_val
                    elif tmp_boards[move_pos][j]==tmp_val:
                        tmp_boards[move_pos][j]=tmp_val*2
                        move_pos-=1
                    else:
                        move_pos-=1
                        tmp_boards[move_pos][j]=tmp_val

    #3. 좌
    elif d==2:

        for i in range(N):
            move_pos = 0
            for j in range(N):
                if tmp_boards[i][j]!=0:
                    tmp_val = tmp_boards[i][j]
                    tmp_boards[i][j]=0
                    if tmp_boards[i][move_pos]==0:
                        tmp_boards[i][move_pos]=tmp_val
                    elif tmp_boards[i][move_pos]==tmp_val:
                        tmp_boards[i][move_pos]=tmp_val*2
                        move_pos += 1
                    else:
                        move_pos += 1
                        tmp_boards[i][move_pos]=tmp_val

    #4. 우
    elif d==3:

        for i in range(N):
            move_pos = N-1
            for j in range(N-1,-1,-1):
                if tmp_boards[i][j]!=0:
                    tmp_val = tmp_boards[i][j]
                    tmp_boards[i][j]=0
                    if tmp_boards[i][move_pos]==0:
                        tmp_boards[i][move_pos]=tmp_val
                    elif tmp_boards[i][move_pos]==tmp_val:
                        tmp_boards[i][move_pos]=tmp_val*2
                        move_pos -= 1
                    else:
                        move_pos -= 1
                        tmp_boards[i][move_pos]=tmp_val

    return tmp_boards

def find_answer(tmp_boards):
    global answer

    for i in range(N):
        for j in range(N):
            answer = max(answer,tmp_boards[i][j])
            
    return

def dfs(now_boards,cnt):

    if cnt==5:
        find_answer(now_boards)
        return

    #상하좌우 이동
    for i in range(4):
        copy_boards = deepcopy(now_boards) #*deepcopy로 복사
        tmp_boards = move(i,copy_boards)
        dfs(tmp_boards,cnt+1)


dfs(boards,0)
print(answer)

#틀린 move() 함수
#아래와 같이 해결하는 경우 뒤에서 합쳐지는 경우 해결 못 함
#아래 테케에서 16 나와야 하는데 8 나옴
# 4
# 2 0 2 8
# 0 0 2 2
# 0 0 0 0
# 0 0 0 0

#bfs 사용
#시간복잡도 O(N*N). 1<-N<=20
# 1) 상하좌우로 이동 -> for i in range(4)
# 2) 이동 move(x,y,d)
  # boards 값 이동: 다음 위치가 범위 내(0보다크고N보다작음)에 존재하고, 다음 위치가 현재의 값과 일치하는지에 따라 처리
  # 일치하는 경우 -> boards의 첫 번째 값 변경, True로 변경
  # 일치하지 않는 경우 -> 위치만 이동
# 3) 최대 5번 이동한 후 얻을 수 있는 가장 큰 블록 출력

#1. 이동하는 블럭을 정렬로 처리
# def move(d,tmp_boards):
#     #print("d",d)
#     global blocks_pos

#     tmp_blocks_pos = []

#     #blocks_pos 정렬해 똑같은 수가 세 개 있는 경우, 이동하려고 하는 쪽의 칸이 먼저 합쳐짐
#     if d==0:
#         blocks_pos.sort() #x로 정렬
#     elif d==1:
#         blocks_pos.sort(reverse=True) #x 반대로 정렬
#     elif d==2:
#         blocks_pos.sort(key=lambda x:x[1]) #y로 정렬
#     elif d==3:
#         blocks_pos.sort(key=lambda x:x[1], reverse=True) #y로 반대로 정렬

    
#     #블럭 하나씩 빼기
#     for x,y in blocks_pos:
#         #print("First x,y",x,y)
#         tmp_x,tmp_y = x,y
#         tmp_val = tmp_boards[x][y]

#         #아래 해당 안 되면 계속 up
#         #1)범위를 벗어난 경우
#         #2)다른 블럭이 존재하는 경우
#         while True:
#             #범위 내에 존재하는지 확인
#             if x+dir[d][0]<0 or x+dir[d][0]>=N or y+dir[d][1]<0 or y+dir[d][1]>=N:
#                 break
#             next_val = tmp_boards[x+dir[d][0]][y+dir[d][1]]
#             #다른 수의 블럭인 경우
#             if (next_val!=0 and next_val!=tmp_val):
#                 break
#             x += dir[d][0]
#             y += dir[d][1]

#         tmp_blocks_pos.append([x,y]) #이동 위치 저장
        
#         #위치가 바뀐 경우만 진행
#         if tmp_x!=x or tmp_y!=y:
#             tmp_boards[tmp_x][tmp_y]=0 #기존 위치 초기화 
#             #이미 존재하는 블럭이 있는지 확인
#             #1)존재X
#             if tmp_boards[x][y]==0:
#                 tmp_boards[x][y]=tmp_val
#             #2)존재
#             #같은 값의 블럭이므로 True 변경 + 값 업데이트
#             else:
#                 tmp_boards[x][y]=tmp_val*2

#     blocks_pos = tmp_blocks_pos
#     return tmp_boards