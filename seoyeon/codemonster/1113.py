# #1113 수영장 만들기
# #1. 테케 3,4 실패 -> 벽의 크기가 같은 경우 통과, 다른 경우 실패
# from collections import deque

# N, M = map(int,input().split())
# boards = [[] for _ in range(N)]

# for n in range(N):
#     board = input()
#     boards[n] = board

# d = [[0,-1],[0,1],[1,0],[-1,0]]

# def dfs(x,y,height,visited):
    
#     for dx,dy in d:
#         nx,ny = x+dx,y+dy
#         if 0<=nx<N and 0<=ny<M:
#             if int(boards[nx][ny])<height and visited[nx][ny]==False:
#                 visited[nx][ny]=True
#                 dfs(nx,ny,height,visited)
#             elif int(boards[nx][ny])>height and visited[nx][ny]==False:
#                 visited[nx][ny]=True

# #물이 고이는지 확인
# def cal(visited):
#     for i in range(N):
#         if visited[i][0]==True:
#             return False
#         elif visited[i][M-1]==True:
#             return False

#     for j in range(M):
#         if visited[0][j]==True:
#             return False
#         elif visited[N-1][j]==True:
#             return False
        
#     return True

# def cal_cnt(k):
#     cnt = 0
#     for i in range(1,N-1):
#         for j in range(1,M-1):
#             if visited[i][j]==True:
#                 cnt += k-int(boards[i][j])
#     return cnt

# #k:벽
# ans = 0
# for k in range(2,10):
#     #print("k",k)
#     for i in range(1,N-1):
#         for j in range(1,M-1):
#             visited=[[False for _ in range(M)] for _ in range(N)]
#             visited[i][j]=True
#             dfs(i,j,k,visited)
#             if (cal(visited)):
#                 cnt = cal_cnt(k)
#                 #print("cnt",cnt)
#                 ans = max(ans,cnt)
                
# print(ans)

# #2.
# 1)높이가 k까지 있을 때 k보다 큰 곳은 벽으로 생각 (k는 9부터 2까지)
# 2)고이면 방문처리&물의 양 카운트
import heapq

N, M = map(int,input().split())

boards = [[] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

for n in range(N):
    board = input()
    for b in board:
        boards[n].append(int(b))

d = [[0,-1],[0,1],[-1,0],[1,0]]

heap = []
answer = 0

#외곽 먼저 
for i in range(N):
    for j in range(M):
        if i==0 or i==N-1 or j==0 or j==M-1:
            heapq.heappush(heap, [boards[i][j],i,j])
            visited[i][j]=True

#heapq 사용 [height,x,y]
#height가 작은 순서대로 울타리의 높이가 됨
while heap:
    height, x, y = heapq.heappop(heap)
    #print("Current","x",x,"y",y)
    for dx,dy in d:
        nx = x+dx
        ny = y+dy

        #범위 내에 존재하고 방문한 적 없는 경우만 처리
        if 0<=nx<N and 0<=ny<M and visited[nx][ny]==False:
            #현재 칸보다 낮은 칸은 현재 칸까지 물 채움
            if boards[nx][ny]<height:
                #print("nx",nx,"ny",ny,"boards[nx][ny]",boards[nx][ny])
                answer += (height - boards[nx][ny])
                boards[nx][ny]=height
            
            #boards[nx][ny]가 height보다 높다면 그대로 울타리 형태가 됨
            visited[nx][ny]=True
            heapq.heappush(heap, [boards[nx][ny],nx,ny])
            
print(answer)