#백준 17484 진우의 달 여행 (Small)
#DP
#풀이참고

N, M = map(int, input().split())

oil_lst = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    oil_lst[i] = list(map(int, input().split()))


#[조건]
#1. 움직일 수 있는 방향은 [1,-1], [1,0], [1,1]
#2. 같은 방향으로 두 번 연속 움직일 수 없음
#출력: 최대한 연료를 아껴 달에 착륙할 수 있는 연료의 최솟값

#[풀이]
#범위: 1<=x<N 
#cnt_lst[x][y] 값 계산. 해당 값은 cnt_lst[x][y]="min(oil_lst[x-1][y-1],oil_lst[x-1][y],oil_lst[x-1][y+1])+oil_lst[x][y]"
#같은 방향으로 두 번 갈 수 없도록 

cnt_lst = [[[] for _ in range(M)] for _ in range(N)]

#[x,y,z]에서 x,y는 좌표, z=0이면 왼쪽, 1은 위, 2는 오른쪽에서 오는 경우
#dp_lst[x][y]는 x-1까지 소요된 최소 연료양. x 위치가 아닌 x-1 위치임을 생각할 것
#따라서 N+1로 한 번 더 진행해야 됨
dp_lst = [[[0,0,0] for _ in range(M)]] + [[[float('inf'), float('inf'), float('inf')] for _ in range(M)] for _ in range(N)] 

for i in range(1,N+1): #N-1까지가 아닌 N까지 진행하는 이유는 dp_lst[x][y]는 oil_lst[x][y]를 더하기 전 값이기 때문
    for j in range(M):
        #i-1 -> i 로 이동할 때 어느 방향에서 왔는지 
        #dp_lst[i][j][0], dp_lst[i][j][1], dp_lst[i][j][2]는 각각 오른쪽,위쪽,왼쪽에서 접근하는 경우
        
        #1.오른쪽에서 오는 경우, min은 i-2에서 i-1로 들어온 값 중 최소값 선택. j는 어느 방향에서 오느냐에 따라 고정됨. dp_lst의 세번째 파라미터는 현재 위쪽에서 오면 왼쪽과 오른쪽만 생각하도록 함
        if j < M-1:
            dp_lst[i][j][0] = min(dp_lst[i-1][j+1][1], dp_lst[i-1][j+1][2]) + oil_lst[i-1][j] #i-2번째값 + i-1번째값
        #2.왼쪽에서 오는 경우
        if 0 < j:
            dp_lst[i][j][2] = min(dp_lst[i-1][j-1][0],dp_lst[i-1][j-1][1]) + oil_lst[i-1][j] #i-2번째값 + i-1번째값
        #3.위쪽에서 오는 경우
        dp_lst[i][j][1] = min(dp_lst[i-1][j][0], dp_lst[i-1][j][2]) + oil_lst[i-1][j]

ans = float('inf')
for lst in dp_lst[N]:
    for val in lst:
        if val < ans:
            ans = val
print(ans)