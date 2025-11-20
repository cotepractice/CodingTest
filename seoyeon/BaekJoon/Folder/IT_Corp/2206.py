#백준 #2206 벽 부수고 이동하기

#9:15-10:30

#0:이동가능, 1:이동불가능.벽
#(1,1)->(N,M)으로 최단거리 이동
#벽을 한 개 부수고 경로가 짧아지면 부수고 이동

# #1. O(len(walls)*(N*M)). 시간초과 발생
# from collections import deque

# N,M = map(int,input().split())
# boards = [[] for _ in range(N)]

# for n in range(N):
#     boards[n]=list(input())

# walls = []

# for i in range(N):
#     for j in range(M):
#         if boards[i][j]=="1":
#             walls.append([i,j])

# def move(boards):
#     d=[[0,1],[0,-1],[1,0],[-1,0]]
#     visited=set()
#     dp=[[float("inf") for _ in range(M)] for _ in range(N)]

#     Q = deque()
#     Q.append([0,0,1])
#     visited.add((0,0))

#     while Q:
#         cx,cy,cnt = Q.popleft()
#         dp[cx][cy]=cnt

#         for dx,dy in d:
#             nx=cx+dx
#             ny=cy+dy
#             if 0<=nx<N and 0<=ny<M and boards[nx][ny]=="0" and (nx,ny) not in visited:
#                 visited.add((nx,ny))
#                 Q.append([nx,ny,cnt+1])

#     return dp[N-1][M-1]

# answer=float("inf")
# for wx,wy in walls:
#     boards[wx][wy]="0"
#     res=move(boards)
#     answer=min(answer,res)
#     boards[wx][wy]="1"

# if answer==float("inf"):
#     print(-1)
# else:
#     print(answer)


#2. 
from collections import deque

N,M = map(int,input().split())
boards = [[] for _ in range(N)]

for n in range(N):
    boards[n]=list(input())

d=[[0,1],[0,-1],[1,0],[-1,0]]

def bfs():
    Q = deque() #[x,y,check].check=0인 경우 벽 부순적없음, 1인 경우 부순적있음
    Q.append([0,0,0]) 
    distance = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(2)]
    distance[0][0][0]=1

    while Q:
        x,y,check=Q.popleft()

        #종결조건
        if x==N-1 and y==M-1:
            return distance[check][x][y]

        for dx,dy in d:
            nx=x+dx
            ny=y+dy
            if 0<=nx<N and 0<=ny<M:
                #1. 이동 가능하고 처음 방문하는 경우
                #BFS 문제 해결 시 방문 처리(distance[check][x][y]==0)하지 않으면 메모리 초과 발생
                if boards[nx][ny]=="0" and distance[check][nx][ny]==0:
                    distance[check][nx][ny]=distance[check][x][y]+1
                    Q.append([nx,ny,check])
                #2. 벽이고, 부순적없고, 처음 방문하는 경우 부술 수 있음
                if boards[nx][ny]=="1" and check==0 and distance[1][nx][ny]==0:
                    distance[1][nx][ny]=distance[check][x][y]+1
                    Q.append([nx,ny,1])
                    
    return -1

print(bfs())