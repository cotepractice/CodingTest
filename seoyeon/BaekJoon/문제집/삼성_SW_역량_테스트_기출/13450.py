#백준 #13460 구슬탈출2
#구현, dfs

#이동 동작
#왼쪽,오른쪽,위,아래로 기울이기
#최소 몇 번만에 빨간 구슬을 빼낼 수 있는지. 파란 구슬은 빼낼 수 없음
#10번 이하로 빼낼 수 없으면 -1 출력

#상하좌우 이동

# 1. DFS

# N,M = map(int,input().split())
# boards = [[] for _ in range(N)] # ".":빈칸, "#":공이이동할 수 없는 장애물 또는 벽, "0":구멍, "R":빨간구슬위치, "B":파란구슬위치

# rx,ry,bx,by,hx,hy = -1,-1,-1,-1,-1,-1
# for i in range(N):
#     lst = list(input())
#     boards[i]=lst
#     for j in range(M):
#         if boards[i][j]=="R":
#             rx,ry = i,j
#         elif boards[i][j]=="B":
#             bx,by = i,j

# answer = 11

# dir = [[0,1],[0,-1],[1,0],[-1,0]]

# def move(x,y,d):
#     cnt = 0

#     #현재 위치가 구멍이 아니고, 다음이 벽도 아니면 이동
#     #즉, 현재 위치가 구멍이거나 다음이 벽이면 이동하지 않음
#     while boards[x+dir[d][0]][y+dir[d][1]]!="#" and boards[x][y]!="O":
#         x += dir[d][0]
#         y += dir[d][1]
#         cnt += 1
    
#     return [cnt,x,y]


# def dfs(rx,ry,bx,by,cnt):
#     global answer

#     if cnt>10:
#         return
    
#     rrcnt,bbcnt = 0,0

#     #상하좌우로 이동
#     for d in range(4):
#         rrcnt, rrx, rry = move(rx,ry,d)
#         bbcnt, bbx, bby = move(bx,by,d)

#         #1.파란 구슬이 구멍에 들어가면 실패
#         if boards[bbx][bby]=="O":
#             continue # *return이 아닌 continue 해야함

#         #2.빨간 구슬이 구멍에 들어가면 성공
#         if boards[rrx][rry]=="O":
#             answer = min(answer,cnt)
#             return

#         #겹치는 경우 멀리서 온 구슬 재배치
#         if rrx==bbx and rry==bby:
#             if rrcnt>bbcnt:
#                 rrx -= dir[d][0]
#                 rry -= dir[d][1]
#             elif rrcnt<bbcnt:
#                 bbx -= dir[d][0]
#                 bby -= dir[d][1]
        
#         dfs(rrx,rry,bbx,bby,cnt+1)

# dfs(rx,ry,bx,by,1)

# if answer==11:
#     print(-1)
# else:
#     print(answer)

#####
#2. BFS

from collections import deque

N,M = map(int,input().split())
boards = [[] for _ in range(N)] # ".":빈칸, "#":공이이동할 수 없는 장애물 또는 벽, "0":구멍, "R":빨간구슬위치, "B":파란구슬위치

rx,ry,bx,by,hx,hy = -1,-1,-1,-1,-1,-1
for i in range(N):
    lst = list(input())
    boards[i]=lst
    for j in range(M):
        if boards[i][j]=="R":
            rx,ry = i,j
        elif boards[i][j]=="B":
            bx,by = i,j

visited = []
answer = 11

dir = [[0,1],[0,-1],[1,0],[-1,0]]

def move(x,y,d):
    cnt = 0
    #멈추는방법: 다음이 벽인 경우, 현재가 구멍인 경우
    while (boards[x+dir[d][0]][y+dir[d][1]]!="#" and boards[x][y]!="O"):
        x += dir[d][0]
        y += dir[d][1]
        cnt += 1
    return [cnt,x,y]

def bfs(rx,ry,bx,by):
    global answer

    Q = deque()
    Q.append([rx,ry,bx,by,1])
    visited.append((rx,ry,bx,by))

    while Q:
        
        rx,ry,bx,by,cnt = Q.popleft()
        
        if cnt > 10:
            break

        for d in range(4):
            rcnt,rrx,rry=move(rx,ry,d)
            bcnt,bbx,bby=move(bx,by,d)

            #파란 구슬이 들어가면 종료. 다음 위치로 이동
            if boards[bbx][bby]=="O":
                continue
            #빨간 구슬이 들어가면 계속 진행
            if boards[rrx][rry]=="O":
                answer = min(answer,cnt)
                return #종결
            #동일한 위치인 경우
            if rrx==bbx and rry==bby:
                if rcnt>bcnt:
                    rrx -= dir[d][0]
                    rry -= dir[d][1]
                else:
                    bbx -= dir[d][0]
                    bby -= dir[d][1]
            
            if (rrx,rry,bbx,bby) not in visited:
                visited.append((rrx,rry,bbx,bby))
                Q.append([rrx,rry,bbx,bby,cnt+1])             

bfs(rx,ry,bx,by)

if answer==11:
    print(-1)
else:
    print(answer)