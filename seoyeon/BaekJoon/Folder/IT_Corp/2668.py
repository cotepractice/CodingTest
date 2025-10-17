#백준 #2668 숫자고르기

#DFS
from collections import deque

N = int(input())
N_lst = []

#index와 값 모두 0~N-1까지
for _ in range(N):
    x=int(input())
    N_lst.append(x-1)

result=[]
for i in range(N):
    visited=[False for _ in range(N)]
    
    Q = deque()
    Q.append(i)
    visited[i]=True
    check=0

    while Q:
        x = Q.popleft()

        next=N_lst[x]

        #다음 인덱스
        if visited[next]==False:
            check=1
            visited[next]=True
            Q.append(next)

        #종결조건: 사이클 계산 ! 한 바퀴 돈 경우 i는 넣어도 됨
        elif visited[next]==True and next==i:
            result.append(i)
            break

result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i]+1)