#백준 #2573 빙산
#16:49 - 17:57

# # 1. PyPy3로 해결. BUT Python3의 경우 시간 초과 발생
# # 시간측정->1.84초 (start_time=time.time(), end_time=time.time(), end_time-start_time)
# # #시간복잡도 O(N*M)
# from collections import deque
# import copy

# #solv() -> O(1)
# def solv(x,y):
#     d = [[-1,0],[1,0],[0,-1],[0,1]]
#     water = 0

#     for dx,dy in d:
#         nx = x+dx
#         ny = y+dy
#         if 0<=nx<N and 0<=ny<M and mountains[nx][ny]==0:
#             water += 1
    
#     if (mountains[x][y]-water)>=0:
#         return mountains[x][y]-water
#     else:
#         return 0

# #bfs() -> O(10,000).X는 빙산 개수.최대 10,000
# def bfs(x,y,visited):
#     d = [[-1,0],[1,0],[0,-1],[0,1]]
    
#     Q=deque()
#     Q.append([x,y])

#     while Q:
#         xx,yy = Q.popleft()
#         for dx,dy in d:
#             nx = xx+dx
#             ny = yy+dy
#             if 0<=nx<N and 0<=ny<M and mountains[nx][ny]!=0 and visited[nx][ny]==False:
#                 visited[nx][ny]=True
#                 Q.append([nx,ny])

#     return visited

# #count() -> O(N*M)
# def count():
#     visited = [[False for _ in range(M)] for _ in range(N)]
#     mountains_n = 0
#     for i in range(N):
#         for j in range(M):
#             if mountains[i][j]!=0 and visited[i][j]==False:
#                 if mountains_n==0:
#                     mountains_n += 1
#                     visited[i][j]=True
#                     visited = bfs(i,j,visited)
#                 #빙하가 2 이상인 경우 더 계산할 필요없음
#                 else:
#                     return 2

#     return mountains_n

# ## 시간제한:1초 = 20,000,000 (=2*10^7)
# ## 3<=N,M<=300, 빙산이 차지하는 칸의 개수는 10,000개 이하
# N,M = map(int,input().split())
# mountains = [[0 for _ in range(M)] for _ in range(N)]
# for n in range(N):
#     mountains[n]=list(map(int,input().split()))

# t = 0
# while True:
#     t += 1
#     #초당 빙산 업데이트
#     change = copy.deepcopy(mountains)

#     for i in range(N):
#         for j in range(M):
#             if mountains[i][j]>0:
#                 change[i][j] = solv(i,j) #바로 mountains에 적용하면 안 됨
    
#     #변경사항 한 번에 적용
#     mountains = change

#     #종료: (원하던 결과) 빙산 분리 
#     if count()==2:
#         break
#     #종료: 빙산이 다 녹을 때까지 분리되지 않은 경우 0 출력
#     elif count()==0:
#         t=0
#         break

# print(t)

#---------------

#2. Python3로 해결
#
from collections import deque

#solv() -> O(1)
def solv(x,y):
    d = [[-1,0],[1,0],[0,-1],[0,1]]
    water = 0

    for dx,dy in d:
        nx = x+dx
        ny = y+dy
        if 0<=nx<N and 0<=ny<M and mountains[nx][ny]==0:
            water += 1
    
    if (mountains[x][y]-water)>=0:
        return mountains[x][y]-water
    else:
        return 0

#bfs() -> O(10,000).X는 빙산 개수.최대 10,000
def bfs(x,y):
    d = [[-1,0],[1,0],[0,-1],[0,1]]
    
    visited[x][y]=True
    Q=deque()
    Q.append([x,y])

    while Q:
        xx,yy = Q.popleft()
        for dx,dy in d:
            nx = xx+dx
            ny = yy+dy
            if 0<=nx<N and 0<=ny<M and mountains[nx][ny]!=0 and visited[nx][ny]==False:
                visited[nx][ny]=True
                Q.append([nx,ny])

    return visited

## 시간제한:1초 = 20,000,000 (=2*10^7)
## 3<=N,M<=300, 빙산이 차지하는 칸의 개수는 10,000개 이하
N,M = map(int,input().split())
mountains = [[0 for _ in range(M)] for _ in range(N)]
for n in range(N):
    mountains[n]=list(map(int,input().split()))

ice_lst = []
for i in range(N):
    for j in range(M):
        if mountains[i][j]!=0:
            ice_lst.append([i,j])

t = 0
while True:
    t += 1
    #초당 빙산 업데이트
    change = [item[:] for item in mountains] #[Point1.deepcopy는 시간복잡도가 커 슬라이스로 변환]

    for i in range(N):
        for j in range(M):
            if mountains[i][j]>0:
                change[i][j] = solv(i,j) #바로 mountains에 적용하면 안 됨
    
    #변경사항 한 번에 적용
    mountains = change

    #BFS
    visited = [[False for _ in range(M)] for _ in range(N)]
    cnt = 0 #빙하 덩어리 개수
    for x,y in ice_lst: #[Point2.이중for문이 아닌 ice_lst로 변경]
        if mountains[x][y]!=0 and visited[x][y]==False:
            cnt += 1
            bfs(x,y)

    if cnt>=2:
        break
    elif cnt==0:
        t=0
        break
print(t)