#백준 #15684 사다리조작
#8:22-

N,M,H = map(int,input().split())
ladders = [[False for _ in range(N)] for _ in range(H)]

for m in range(M):
    a, b = map(int,input().split()) #a:H, b:b와 b+1 연결
    ladders[a-1][b-1]=True

answer = float("inf")

#O(N*H)
def check():

    #**current에 맞춰 h 진행! n에 맞추는 것 아님
    for n in range(N):
        current = n
        for h in range(H):
            if current>0 and ladders[h][current-1]:
                current -= 1
            elif ladders[h][current]:
                current += 1
        if current!=n:
            return False
        
    return True
    #** 리스트 만들 필요 없음 -> 시간초과
    # parents = [i for i in range(N)]

    # for i in range(H):
    #     for j in range(N-1):
    #         if ladders[i][j]==True:
    #             parents[j], parents[j+1] = parents[j+1], parents[j]

    # for k in range(N):
    #     if parents[k]!=k:
    #         return False
    # return True

#전체 시간복잡도 O((N*H)^2)
#ladders를 모두 돌면서 backtracking
#ladders[x][y]가 False일 때 True로 변경 후 다시 추적
def backtracking(x,y,cnt):
    global answer

    if check():
        answer = min(answer,cnt)
        return
    
    if cnt>=3 or cnt>=answer:
        return

    #y>N-1인 경우 현재 x에서 탐색할 ladder 없음
    #**이렇게 하면 안 됨!
    # if y>N-1:
    #     x+=1
    #     y=0

    #i는 x부터 H-1, j는 y부터 N-2
    #j는 j와 j+1을 연결하는지 확인하기 때문
    for i in range(x,H):
        #** j는 i==x일 때 y부터, 그 이후로는 0부터 
        if i==x:
            now=y
        else:
            now=0
        for j in range(now,N-1):
            #두 가로선이 연속하면 안 되므로!
            #ladders[i][j]. 즉, j와 j+1 연결 -> j+2와 j+3 연결 확인 필요
            #**ladders[i][j+1]도 False여야 함. ladders[i][j-1]은 elif에서 탐색
                    
            #1.ladder False
            if ladders[i][j]==False and ladders[i][j+1]==False:
                if j>0 and ladders[i][j-1]==True:
                    continue
                ladders[i][j]=True
                backtracking(i,j+2,cnt+1)
                ladders[i][j]=False
            # #2.ladders True
            # elif ladders[i][j]:
            #     backtracking(i,j+2,cnt)

backtracking(0,0,0)

if answer==float("inf"):
    print(-1)
else:
    print(answer)