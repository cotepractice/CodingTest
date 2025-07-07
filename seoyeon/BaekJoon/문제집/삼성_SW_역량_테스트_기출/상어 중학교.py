# 백준 #21609 상어 중학교
# 삼성 SW 역량 테스트 기출
# 2024 상반기 삼성 신입사원 문제와 유사


#검은색 블록이 -1, 무지개 블록이 0, 일반 블록은 1~M까지
#인접한 칸은 상하좌우만

#블록그룹은 연결된 블록의 집합이며, 
#1)일반 블록이 적어도 하나 있어야하며 일반 블록의 색이 모두 같아야함
#2)검은색 블록은 속하면 안 되고 무지개 블록은 얼마나 있든 상관없음
#3)블록의 개수는 2 이상이어야함
#(?)임의의 한 블록에서 그룹에 속한 인접한 칸으로 이동해 그룹에 속한 모든 칸으로 이동할 수 있어야 함

#1. 크기가 가장 큰 블록 그룹 찾기

#2-1. 1에서 찾은 블록 그룹의 모든 블록 제거
#2-2. 블록 그룹의 수의 제곱만큼 점수 획득
#3. 격자에 중력 작용
# 검은색 블록을 제외한 모든 블록이 행의 번호가 큰 칸(아래)으로 이동
#4. 격자 90도 반시계 방향으로 회전
#5. 격자에 중력

from collections import deque
import copy

#1. 크기가 가장 큰 블록 그룹 찾기.
# -1은 들어가면 안 되고 0은 가능. 일반 블록은 동일한 값이어야함
# 일반 블록 하나는 반드시 존재
def findBlock(graph,x,y):
    numberLst = deque()
    Q = deque()
    color = graph[x][y]
    zero = deque()   #graph[nx][ny]==0인경우 마지막에 visited=False로 변경
    cnt = 0 #블록 총 크기
    rainbowCnt = 0  #rainbow 블록 개수
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    Q.append((x,y))
    visited[x][y] = True    #이때 visited는 외부(main)의 visited를 가져옴
    
    while Q:
        
        i,j = Q.popleft()
        cnt += 1
        numberLst.append((i,j))

        for k in range(4):
            nx = i+dx[k]
            ny = j+dy[k]
            
            if 0<=nx<N and 0<=ny<N:
                
                #조건1. -1은 반드시 제거
                #조건2. 0은 반드시 포함
                #조건3. 1<=graph[nx][ny]<=M인데 color와 같지 않으면 반드시 제거 
                #조건4. graph[nx][ny] == color이면서 visited[nx][ny] == False이면 Q에 추가
                if visited[nx][ny] == True:
                    continue
                if graph[nx][ny] == -1:
                    continue
                elif graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    rainbowCnt += 1
                    Q.append((nx,ny))
                    zero.append((nx,ny))
                elif 1<=graph[nx][ny]<=M:
                    if graph[nx][ny]!=color:
                        continue
                    if visited[nx][ny] == True:
                        continue
                    visited[nx][ny] = True
                    Q.append((nx,ny))

    for k in range(len(zero)):
        i,j = zero.popleft()
        visited[i][j] = False

    #print("FIND",x,y, numberLst)
    return cnt, rainbowCnt, numberLst

#중력
#검은색 블록(-1)을 제외한 모든 블록이 행의 번호가 큰 칸으로 이동
def gravity(graph):
    graph_copy = copy.deepcopy(graph)

    #행은 큰 곳(뒤에서)부터
    for i in range(N-2,-1,-1):   
        for j in range(N):
            minus = False
            #print("i,j",i,j)
            down = i
            if graph[i][j] == -1 or graph[i][j] == -2:
                continue
            
            if 0<=graph[i][j]<=M:
                for k in range(i+1,N):
                    # if minus == True:
                    #     print("1")
                    #     continue
                    
                    if graph_copy[k][j] != -2:
                        down = k-1
                        break
                    down = k
                #print(i,j,graph[i][j],"down",down)
            
            tmp = graph[i][j]
            #기존의 위치는 -2, 이동한 위치는 기존 위치의 값
            if down != i:
                graph_copy[down][j], graph_copy[i][j] = tmp, -2
            
    #print("gravity graph:",graph_copy)
    return graph_copy


#반시계방향으로 90도 회전
def rotate(graph):
    graph_copy = copy.deepcopy(graph)
    for i in range(N):
        for j in range(N):
            nx = (N-1)-j
            ny = i
            #print("i,j",i,j,"nx,ny",nx,ny,"value",graph[i][j])
            graph_copy[nx][ny] = graph[i][j]

    #print(graph)
    #print(graph_copy)
    return graph_copy

#입력
N, M = map(int,input().split()) #N:NxN 격자, M: 블록은 M 이하의 자연수 색

graph = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
        graph[i] = list(map(int,input().split()))
score = 0   #점수

#Main
while True:
    
    visited = [[False for _ in range(N)] for _ in range(N)]
    maxN = 0
    maxRainbowN = 0
    maxNLst = deque()

    #1. 크기가 가장 큰 블록 찾기
    for x in range(N):
        for y in range(N):
            #graph[x][y]가 1부터 M까지인 경우만 실행
            if visited[x][y] == False and 1<=graph[x][y]<=M:
                #1-1. 해당 좌표에서의 dfs 실행
                #print("1 visited",visited)
                blockInfo = findBlock(graph,x,y) #numberLst[0]은 자기자신
                #print("2 visited",visited)

                #1-2. 해당 크기가 max 크기보다 크면 업데이트
                if blockInfo[0] > maxN:
                    maxN = blockInfo[0]
                    maxRainbowN = blockInfo[1]
                    maxNLst= blockInfo[2]
                elif blockInfo[0] == maxN:
                    #rainbow 블럭이 가장 많은 것
                    if blockInfo[1] > maxRainbowN:
                        maxN = blockInfo[0]
                        maxRainbowN = blockInfo[1]
                        maxNLst= blockInfo[2]   
                    elif blockInfo[1] == maxRainbowN:
                        #행이 가장 큰 것
                        if x > maxNLst[0][0]:
                            maxN = blockInfo[0]
                            maxRainbowN = blockInfo[1]
                            maxNLst= blockInfo[2] 
                        elif x == maxNLst[0][0]:
                            #열이 가장 큰 것
                            if y > maxNLst[0][1]:
                                maxN = blockInfo[0]
                                maxRainbowN = blockInfo[1]
                                maxNLst= blockInfo[2] 

    # print("maxN",maxN)
    #print("maxNLst",maxNLst)

    if maxN < 2:
        break
    #2. 블록 제거 및 점수 획득
    for k in range(len(maxNLst)):
        x,y = maxNLst.popleft()
        graph[x][y] = -2
        visited[x][y] = False

    score += maxN**2
    #print("graph",graph)

    #3. 중력 작용
    graph = gravity(graph)
    #print("graph after gravity",graph)

    #4. 90도 반시계 방향으로 회전
    graph = rotate(graph)
    #print("After rotate: ",graph)
    #5. 중력 작용
    graph = gravity(graph)
    #print("graph",graph)
#6. 점수 합
print(score)