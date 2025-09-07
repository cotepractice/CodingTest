#백준 #14499 주사위 굴리기



#지도의 각 칸에는 정수 존재

#N,M: 지도 크기 (N*M)
#x,y: 주사위 놓은 곳의 좌표
#K: 명령 개수
N,M,x,y,K = map(int,input().split())

boards = [[-1 for _ in range(M)] for _ in range(N)]

dice = [0,0,0,0,0,0] #전개도에서 맨 위부터 -> 왼쪽 -> 오른쪽

for i in range(N):
    board = list(map(int,input().split()))
    boards[i]=board

#이동 명령 1.동쪽(오른쪽) 2.서쪽(왼쪽) 3.북쪽(위) 4.남쪽(아래)
commands = list(map(int,input().split()))

#동서남북

def right():
    global dice
    dice[4],dice[1],dice[5],dice[3] = dice[3],dice[4],dice[1],dice[5]
    return

def left():
    global dice
    dice[4],dice[1],dice[5],dice[3] = dice[1],dice[5],dice[3],dice[4]
    return

def up():
    global dice
    dice[0],dice[1],dice[2],dice[3] = dice[1],dice[2],dice[3],dice[0]
    return

def down():
    global dice
    dice[0],dice[1],dice[2],dice[3] = dice[3],dice[0],dice[1],dice[2]
    return

def move(c):
    if c==1:
        right()
    elif c==2:
        left()
    elif c==3:
        up()
    else:
        down()

#동서북남
dir = [[0,1],[0,-1],[-1,0],[1,0]]

nx,ny = x,y
for command in commands:
    
    nx += dir[command-1][0]
    ny += dir[command-1][1]

    if 0<=nx<N and 0<=ny<M:
        
        move(command)
        #1.주사위 굴린 후 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥 면에 쓰여 있는 수가 칸에 복사
        #2.0이 아닌 칸이면, 칸에 쓰여 있는 수가 주사위 바닥면으로 복사되고 칸에 쓰여 있는 수는 0이 됨
        if boards[nx][ny]==0:
            boards[nx][ny]=dice[3]
        else:
            dice[3]=boards[nx][ny]
            boards[nx][ny]=0
        print(dice[1])

    else:
        nx -= dir[command-1][0]
        ny -= dir[command-1][1]
