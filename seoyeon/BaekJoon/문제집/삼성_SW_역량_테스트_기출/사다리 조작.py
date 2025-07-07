#백준 #15684 사다리 조작
#삼성 SW 역량 테스트 기출

#Input
N, M, H = map(int, input().split())
#M_lst = [[] for _ in range(M)]
line_check = [[False for _ in range(N+1)] for _ in range(H+1)]

for k in range(M):
    a, b = map(int, input().split())
    line_check[a][b] = True

def check():
    for i in range(1, N+1):
        pos = i
        for j in range(1, H+1):
            if line_check[j][pos] == True:
                pos += 1
            elif line_check[j][pos-1] == True:
                pos -= 1
        if pos != i:
            return False
    return True

#x,y는 탐색하는 위치
def BFS(cnt,x,y):
    global result
    #종결 조건
    if result <= cnt:
        return
    if check():
        result = min(result, cnt)
        return
    
    #진행: 세로 하나 잡고 가로 for문 돌리기
    for i in range(x, H+1):
        if i==x:
            now=y
        else:
            now=0
        #print("now,N",now,N)
        for j in range(now, N):
            if line_check[i][j]==False and line_check[i][j+1]==False and line_check[i][j-1]==False:
                line_check[i][j] = True
                BFS(cnt+1, i, j+2)
                line_check[i][j] = False

result = 4
BFS(0,1,1)
if result == 4:
    print(-1)
else:
    print(result)