#백준 #16236 아기 상어
#삼성 SW 역량 테스트 기출
from collections import deque

n = int(input())
region = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    region[i] = list(map(int, input().split()))

x,y = -1,-1

for i in range(n):
    for j in range(n):
        if region[i][j] == 9: #같아도 지나갈 수는 있는데 먹는 것은 안 됨
            x=i
            y=j

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(x,y):
    visited = [[0 for _ in range(n)] for _ in range(n)] #떨어져있는 거리 측정
    Q = deque([(x,y)])
    canEat = []  #먹을 수 있는 물고기 좌표 및 떨어진 거리 
    visited[x][y] = 1

    while Q:

        i,j = Q.popleft()

        for k in range(4):
            nx = i+dx[k]
            ny = j+dy[k]

            if (0<=nx<n and 0<=ny<n and visited[nx][ny]==0):
                
                #1) 현재 위치에서 먹을 수 있는 경우 => 이동&먹기 :visited[nx][ny] = visited[x][y]+1 & canEat
                if region[x][y] > region[nx][ny] and region[nx][ny] != 0:
                    visited[nx][ny] = visited[i][j] + 1
                    canEat.append((visited[nx][ny]-1,nx,ny))  #먹을 수 있는 물고기를 찾은 경우 주변을 더 탐색(bfs)하지 않음

                #2) 먹지는 못 하지만 이동할 수는 있는 경우 => 이동만 가능
                elif region[nx][ny] == region[x][y]:
                    visited[nx][ny] = visited[i][j] + 1
                    Q.append((nx,ny))

                #3) 물고기가 없는 경우 => 이동 가능
                elif region[nx][ny] == 0:
                    visited[nx][ny] = visited[i][j] + 1
                    Q.append((nx,ny))
    
    #문제에 주어진 순서로 정렬 => 1)거리 2)x좌표 3)y좌표
    return sorted(canEat, key=lambda x:(x[0],x[1],x[2]))

size = [2,0]    #size[0]은 상어 무게, size[1]은 먹은 물고기 개수. 같아지면 무게 1 증가
t = 0

#main
while True:
    region[x][y] = size[0]  #해당 위치에 상어 무게 두기
    canEat = deque(bfs(x,y))


    #더이상 먹을 수 있는 물고기가 없는 경우
    if canEat == deque([]):
        break
    
    #먹을 물고기 존재 => 가장 앞쪽의 물고기 선택
    distance,px,py = canEat.popleft()
    t += distance   #가는데 걸리는 거리를 1초로 계산
    size[1] += 1    #먹었으니 먹은 개수 증가

    #몇개를 먹었는지 체크
    if size[0] == size[1]:
        size[0] += 1
        size[1] = 0

    region[x][y] = 0
    x,y=px,py

print(t)