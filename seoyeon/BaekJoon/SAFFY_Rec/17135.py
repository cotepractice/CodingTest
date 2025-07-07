#백준 #17135 캐슬 디펜스
from itertools import combinations
from collections import deque
from copy import deepcopy

def solv(x,y,z,d):
    global board
    maps = deepcopy(board)

    solv_ans = 0
    N_pos = [[N,x],[N,y],[N,z]]

    Q_lst = [] #적의 좌표 

    for i in range(N):
        for j in range(M):
            if maps[i][j]==1:
                Q_lst.append([i,j])

    Q = deque(Q_lst) #적의 좌표
    
    while True:
        N_min = [[float("inf"),-1,-1],[float("inf"),-1,-1],[float("inf"),-1,-1]]
        
        #1.궁수와 가장 가까운 좌표 탐색:N_min [가장가까운거리,적의x좌표,적의y좌표]
        while Q:
            x,y = Q.popleft()

            for k in range(3):
                m = abs(x-N) + abs(y-N_pos[k][1])
                if m<=d and m<N_min[k][0]:
                    N_min[k] = [m,x,y]
                elif m<=d and m==N_min[k][0]:
                    if y<N_min[k][2]:
                        N_min[k] = [m,x,y]
        #print("N_min:",N_min)
        #2.적 공격   
        for k in range(3):
            min_d,min_x,min_y = N_min[k]
            
            #공격할 수 있는 적이 없는 경우
            if min_d==float('inf'):
                continue
            #공격할 수 있는 적이 있는 경우
            if maps[min_x][min_y]==1:
                maps[min_x][min_y]=0
                solv_ans += 1 
                Q_lst.remove([min_x,min_y]) #공격받은 적 제거
        
        #3. 남은 적 위치 업데이트: Q에 남은 적 위치 추가 및 maps 업데이트  
        #for i 에서 i가 큰 순서대로 진행해야 함 ->
        Q = deque()
  
        tmp_lst = []
        #print("Q_lst1:",Q_lst)
        Q_lst.sort(key=lambda x : x[0],reverse=True)
        #print("Q_lst2:",Q_lst)
        for k in range(len(Q_lst)):
            x,y = Q_lst[k]

            #maps에 남아 있으면 자리 업데이트
            if x+1<N:
                maps[x][y]=0
                maps[x+1][y]=1
                tmp_lst.append([x+1,y])
            else:
                maps[x][y]=0
        
        #print("tmp_lst:",tmp_lst)
        #남은 적이 없는 경우 종료
        if len(tmp_lst)==0:
            return solv_ans
        
        #print("MAPS")
        # for i in range(N):
        #     print(maps[i])

        Q = deque(tmp_lst)
        Q_lst = tmp_lst



N,M,D = map(int,input().split())

board = [[0 for _ in range(M)] for _ in range(N+1)]

for i in range(N):
    lst = list(map(int, input().split()))
    board[i] = lst

#1. M개 중 3개의 조합 찾기
m_lst = [i for i in range(M)]
combi = list(combinations(m_lst,3))

ans = 0

#2. 조합
for c in combi:
    x,y,z = c
    #print("c",c)
    a = solv(x,y,z,D)
    if a>ans:
        ans = a

print(ans)