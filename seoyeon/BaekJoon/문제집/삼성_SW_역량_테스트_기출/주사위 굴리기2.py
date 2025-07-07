#백준 #23288 주사위 굴리기2

from collections import deque

N,M,k = map(int, input().split())

graph = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    graph[i] = list(map(int, input().split()))

#동쪽으로 굴릴 때 인덱스 증가, 서쪽으로 굴릴 때 인덱스 감소:아랫면의 수
dice_lr = [3,1,4,6]
#남쪽으로 굴리면 인덱스 증가, 북쪽으로 굴릴 때 인덱스 감소:아랫면의 수
dice_ud = [5,1,2,6]

#동남서북. 시계방향
dir = [(0,1),(1,0),(0,-1),(-1,0)]
dir_k = 0

#getPoint => bfs 사용
def getPoint(graph,x,y):
    visited = [[0 for _ in range(M)] for _ in range(N)]
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    B = graph[x][y]
    Q = deque()
    Q.append((x,y))
    visited[x][y] = 1
    cnt = 1

    while Q:
        mx,my = Q.popleft()
        for i in range(4):
            nx = mx+dx[i]
            ny = my+dy[i]

            if 0<=nx<N and 0<=ny<M:
                if visited[nx][ny] == 0:
                    if graph[nx][ny] == B:
                        cnt += 1
                        #print("nxny",nx,ny)
                        visited[nx][ny] = 1
                        Q.append((nx,ny))

    answer = cnt * B    #점수
    return answer

#방향 변경
def changeDir(dice_n,map_n,dir_k):
    if dice_n>map_n:
        dir_k = (dir_k+1)%4
    elif dice_n<map_n:
        dir_k = (dir_k-1)%4
    return dir_k

x,y = 0,0
dice = [1,2,3,4,5,6]
ans = 0

for l in range(k):
    #칸을 넘어가는 경우 방향 변경
    if not 0<=x+dir[dir_k][0]<N or not 0<=y+dir[dir_k][1]<M:
        dir_k = (dir_k+2)%4
    
    x, y = x+dir[dir_k][0], y+dir[dir_k][1]

    ans += getPoint(graph,x,y)

    #이동 방향별로 dice 변경
    if dir_k == 0:  #동
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif dir_k == 1:    #남
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
    elif dir_k == 2:    #서
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    else:   #북
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    
    #방향 변경
    dir_k = changeDir(dice[5],graph[x][y],dir_k)

print(ans)