#백준 #12100 2048(Easy)
#19:38-

#구현, BFS
# 상하좌우 네 방향 중 하나로 이동
# 같은 값을 가지는 두 블록이 충돌하면 하나로 합쳐짐 + 더한 값으로 됨
# 한 번의 이동에서 이미 합쳐진 블록은 또 다른 블록과 다시 합쳐질 수 없음
# 똑같은 수가 세 개 있는 경우 이동하려고 하는 쪽의 칸이 먼저 합쳐짐. Ex. 위로 이동하는 경우 위쪽 블록이 먼저 합쳐짐
# 최대 5번 이동으로 만들 수 있는 가장 큰 블록의 값 계산

from collections import deque

N = int(input())
boards = [[0 for _ in range(N)] for _ in range(N)]
answer = 0

for i in range(N):
    boards[i] = list(map(int,input().split()))

def up(boards):
    visited = set()

    tmp_boards = [[0 for _ in range(N)] for _ in range(N)]

    #모두 넣기
    for j in range(N):
        stack = deque()
        for i in range(N):
            #존재하면 이동
            #이동할 때 합칠 수 있는지 확인: 이미 합쳐지지 않고, 값이 같아야 함
            if boards[i][j]>0:
                stack.append(boards[i][j])
    
        #합칠 수 있는지 확인
        #앞의 좌표가 방문한 적 없고, 값이 같은 경우
        i_idx = 0
        while stack:
            x=stack.popleft()
            if i_idx-1>=0 and (i_idx-1,j) not in visited and tmp_boards[i_idx-1][j]==x:
                visited.add((i_idx-1,j))
                tmp_boards[i_idx-1][j] *= 2
            else:
                tmp_boards[i_idx][j]=x
                i_idx+=1 
            
    # for k in range(N):
    #     print(*tmp_boards[k])
    return tmp_boards

def down(boards):
    visited = set()

    tmp_boards = [[0 for _ in range(N)] for _ in range(N)]

    #모두 넣기
    for j in range(N):
        stack = deque()
        for i in range(N-1,-1,-1):
            #존재하면 이동
            #이동할 때 합칠 수 있는지 확인: 이미 합쳐지지 않고, 값이 같아야 함
            if boards[i][j]>0:
                stack.append(boards[i][j])
    
        #합칠 수 있는지 확인
        #앞의 좌표가 방문한 적 없고, 값이 같은 경우
        i_idx = N-1
        while stack:
            x=stack.popleft()
            if i_idx+1<N and (i_idx+1,j) not in visited and tmp_boards[i_idx+1][j]==x:
                visited.add((i_idx+1,j))
                tmp_boards[i_idx+1][j] *= 2
            else:
                tmp_boards[i_idx][j]=x
                i_idx-=1
    
    # for k in range(N):
    #     print(*tmp_boards[k])
    return tmp_boards

def left(boards):
    visited = set()

    tmp_boards = [[0 for _ in range(N)] for _ in range(N)]

    #모두 넣기
    for i in range(N):
        stack = deque()
        for j in range(N):
            #존재하면 이동
            #이동할 때 합칠 수 있는지 확인: 이미 합쳐지지 않고, 값이 같아야 함
            if boards[i][j]>0:
                stack.append(boards[i][j])
    
        #합칠 수 있는지 확인
        #앞의 좌표가 방문한 적 없고, 값이 같은 경우
        j_idx = 0
        while stack:
            x=stack.popleft()

            if j_idx-1>=0 and (i,j_idx-1) not in visited and tmp_boards[i][j_idx-1]==x:
                visited.add((i,j_idx-1))
                tmp_boards[i][j_idx-1] *= 2
            else:
                tmp_boards[i][j_idx]=x
                j_idx+=1
    
    # for k in range(N):
    #     print(*tmp_boards[k])
    return tmp_boards

def right(boards):
    visited = set()

    tmp_boards = [[0 for _ in range(N)] for _ in range(N)]

    #모두 넣기
    for i in range(N):
        stack = deque()
        for j in range(N-1,-1,-1):
            #존재하면 이동
            #이동할 때 합칠 수 있는지 확인: 이미 합쳐지지 않고, 값이 같아야 함
            if boards[i][j]>0:
                stack.append(boards[i][j])
    
        #합칠 수 있는지 확인
        #앞의 좌표가 방문한 적 없고, 값이 같은 경우
        j_idx = N-1
        while stack:
            x=stack.popleft()
            if j_idx+1<N and (i,j_idx+1) not in visited and tmp_boards[i][j_idx+1]==x:
                visited.add((i,j_idx+1))
                tmp_boards[i][j_idx+1] *= 2
            else:
                tmp_boards[i][j_idx]=x
                j_idx-=1
    
    # for k in range(N):
    #     print(*tmp_boards[k])
    return tmp_boards

#up(boards)
#down(boards)
#left(boards)
#right(boards)

def check(boards):
    max_n = 0
    for i in range(N):
        for j in range(N):
            max_n = max(max_n,boards[i][j])
    return max_n

def solv(cnt,boards):
    global answer
    if cnt==5:
        ans=check(boards)
        answer=max(ans,answer)
        return
    
    solv(cnt+1,up(boards))
    solv(cnt+1,down(boards))
    solv(cnt+1,left(boards))
    solv(cnt+1,right(boards))


solv(0,boards)
print(answer)