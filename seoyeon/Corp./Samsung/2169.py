
#해결 방법: 1)dp 2)dfs 3)bfs
#bfs -> 로봇이 얻는 가치가 모두 동일하지 않기 때문에 불가능
#dfs -> 같은 지점을 여러 번 방문하는 중복 문제 발생. 로봇이 오른쪽으로 갔다가 왼쪽으로 돌아올 수 있어 시간복잡도 초과
N,M = map(int,input().split())

boards = [[0 for _ in range(M)] for _ in range(N)]
dp1 = [[-float("inf") for _ in range(M)] for _ in range(N)]
dp2 = [[-float("inf") for _ in range(M)] for _ in range(N)]
dp = [[-float("inf") for _ in range(M)] for _ in range(N)]

for i in range(N):
    lst = list(map(int,input().split()))
    boards[i]=lst

#왼쪽->오른쪽으로 이동 & 위->아래로 이동
def solv1(idx,start):
    global dp1

    #처음엔 반드시 위에서 오기
    dp1[idx][start] = boards[idx][start]+dp[idx-1][start]
    start += 1
    #이후로는 왼쪽에서 오거나 위에서 오는 경우 둘 다 계산
    while True:
        if start==M:
            return
        dp1[idx][start] = boards[idx][start] + max(dp1[idx][start-1],dp[idx-1][start])
        start += 1
    

#오른쪽->왼쪽으로 이동 & 위->아래로 이동
def solv2(idx,start):
    global dp2

    #처음엔 반드시 위에서 오기
    dp2[idx][start] = boards[idx][start] + dp[idx-1][start]
    start -= 1
    #이후로는 오른쪽에서 오거나 위에서 오는 경우 둘 다 계산
    while True:
        if start==-1:
            return
        dp2[idx][start] = boards[idx][start] + max(dp2[idx][start+1], dp[idx-1][start])
        start -= 1


#dp[x][y]에서 x==0인 경우, y==0인 경우 dp 값 업데이트
dp[0][0]=boards[0][0]

for i in range(1,M):
    dp[0][i] = dp[0][i-1]+boards[0][i]

for i in range(1,N):
    solv1(i,0)
    solv2(i,M-1)

    for j in range(M):
        dp[i][j] = max(dp1[i][j], dp2[i][j])


print(dp[N-1][M-1])