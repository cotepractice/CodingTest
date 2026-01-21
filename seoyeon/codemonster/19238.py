#백준 #19238 스타트 택시
#삼성 SW 역량 테스트 기출

from collections import deque

N, M, amount = map(int, input().split())
Maps = [[0 for _ in range(N)] for _ in range(N)]
taxi = [0,0]
customers = [[0,0,0,0] for _ in range(M)]

for i in range(N):
    Maps[i] = list(map(int, input().split()))

tx,ty = map(int, input().split())
taxi = [tx-1, ty-1]

passenger_start = []
passenger_end = []

for j in range(M):
    sx,sy,ex,ey = list(map(int, input().split()))  #[시작x, 시작y, 도착x, 도착y]
    passenger_start.append([sx-1,sy-1])
    passenger_end.append([ex-1,ey-1])

#택시와 승객 사이의 거리
dx = [0,0,-1,1]
dy = [-1,1,0,0]

#최단 경로의 손님 찾는 함수
def findPassenger(taxi):
    Q = deque()
    Q.append(taxi)
    visited = [[0 for _ in range(N)] for _ in range(N)]
    minDistance = float('inf')
    candidate = []  #최단 경로인 승객 저장. 모든 승객 저장하는 것이 아님. "최단 경로" 승객만!
    while Q:
        x, y = Q.popleft()
        #종결조건
        if visited[x][y] > minDistance:
            break
        #좌표가 승객의 출발지점 좌표인 경우
        if [x,y] in passenger_start:
            minDistance = visited[x][y]
            candidate.append([x,y])
        else:
            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]
                if 0<=nx<N and 0<=ny<N and Maps[nx][ny]==0 and visited[nx][ny]==0:
                    visited[nx][ny] = visited[x][y] + 1
                    Q.append([nx,ny])
    #최단 경로 승객을 최단 거리, 행, 열로 정렬              
    if candidate:
        candidate.sort()
        return visited[candidate[0][0]][candidate[0][1]], candidate[0][0], candidate[0][1]
    #도달할 수 있는 손님이 없는 경우
    else:
        return -1,-1,-1

#손님의 목적지로 가는 함수
def goDestination(start, end):
    Q = deque()
    Q.append(start)
    visited = [[0 for _ in range(N)] for _ in range(N)]
    while Q:
        x, y =Q.popleft()
        #종결조건
        if [x,y] == end:
            break
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0<=nx<N and 0<=ny<N and Maps[nx][ny]==0 and visited[nx][ny]==0:
                visited[nx][ny] = visited[x][y] + 1
                Q.append([nx,ny])
    return visited[x][y], x, y

for _ in range(M):
    distance, px, py = findPassenger(taxi)
    #최단 거리의 승객을 찾을 수 없거나 or 가는 길에 연료가 떨어지는 경우
    if distance == -1 or amount-distance < 0:
        amount = -1
        break
    amount -= distance

    #최단 경로의 손님의 index 찾기
    idx = passenger_start.index([px,py])
    #손님을 태웠으므로 findPassenger에서 제외
    passenger_start[idx] = [-1,-1]
    #목적지까지 이동
    distance2, px2, py2 = goDestination([px,py], passenger_end[idx])
    #도착지에 도달하지 못 하거나 or 가는 길에 연료가 떨어지는 경우
    if [px2, py2] != passenger_end[idx] or amount - distance2 < 0:
        amount = -1
        break

    #정상적으로 목적지에 도달한 경우
    amount += distance2
    #택시 위치 이동
    taxi = [px2,py2]

print(amount)