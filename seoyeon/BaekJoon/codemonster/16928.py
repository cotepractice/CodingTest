#16928 뱀과 사다리 게임

# 1. 21% 틀렷습니다
N, M = map(int,input().split())

ladder = dict()
snake = dict()

for n in range(N):
    x,y = map(int,input().split()) #x->y로 이동 (x<y)
    ladder[x] = y

for m in range(M):
    u,v = map(int,input().split()) #u->v로 이동(u>v)
    snake[u] = v

dp = [float('inf') for _ in range(101)] #주사위 굴려야 하는 최소 횟수
dp[1] = 0

current = 1
while True:
    if current == 100: 
        break

    #사다리가 있으면 사다리 타고 온 횟수
    for i in range(1,7):
        next = current+i
        if 1<=next<101:
            dp[next] = min(dp[next], dp[current]+1)
            if next in ladder:
                dp[ladder[next]] = min(dp[ladder[next]], dp[next])
    current += 1

print(dp[100])