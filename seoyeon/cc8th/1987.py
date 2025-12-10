#백준 #1987 알파벳

#1. Backtracking. 시간초과
#O(4^(R*C)). (R<=20, C<=20)

from collections import deque

R, C = map(int,input().split())

boards=[[] for _ in range(R)]

for r in range(R):
    boards[r]=list(input())

alpha=set() #alpha
result=0

Q = deque()
Q.append([0,0,0])

d = [[0,1],[0,-1],[1,0],[-1,0]]

#Backtracking

visited = [[False for _ in range(C)] for _ in range(R)]

def backtracking(x,y,cnt,alpha):
    global result

    for dx,dy in d:
        nx=x+dx
        ny=y+dy
        #범위 내 존재 & 방문한 적 없는 경우
        if 0<=nx<R and 0<=ny<C and visited[nx][ny]==False:
            # 1)alpha가 이미 존재
            if boards[nx][ny] in alpha:
                result=max(result,cnt)
            # 2)alpha 존재 X
            # 방문처리 & alpha 추가
            else:
                visited[nx][ny]=True
                alpha.add(boards[nx][ny])
                backtracking(nx,ny,cnt+1,alpha)
                #다음을 위해 복구
                visited[nx][ny]=False
                alpha.remove(boards[nx][ny])

alpha.add(boards[0][0])
visited[0][0]=True
backtracking(0,0,1,alpha)
print(result)

#2. Backtracking. visited를 set()으로 변경. 시간초과

from collections import deque

R, C = map(int,input().split())

boards=[[] for _ in range(R)]

for r in range(R):
    boards[r]=list(input())

alpha=set() #alpha
result=0

Q = deque()
Q.append([0,0,0])

d = [[0,1],[0,-1],[1,0],[-1,0]]

#Backtracking

visited=set()

def backtracking(x,y,cnt,alpha,visited):
    global result

    #print(x,y)

    for dx,dy in d:
        nx=x+dx
        ny=y+dy
        #범위 내 존재 & 방문한 적 없는 경우
        if 0<=nx<R and 0<=ny<C and (nx,ny) not in visited:
            
            # 1)alpha가 이미 존재
            if boards[nx][ny] in alpha:
                result=max(result,cnt)
                continue
            # 2)alpha 존재 X
            # 방문처리 & alpha 추가
            else:
                visited.add((nx,ny))
                alpha.add(boards[nx][ny])
                backtracking(nx,ny,cnt+1,alpha,visited)
                #다음을 위해 복구
                visited.remove((nx,ny))
                alpha.remove(boards[nx][ny])
                

alpha.add(boards[0][0])
visited.add((0,0))
backtracking(0,0,1,alpha,visited)
print(result)

#3. [GPT] visited 할 필요 없음. alpha로만 처리. 시간초과
from collections import deque

R, C = map(int,input().split())

boards=[[] for _ in range(R)]

for r in range(R):
    boards[r]=list(input())

result=0

Q = deque()
Q.append([0,0,0])

d = [[0,1],[0,-1],[1,0],[-1,0]]

def backtracking(x,y,alpha):
    global result

    result=max(result,len(alpha))

    for dx,dy in d:
        nx=x+dx
        ny=y+dy
        if 0<=nx<R and 0<=ny<C and boards[nx][ny] not in alpha:
            backtracking(nx,ny,alpha+[boards[nx][ny]])

backtracking(0,0,[boards[0][0]])
print(result)

#4. 비트마스크 사용. 성공!

from collections import deque

R, C = map(int,input().split())

boards=[[] for _ in range(R)]

for r in range(R):
    boards[r]=list(input())

result=0

Q = deque()
Q.append([0,0,0])

d = [[0,1],[0,-1],[1,0],[-1,0]]

def backtracking(x,y,cnt,mask):
    global result

    #print(mask)

    result=max(result,cnt)

    for dx,dy in d:
        nx=x+dx
        ny=y+dy
        if 0<=nx<R and 0<=ny<C and mask&(1<<(ord(boards[nx][ny])-ord("A"))) == 0:
            idx=ord(boards[nx][ny])-ord("A")
            # if mask&(1<<idx):
            #     continue
            new_mask = mask | (1<<idx)
            backtracking(nx,ny,cnt+1,new_mask)
            
#비트마스크: 초기는 모두 0
#[0,0] 좌표 알파벳 비트마스크 1로 변경
mask=1<<ord(boards[0][0])-ord("A")
backtracking(0,0,1,mask)
print(result)

#5. set()

from collections import deque
def bfs():
    # q 등 필요데이터 생성
    q = deque()
    # v = [[[] for _ in range(C)] for _ in range(R)] # 리스트는 O(N)
    v = [[set() for _ in range(C)] for _ in range(R)] # set는 O(1)
    ans = 1

    # q에 초기데이터(들) 삽입
    q.append((0,0,arr[0][0]))
    v[0][0].add(arr[0][0])

    while q:
        ci,cj,cv = q.popleft()
        ans = max(ans, len(cv))
        # 4방향, 범위내, 중복값이 아닌경우, 중복시퀀스 아닌경우
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<R and 0<=nj<C and arr[ni][nj] not in cv:
                if cv+arr[ni][nj] not in v[ni][nj]:
                    q.append((ni,nj,cv+arr[ni][nj]))
                    v[ni][nj].add((cv+arr[ni][nj]))
    return ans


R, C = map(int, input().split())
arr = list(input() for _ in range(R))

ans = bfs()
print(ans)