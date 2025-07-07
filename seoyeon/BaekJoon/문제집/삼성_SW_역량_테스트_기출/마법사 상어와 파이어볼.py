#백준 #20056 마법사 상어와 파이어볼
#삼성 SW 역량 테스트 기출

from collections import deque

N, M, K = map(int, input().split())
maps = [[0 for _ in range(N)] for _ in range(N)]    #파이어볼 개수
fireballs = [(0,0,0,0,0) for _ in range(M)] #(x,y,질량,속력,방향)

for k in range(M):
    r,c,m,s,d = map(int, input().split())
    fireballs[k] = (r-1,c-1,m,s,d)
    maps[r-1][c-1] += 1

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

def twomore(i,j,separateFireballs,newFireballs):
    #a. 같은 칸의 파이어볼 합치기
    newM = 0
    newS = 0
    newD = (0,2,4,6)
    Dlst = []
    cnt = 0
    maps[i][j] = 4
    #b. 파이어볼이 4개의 파이어볼의 질량,속력,방향 계산
    while True:
        if newFireballs == deque([]):
            break
        r,c,m,s,d = newFireballs.popleft()
        
        if r == i and c == j:
            newM += m
            newS += s
            Dlst.append(d)
            cnt += 1
        else:
            newFireballs.appendleft((r,c,m,s,d))
            break

    newM = newM//5
    #질량이 0이면 소멸 => maps[i][j] == 0, separateFireballs와 newFireballs는 그대로 출력
    if newM == 0: 
        maps[i][j] = 0
        return separateFireballs, newFireballs
    newS = newS//cnt

    #방향 설정
    cnt_odd = False
    cnt_even = False
    for l in range(cnt):
        if Dlst[l]%2==0:
            cnt_even = True
        else:
            cnt_odd = True
    if cnt_even == cnt_odd:
        newD = (1,3,5,7)

    #c. separateFireballs에 추가
    for p in range(4):
        separateFireballs.append((i,j,newM,newS,newD[p]))

    return separateFireballs, newFireballs


for _ in range(K):
    #1. 모든 파이어볼이 자신의 방향과 속력대로 이동
    newFireballsLst = []   #이동한 파이어볼 정보
    for k in range(len(fireballs)):
        r,c,m,s,d = fireballs[k]
        x = (r + s*dx[d]) % N   #격자가 붙어있기때문
        y = (c + s*dy[d]) % N
        maps[r][c] -= 1 #기존 위치에서 파이어볼 제거
        maps[x][y] += 1 #이동한 위치에 파이어볼 추가
        newFireballsLst.append((x,y,m,s,d))
    
    newFireballsLst.sort()
    newFireballs = deque(newFireballsLst)

    separateFireballs = []  #결과적으로 아래 명령 이후에 존재하는 파이어볼
    #2. maps(i,j)의 개수에 따라 처리 
    for i in range(N):
        for j in range(N):
            if newFireballs == deque([]):
                break
            #a) 2개 이상인 경우
            if maps[i][j] >= 2:
                separateFireballs,newFireballs = twomore(i,j,separateFireballs,newFireballs)
            #b) 1개인 경우
            elif maps[i][j] == 1:
                r,c,m,s,d = newFireballs.popleft()
                separateFireballs.append((r,c,m,s,d))
    fireballs = separateFireballs

result = 0
for k in range(len(separateFireballs)):
    result += separateFireballs[k][2]
print(result)