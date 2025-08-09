#백준 #2623 음악프로그램
#NAVER 코테 대비
#위상정렬
from collections import deque

N, M = map(int,input().split())
connections = [0 for _ in range(N+1)] #앞에 먼저 나와야 하는 다른 가수의 수
graph = [[] for _ in range(N+1)] #graph[a]=[b,c,...]는 a가 먼저 나오고 b,c가 나옴

for m in range(M):

    lst = list(map(int,input().split()))

    lst_n = lst[0]

    #i->j
    for i in range(1,lst_n): #lst[1]~lst[lst_n]
        for j in range(i+1,lst_n+1):
            connections[lst[j]] += 1 #뒤에 나와야하는 j가 앞에 가지는 가수의 수
            graph[lst[i]].append(lst[j]) 

Q = deque() #connections[k]==0인 경우
result = []
for k in range(1,N+1):
    if connections[k]==0:
        Q.append(k)

while Q:
    current_n = Q.popleft()
    result.append(current_n)

    for next in graph[current_n]:
        connections[next] -= 1 
        if connections[next]==0: #앞에 나와야 할 가수가 다 나왔으면 이제 나가도 됨
            Q.append(next)

if len(result)==N:
    print(*result,sep="\n")
else:
    print(0)