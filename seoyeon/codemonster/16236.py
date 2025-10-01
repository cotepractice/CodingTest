#백준 #16236 아기상어
from collections import defaultdict
import heapq

N = int(input())
boards=[[-1 for _ in range(N)] for _ in range(N)]
shark = [-1,-1,0] #[x좌표,y좌표,먹은 같은 크기 물고기 개수]
shark_n=2
fishes=defaultdict(list)
cnt=0

t=0

for i in range(N):
    boards[i]=list(map(int,input().split()))
    for j in range(N):
        if boards[i][j]==9:
            shark=[i,j,0]
        if 0<boards[i][j]<7:
            fishes[cnt]=[i,j]
            cnt+=1

#M마리 물고기, 1마리 아기상어
#물고기와 아기 상어 모두 크기를 가지고, 가장 처음 아기 상어 크기는 2
#아기상어 이동
#1.1초에 상하좌우로 인접한 한 칸씩 이동
#2.자신의 크기보다 큰 물고기는 지날 수 없고, 나머지 칸은 지날 수 있음
#3.자기보다 크기 작은 물고기 먹을 수 있음. 크기가 같은 물고기는 먹을 수 없지만 지나갈 수는 있음
# 더 이상 먹을 수 있는 물고기가 공간에 없으면 엄마 상어에게 도움 요청
# 먹을 수 있는 물고기가 1마리면 그 물고기 먹으러 감
# 먹을 수 있는 물고기가 1마리보다 많으면, 거리가 가장 가까운 물고기 먹으러 감
#   거리는 아기상어가 있는 칸에서 물고기 있는 칸으로 이동할 때 지나야하는 칸의 개수의 최솟값
#   가까운 물고기가 많다면 가장 위에 있는 물고기, 그러한 물고기가 여러마리면 가장 왼쪽에 있는 물고기 먹음
# 이동시 1초 걸리고, 자신의 크기와 같은 수의 물고기를 먹을 때마다 크기가 1증가

#출력: 이동하는 물고기 위치
#O(N*N)
def bfs(x,y):
    visited=[[False for _ in range(N)] for _ in range(N)]
    lst = [] #먹을 수 있는 물고기
    d=[[0,1],[0,-1],[1,0],[-1,0]]
    heap = []
    heapq.heapify(heap)
    heapq.heappush(heap,[0,x,y])
    visited[x][y]=True
    min_n = float("inf") #먹을 수 있는 물고기가 있는 최단거리

    while heap:
        cnt,cx,cy = heapq.heappop(heap)
        
        #종결조건: cnt가 min_n보다 큰 경우 더 할 필요없음
        if cnt>min_n:
            break
        #종결조건: boards 값이 1,2,3,4,5,6 즉 물고기 크기라면 lst에 넣어 반환
        #먹을 수 있는 물고기 탐색
        if 0<boards[cx][cy]<shark_n and (cx!=shark[0] or cy!=shark[1]):
            if cnt<min_n:
                lst = [[cx,cy,cnt]]
                min_n=cnt
                continue
            elif cnt==min_n:
                lst.append([cx,cy,cnt])
                continue

        for dx,dy in d:
            nx=cx+dx
            ny=cy+dy
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==False:
                #자신보다 크면 안 됨
                if boards[nx][ny]<=shark_n:
                    visited[nx][ny]=True
                    heapq.heappush(heap, [cnt+1,nx,ny])
    
    #지나야하는 칸의 개수의 최솟값
    lst.sort(key=lambda x:(x[0],x[1]))

    if len(lst)==0:
        return []
    else:
        return lst[0]

#시간복잡도 O((N*N)*(N*N))
while True:
    #1.상하좌우에서 먹을 수 있는 물고기 탐색
    #먹을 수 있는 물고기 possible=[x좌표,y좌표,거리]
    #BFS
    possible = bfs(shark[0],shark[1])
    if len(possible)==0:
        print(t)
        break
    
    #2.물고기 먹기
    nx,ny,cnt = possible
    boards[nx][ny]=0
    shark[2]+=1

    if shark[2]==shark_n:
        shark_n+=1
        shark[2]=0
    
    #3. 상어 위치 이동
    boards[shark[0]][shark[1]]=0
    shark[0],shark[1]=nx,ny
    boards[shark[0]][shark[1]]=9

    t+=cnt
