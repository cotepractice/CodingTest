#16:48 - 
#방법
#1. Dijkstra: 한 곳에서 다른 경로까지의 최단 경로
#2. DP 
#3. BFS
#4. DFS

#1. DFS -> recursion 오류 발생
# def dfs(x,y,check):    #check: 벽을 부쉈는지 
    
#     if x==N-1 and y==M-1:
#         return

#     for dx,dy in d:
#         nx = x+dx
#         ny = y+dy
#         if 0<=nx<N and 0<=ny<M:
#             if maps[nx][ny]=="0":
#                 #solv
#                 tmp = distance[nx][ny]
#                 distance[nx][ny] = min(distance[x][y]+1,distance[nx][ny])
#                 dfs(nx,ny,check)
#                 distance[nx][ny] = tmp
#             elif maps[nx][ny]=="1" and check==False:
#                 check=True
#                 #solv
#                 tmp = distance[nx][ny]
#                 distance[nx][ny] = min(distance[x][y]+1,distance[nx][ny])
#                 dfs(nx,ny,check)
#                 distance[nx][ny] = tmp

# # dfs(0,0,False)

# if distance[N-1][M-1]==float("inf"):
#     print(-1)
# else:
#     print(distance[N-1][M-1])

# #2. BFS -> 15% 틀렸습니다
# #시간복잡도 O((N*M)^2)

# #2-1.벽 뚫지 않고 계산 -> bfs()
# #2-2.벽하나 뚫고 계산 -> solv(),bfs()
# #bfs로 해결

# import sys
# from collections import deque

# input = sys.stdin.readline

# N, M = map(int,input().split())
# maps = [[-1 for _ in range(M)] for _ in range(N)]
# distance = [[float("inf") for _ in range(M)] for _ in range(N)]
# distance[0][0] = 1

# walls = []

# for i in range(N):
#     lst = list(input())
#     for j in range(M):
#         maps[i][j]=int(lst[j])
#         if maps[i][j]==1:
#             walls.append([i,j])

# d = [[0,1],[0,-1],[1,0],[-1,0]]

# #2-1. 벽뚫지않고 계산
# def bfs(distance_lst):
#     global ans

#     Q = deque()
#     Q.append([0,0])
#     distance[0][0] = 1

#     while Q:
#         x,y = Q.popleft()

#         for dx,dy in d:
#             nx = x+dx
#             ny = y+dy
#             if 0<=nx<N and 0<=ny<M and maps[nx][ny]==0:
#                 if distance_lst[x][y]+1 < distance_lst[nx][ny]:
#                     distance_lst[nx][ny] = distance_lst[x][y]+1
#                     Q.append([nx,ny])
#     #print("distance",distance_lst)
#     ans = min(ans, distance_lst[N-1][M-1])

# #2-2. 벽 하나 뚫기
# def solv():
    
#     for wall in walls:
#         #distance 매번 재정의
#         distance_tmp = [[float("inf") for _ in range(M)] for _ in range(N)]
#         distance_tmp[0][0]=1
#         tmp = distance_tmp
#         #벽뚫기
#         maps[wall[0]][wall[1]]=0
#         #다시 최단 거리 계산
#         bfs(tmp)
#         #벽복구
#         maps[wall[0]][wall[1]]=1

# ans = float("inf")
# bfs(distance)
# solv()


# if ans == float("inf"):
#     print(-1)
# else:
#     print(ans)

#3. BFS
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int,input().split())
maps = [[-1 for _ in range(M)] for _ in range(N)]

for i in range(N):
    lst = list(input())
    for j in range(M):
        maps[i][j]=int(lst[j])

d = [[0,1],[0,-1],[1,0],[-1,0]]

def bfs():

    Q = deque()
    Q.append([0,0,0])
    
    distance = [[[0]*2 for _ in range(M)] for _ in range(N)] #distance[x][y][c]. 좌표:x,y, c:벽부신적없으면0, 있으면1
    distance[0][0][0]=1

    while Q:
        x,y,c = Q.popleft()

        #가장 먼저 [N-1,M-1]을 만나는 경우의 거리 반환
        #가장 먼저 만날 때의 거리가 가장 짧음 -> 모든 거리가 1로 동일하기 때문
        if x==N-1 and y==M-1:
            return distance[x][y][c]

        for dx,dy in d:
            nx,ny = x+dx,y+dy
            if 0<=nx<N and 0<=ny<M:
                #벽이고, 파괴할 기회 있는 경우
                if  maps[nx][ny]==1 and c==0:
                    #print("HERE1")
                    distance[nx][ny][1]=distance[x][y][0]+1
                    Q.append([nx,ny,1])
                #지나갈 수 있는 경우
                elif maps[nx][ny]==0 and distance[nx][ny][c]==0:
                    distance[nx][ny][c] = distance[x][y][c]+1
                    Q.append([nx,ny,c])
    #[N-1,M-1]까지 도달하지 못 한 경우 -1 반환
    return -1

print(bfs())