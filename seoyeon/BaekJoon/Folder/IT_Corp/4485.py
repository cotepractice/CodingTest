#백준 #4485 녹색옷입은애가젤다지?

#17:40-

#도둑루피: 소지한 루피 감소
#각 칸마다 도둑루피 존재. 이 칸을 지나면 도둑루피의 크기만큼 소지금을 잃음
#잃는 금액을 최소로 하여 [N-1][N-1]까지 이동
#상하좌우 인접한 곳으로 1칸씩 이동 가능

#알고리즘: 간선이 서로 달라 BFS로 해결 불가능

#1. Dijkstra: 틀렸습니다
#Dijkstra: 한 노드에서 다른 한 노드까지의 최단 거리
import heapq

cnt=1
while True:
    
    N = int(input())
    distance=[[float("inf") for _ in range(N)] for _ in range(N)]
    boards=[[-1 for _ in range(N)] for _ in range(N)]
    visited=[[False for _ in range(N)] for _ in range(N)]

    if N==0:
        break

    #1.boards 정의
    for i in range(N):
        boards[i]=list(map(int,input().split()))

    #2.Diijkstra
    distance[0][0]=boards[0][0]
    heap=[]
    heapq.heapify(heap)
    heapq.heappush(heap, [boards[0][0],0,0]) #distance,x,y
    visited[0][0]=True

    d=[[0,-1],[0,1],[-1,0],[1,0]]

    while heap:
        current_d, current_x, current_y=heapq.heappop(heap)

        if current_x==N-1 and current_y==N-1:
            print("Problem ",cnt,": ",current_d,sep="")
            break
        
        for dx,dy in d:
            next_x=current_x+dx
            next_y=current_y+dy
            #visited 추가해야 함!
            if 0<=next_x<N and 0<=next_y<N and visited[next_x][next_y]==False:
                visited[next_x][next_y]=True
                next_d = current_d+boards[next_x][next_y]
                distance[next_x][next_y]=next_d
                heapq.heappush(heap,[next_d,next_x,next_y])

    cnt+=1

#2.DP: 테케2 안됨
#상하좌우로 모두 이동할 수 있기 때문! 간선이 모두 달라 x=0 또는 y=0인 경우가 최단 거리임을 확신할 수 없음
# from collections import deque

# cnt=1
# while True:
    
#     N = int(input())
#     distance=[[float("inf") for _ in range(N)] for _ in range(N)]
#     boards=[[-1 for _ in range(N)] for _ in range(N)]

#     if N==0:
#         break

#     #1.boards 정의
#     for i in range(N):
#         boards[i]=list(map(int,input().split()))

    
#     #2.x==0, y==0 업데이트
#     row=boards[0][0]
#     distance[0][0]=boards[0][0]
#     for i in range(1,N):
#         row+=boards[0][i]
#         distance[0][i]=row
    
#     column=boards[0][0]
#     for i in range(1,N):
#         column+=boards[i][0]
#         distance[i][0]=column
    
#     for cx in range(1,N):
#         for cy in range(1,N):
#             d=min(distance[cx-1][cy],distance[cx][cy-1])+boards[cx][cy]
#             distance[cx][cy]=d
    
#     print("HERE DISTANCE")
#     for kk in range(N):
#         print(distance[kk])
    
#     #print("Probelm ",cnt,":",distance[N-1][N-1],sep="")
    
#     cnt+=1
