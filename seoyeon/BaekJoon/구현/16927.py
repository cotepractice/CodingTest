#백준 #16927 배열 돌리기 2

from collections import deque

N,M,R = map(int, input().split())

N_maps = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    l = list(map(int, input().split()))
    N_maps[i] = l

rotate_N = min(N,M)//2 #겹의 갯수
answer_maps = [[0 for _ in range(M)] for _ in range(N)]

for i in range(rotate_N):
    Q = deque() #위,오른쪽,아래,왼쪽 순서
    for k in range(i,M-i-1):
        Q.append(N_maps[i][k])
    for k in range(i,N-i-1):
        Q.append(N_maps[k][M-i-1])
    for k in range(M-i-1,i,-1):
        Q.append(N_maps[N-i-1][k])
    for k in range(N-i-1,i,-1):
         Q.append(N_maps[k][i])
    
    Q.rotate(-R)

    for k in range(i,M-i-1):
        answer_maps[i][k] = Q.popleft()
    for k in range(i,N-i-1):
        answer_maps[k][M-i-1] = Q.popleft()
    for k in range(M-i-1,i,-1):
        answer_maps[N-i-1][k] = Q.popleft()
    for k in range(N-i-1,i,-1):
        answer_maps[k][i] = Q.popleft()

    
for i in range(N):
    print(*answer_maps[i], sep=" ",end="\n")