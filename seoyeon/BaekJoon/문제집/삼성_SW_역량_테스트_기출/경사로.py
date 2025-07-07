#백준 #14890 경사로 문제
#삼성 SW 역량 테스트 기출
#14:54-15:57
#16:05-16:16
#16:43-17:43


N, L = map(int, input().split())

lst = [[0 for i in range(N)] for i in range(N)]
dp = [[True for i in range(N)] for i in range(N)]   #경사로가 놓이면 False

for i in range(N):
    lst[i] = list(map(int, input().split()))

def pos(now):
    for i in range(1,N):    #1부터 시작
        #2 이상 차이나는 경우
        if abs(now[i]-now[i-1]) > 1:
            return False
        #뒤의 index가 더 큰 경우 => 경사로를 앞에 둬야함
        elif (now[i] > now[i-1]):
            for k in range(L):
                #앞의 index인 i-1과 비교
                #1)같은 높이가 아니거나 2)N보다 범위가 같거나 커지거나 3)이미 경사로가 있는 경우 제외
                if (i-k-1 < 0) or (now[i-1] != now[i-k-1]) or (dp[i-k-1] == True):
                    return False
                if (now[i-1] == now[i-k-1]):
                    dp[i-k-1] = True

        #앞의 index가 더 큰 경우 => 경사로를 뒤에 둬야함
        elif (now[i] < now[i-1]):
            for k in range(L):
                #1)같은 높이가 아니거나 2)N보다 범위가 같거나 커지거나 3)이미 경사로가 있는 경우 제외
                #*index 확인을 가장 앞에 둬야함
                if (i+k >= N) or (now[i] != now[i+k]) or (dp[i+k] == True):
                    return False
                if (now[i] == now[i+k]):
                    dp[i+k] = True
    return True

cnt = 0

for i in range(N):
    dp = [False for _ in range(N)]
    if pos(lst[i]): #True를 반환할 경우 cnt 증가
        cnt += 1

for i in range(N):
    dp = [False for _ in range(N)]
    #*lst의 세로를 새로운 list 형태로 만들어야함
    if pos([lst[j][i] for j in range(N)]):
        cnt += 1

print(cnt)