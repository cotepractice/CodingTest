#백준 #1261 알고스팟
#23:07-23:20
#BFS
from collections import deque

M,N=map(int,input().split())
maps = ["" for _ in range(N)]

for i in range(N):
    maps[i]=input()

def dijkstra():
    distance = [[float("inf") for _ in range(M)] for _ in range(N)]
    d = [[0,1],[0,-1],[1,0],[-1,0]]

    Q = deque() #[x,y,cost]
    Q.append([0,0,0])
    distance[0][0]=0

    while Q:
        current_x,current_y,current_cost = Q.popleft()
        if current_cost>distance[current_x][current_y]:
            continue

        for dx,dy in d:
            next_x,next_y = current_x+dx,current_y+dy
            if 0<=next_x<N and 0<=next_y<M:
                if maps[next_x][next_y]=="0":
                    if current_cost<distance[next_x][next_y]:
                        distance[next_x][next_y] = current_cost
                        Q.append([next_x,next_y,current_cost])

                else:
                    if current_cost+1<distance[next_x][next_y]:
                        distance[next_x][next_y] = current_cost+1
                        Q.append([next_x,next_y,current_cost+1])

    return distance[N-1][M-1]

print(dijkstra())