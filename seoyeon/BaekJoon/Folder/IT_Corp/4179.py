#백준 #4179 불!

#지훈이 위치와 불 붙은 위치 감안 
#탈출할 수 있는지 여부, 얼마나 빨리 탈출할 수 있는지
from collections import deque
import heapq

R,C = map(int,input().split())
boards = [[] for _ in range(R)]

current = [-1,-1]
fire = []

for i in range(R):
    board = list(input())
    for j in range(C):
        if board[j]=="F":
            fire.append([i,j])
        if board[j]=="J":
            current=[i,j]
    boards[i] = board

#*float("inf")로 처리해야 fire가 없는 경우도 원활히 처리 가능
f_boards = [[float("inf") for _ in range(C)] for _ in range(R)]


d = [[0,1],[0,-1],[1,0],[-1,0]]

#1. 불 확산
#불이 여러 개 존재할 수 있음 -> 동시 확산 구현
# def spread(f_boards):
#     heap=[]
#     heapq.heapify(heap)
#     #visited=[[False for _ in range(C)] for _ in range(R)]
#     #print("fire",fire)
    
#     for ff in range(len(fire)):
#         heapq.heappush(heap, [0, fire[ff][0],fire[ff][1]])
    
#     while heap:
#         cnt,fx,fy = heapq.heappop(heap)
#         f_boards[fx][fy]=cnt
        
#         for dx,dy in d:
#             nx=fx+dx
#             ny=fy+dy
#             if 0<=nx<R and 0<=ny<C and boards[nx][ny]!="#" and cnt+1<f_boards[nx][ny]:
#                 heapq.heappush(heap,[cnt+1,nx,ny])

#     return f_boards

#*heapq는 시간 초과, bfs 통과!
def spread(f_boards):
    q = deque()
    
    # fire 배열에 이미 여러 개의 불 시작점이 있다고 가정
    for fx, fy in fire:
        q.append((0, fx, fy))  # (시간, x, y)

    while q:
        cnt, fx, fy = q.popleft()
        f_boards[fx][fy] = cnt
        
        for dx, dy in d:
            nx = fx + dx
            ny = fy + dy
            
            # 범위 체크 + 벽이 아니고, 더 빠른 시간으로 업데이트 가능한 경우만
            if 0 <= nx < R and 0 <= ny < C:
                if boards[nx][ny] != "#" and cnt + 1 < f_boards[nx][ny]:
                    f_boards[nx][ny] = cnt + 1
                    q.append((cnt + 1, nx, ny))

    return f_boards

f_boards=spread(f_boards)
#print(f_boards)

#2. 이동
# 1)이동할 수 있는 위치 탐색
# 2)이동할 수 있으면 이동: 이동할 수 있는 곳: ".", "불이 나지 않은 공간"
# 3)더이상 이동할 수 있는 곳이 없거나 탈출하면 종결
Q=deque()
Q.append([current[0],current[1],0])
visited=[[False for _ in range(C)] for _ in range(R)]
visited[current[0]][current[1]]=True
answer=float("inf")

while Q:
    x,y,cnt=Q.popleft()
    #print("x,y,cnt",x,y,cnt)

    for dx,dy in d:
        nx=x+dx
        ny=y+dy
        #종결 조건: 탈출
        if nx<0 or nx>=R or ny<0 or ny>=C:
            #print("here",nx,ny,cnt+1)
            answer=min(answer,cnt+1)
            break

        #이동: 아직 불 타지 않고 방문한 적 없는 경우
        if cnt+1<f_boards[nx][ny] and boards[nx][ny]!="#" and visited[nx][ny]==False:
            visited[nx][ny]=True
            Q.append([nx,ny,cnt+1])

if answer==float("inf"):
    print("IMPOSSIBLE")
else:
    print(answer)