#백준 #20057 마법사 상어와 토네이도
#삼성 SW 역량 테스트 기출

N = int(input())
graph = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    graph[i] = list(map(int, input().split()))

tonado_nums = 0 #격자 밖으로 떨어진 모래 양

#이동한 위치로부터 퍼트려질 위치와 비율
left = [(-2,0,0.02),(2,0,0.02),(-1,0,0.07),(1,0,0.07),(1,1,0.01),(-1,1,0.01),(1,-1,0.1),(-1,-1,0.1),(0,-2,0.05),(0,-1,0)]
right = [(x,-y,percentage) for x,y,percentage in left]
down = [(-y,x,percentage) for x,y,percentage in left]
up = [(-x,y,percentage) for x,y,percentage in down]

now = [N//2,N//2]
answer = 0  

def move(cnt,dx,dy,direction):
    global answer
    #왼1,하1,우2,상2,왼3,하3과 같이 해당 숫자가 두 번씩 나오면 1 증가한 숫자만큼 이동해야함
    for _ in range(cnt+1):
        now[0], now[1] = now[0]+dx, now[1]+dy   #now 업데이트. 백준 설명의 "y" 뜻함

        #범위 밖이면 break
        if now[0]<0 or now[1]<0:
            break

        #퍼진 모래 누적
        spreads = 0
        for dx,dy,r in direction:
            nx, ny = now[0]+dx, now[1]+dy   #nx,ny는 모래가 퍼지는 곳의 위치
            #1)퍼지지 않는 모래는 현재 자리에 누적=>알파
            #알파는 맨 마지막에 나타나므로 앞에서 모든 spreads 누적
            if r==0:
                sand = graph[now[0]][now[1]] - spreads
            #2)퍼지는 모래 계산
            else:
                sand = int(graph[now[0]][now[1]] * r)
            #1)범위 안은 graph에 누적
            if 0<=nx<N and 0<=ny<N:
                graph[nx][ny] += sand
            #2)범위 밖은 answer에 누적
            else:
                answer += sand
            #퍼트려진 모래 양 추가
            spreads += sand

for i in range(N):
    #왼쪽과 아래쪽을 한 번에 처리, 오른쪽과 위쪽을 한 번에 처리
    if i%2==0:
        move(i,0,-1,left)   #왼쪽
        move(i,1,0,down)    #아래쪽
    else:
        move(i,0,1,right)   #오른쪽
        move(i,-1,0,up)     #위쪽

print(answer)