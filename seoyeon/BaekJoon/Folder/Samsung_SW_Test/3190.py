#백준 #3190 뱀
#20:40-22:00
from collections import defaultdict

N = int(input())
K = int(input())
apples = defaultdict(list)
directions = dict() #directions의 [x,c]는 x초가 끝난 후 L이면 왼쪽, R이면 오른쪽으로 90도 회전

for _ in range(K):
    x,y = map(int,input().split())
    if x-1 in apples:
        apples[x-1].append(y-1)
    else:
        apples[x-1]=[y-1]

L = int(input())

for _ in range(L):
    x,c = input().split()
    directions[int(x)]=c

#뱀이 벽 또는 자기자신의 몸과 부딪히면 게임 종료
#게임은 맨 위 맨 좌측에 위치하고 뱀의 길이는 1이며 오른쪽을 향함
#매초 아래와 같은 규칙 따름
#1.몸길이를 늘려 머리를 다음칸에 위치
#2.벽이나 자기자신의 몸과 부딪히면 게임 종료
#3.만약 이동한 칸에 사과가 있다면, 그 칸의 사과 사라지고 꼬리 움직이지 않음
#4.만약 이동한 칸에 사과가 없다면, 몸길이를 줄여 꼬리가 위치한 칸을 비움->몸길이 변하지 않음

#D인 경우 dir 인덱스 1 증가, L인 경우 인덱스 1 감소
#오른쪽 -> 아래 -> 왼쪽 -> 위
dir = [[0,1],[1,0],[0,-1],[-1,0]]
snakes = []

#오른쪽으로 8 >(8D)> 아래로 2 >(10D)> 왼쪽으로 1 >(11D)>위쪽으로 2 >(13D)>왼쪽으로 

x,y = 0,0
t = 0
d = 0

snakes.append([0,0])
while True:
    
    # [t초동안 이동]
    #1.몸 길이 늘려 머리를 다음칸에 위치
    nx = x+dir[d][0]
    ny = y+dir[d][1]

    #2.종결조건
    #2-1.범위내존재
    if nx<0 or nx>=N or ny<0 or ny>=N:
        break
    #2-2.자기자신과 부딪히는 경우
    if [nx,ny] in snakes:
        break

    #몸을 늘림
    snakes.append([nx,ny])

    #3.이동한 칸 사과 확인
    #3-1.사과 존재하는 경우, 꼬리 없애지 않아도 되고 사과 제거
    if nx in apples and ny in apples[nx]:
        lst=apples[nx]
        lst.remove(ny)
        apples[nx]=lst

    #3-2.사과 존재하지 않는 경우, 꼬리 제거
    else:
        del snakes[0]
    
    t += 1
    x,y = nx,ny

    # [t초 끝난 후 회전 진행]
    #4.방향 회전 있는 경우
    if t in directions:
        if directions[t]=="L":
            d-=1
            if d<0:
                d+=4
        else:
            d+=1
            if d>3:
                d-=4
    
print(t+1)


