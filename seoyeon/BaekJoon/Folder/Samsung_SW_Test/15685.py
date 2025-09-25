#백준 #15685 드래곤 커브

#100*100 격자에 드래곤 커브 N개 존재
#출력:크기가 1*1인 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 정사각형의 개수
from collections import deque

N = int(input())
dragon_curves = [[] for _ in range(N)] #dragon_curves=[[시작x,시작y,시작방향,세대]]
for n in range(N):
    dragon_curves[n] = list(map(int,input().split()))

boards = [[0 for _ in range(101)] for _ in range(101)]
answer = 0

#1.curve에 따라 boards 채우기
# g=10까지 진행 <- 문제에 주어짐
#2.boards 탐색해 1*1 정사각형의 네 꼭짓점 확인
# boards가 1인 경우 dragon_curve에 해당

dir = [[0,1],[-1,0],[0,-1],[1,0]]

def curve(k,d,g,x,y,prev):
    global boards

    #종결조건: g세대 드래곤 커브까지만 진행
    if k==g+1:
        return 
    
    #0세대 드래곤 커브 정의
    elif k==0:
        curve_lst = [[x,y], [x+dir[d][0],y+dir[d][1]]]
        boards[x][y]=1
        boards[x+dir[d][0]][y+dir[d][1]]=1

        curve(k+1,d,g,x,y,curve_lst)
    
    #1세대 이후 드래곤 커브 
    #1. 끝점 탐색
    #2. prev에서 값 popleft() 후 90도 회전
    # 끝점과 회전한 값으로 새로운 좌표 탐색
    #3. 새로운 좌표 boards 업데이트, 다음에 넘길 prev 리스트애 넣기
    else:
        Q = deque(prev)

        ex,ey = prev[-1]
        current=[]
        #print("Q",Q)

        while Q:
            cx,cy = Q.pop()
            #print("cxcy",cx,cy)
            if [cx,cy]==prev[-1]:
                continue
            #90도 회전
            #cx 끝점 x로부터 떨어진 만큼(ex-cx) y로 떨어지고
            #cy 끝점 y로부터 떨어진 만큼(ey-cy) x로 떨어짐
            tmp_x,tmp_y = 0,0
            if ey>=cy:
                tmp_x = -abs(ey-cy)
            else:
                tmp_x = abs(ey-cy)
            
            if cx>=ex:
                tmp_y = -abs(ex-cx)
            else:
                tmp_y = abs(ex-cx)

            nx, ny = ex+tmp_x, ey+tmp_y
            current.append([nx,ny])
            boards[nx][ny]=1

        
        curve(k+1,d,g,x,y,prev+current)

def check():
    global answer

    check_d = [[0,1],[1,0],[1,1]]

    for i in range(99):
        for j in range(99):
            if boards[i][j]==1:
                cnt = 1
                for dd in range(3):
                    if boards[i+check_d[dd][0]][j+check_d[dd][1]]==1:
                        cnt += 1
                    else:
                        break
                if cnt==4:
                    answer += 1


#시간복잡도 O(N*g)
#문제에 주어진대로 boards 업데이트
for x,y,d,g in dragon_curves:
    #print("Dragon")
    curve(0,d,g,y,x,[0,0])

check()
print(answer)

#N*M
# [1,2,3]             [10 7 4 1]        [12 11 10]     
# [4,5,6]             [11 8 5 2]        [9 8 7]        [3 6 9 12]
# [7,8,9]             [12 9 6 3]        [6 5 4]        [2 5 8 11]
# [10,11,12]                            [3 2 1]        [1 4 7 10]

# x<N, y<M일 때 
# [x,y] 
# 1)[y,-x] 2)[-y,x] 3)[y,M-x-1] 4)[N-y-1,x]