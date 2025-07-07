#백준 #3190 뱀
#삼성 SW 역량 테스트 기출
from collections import deque

snake = deque([(0,0)])

N = int(input())    #보드의 크기 N
Maps = [[0 for _ in range(N)] for _ in range(N)]    #사과가 존재하면 1, 뱀이 존재하면 2, 아무것도 없으면 0

K = int(input())    #사과의 개수 K
for i in range(K):
    x, y = map(int, input().split())
    Maps[x-1][y-1] = 1

L = int(input())    #방향 전환 횟수 L
Directions = [(0,0) for _ in range(L)]  #방향 전환: (n,D) or (n,L). n초 후에 D는 오른쪽으로 회전, L은 왼쪽으로 회전
for i in range(L):
    x, y = input().split()
    Directions[i] = (x,y)

x,y = 0,0   #좌표
dx = 0      #이동방향
dy = 1
d = [(0,1),(1,0),(0,-1),(-1,0)] #인덱스가 증가하면 오른쪽으로 회전, 감소하면 왼쪽으로 회전


#매초 진행되는 방식
#1. 뱀의 머리를 다음 칸에 위치 
#2. 만약 벽이나 자기자신과 닿으면 게임 종료
#3. 만약 이동한 칸에 사과 있다면, 그 칸의 사과는 없어지고 꼬리 움직이지 않음. 몸길이 변함
#4. 만약 이동한 칸에 사과 없다면, 몸길이를 줄여 꼬리의 칸을 비움. 즉 몸길이는 변하지 않음
changeDirectionIdx = 0    #Directions index. 방향 전환을 위한 Directions의 index
dIdx = 0    #d의 index.이동방향 dxdy
t = 0

tails_x, tails_y = snake.popleft()  #꼬리 좌표

while True:

    #1. 매초 반복
    x += dx
    y += dy

    #a) 벽이나 뱀 몸통 부딪히는 경우
    if x<0 or x>=N or y<0 or y>=N or Maps[x][y] == 2:
        t += 1
        print(t)
        break

    #b) 사과 있는 경우, 사과 사라지고 머리 존재
    elif Maps[x][y] == 1:
        Maps[x][y] = 2
        snake.append((x,y))

    #c) 뱀도, 사과도 없이 비어있는 경우, 머리는 두고 꼬리를 뗌
    else:
        Maps[x][y] = 2
        snake.append((x,y))
        Maps[tails_x][tails_y] = 0
        tails_x,tails_y = snake.popleft()   #꼬리 위치 변경

    #2. t 증가 & 방향 변경
    t += 1
    
    if changeDirectionIdx>=L:   #L번 방향을 바꾼 후에는 더이상 방향을 바꾸지 않음
        continue
    if t == int(Directions[changeDirectionIdx][0]):
        if Directions[changeDirectionIdx][1] == "L":  #왼쪽으로 90도 회전
            dIdx -= 1
            if dIdx<0:
                dIdx = dIdx%4
            dx = d[dIdx][0]
            dy = d[dIdx][1]
            
        else:   #오른쪽으로 90도 회전
            dIdx += 1
            if dIdx>=4:
                dIdx = dIdx%4
            dx = d[dIdx][0]
            dy = d[dIdx][1]
            
        changeDirectionIdx += 1
