#1. 완전탐색 -> 4% 틀렸습니다
N = int(input()) #N: 최대 100
n_lst = [-1 for _ in range(N)]

for i in range(N):
    k = int(input())
    n_lst[i]=k

ans = dict() #1부터 시작
 
#현재 상황
for i in range(N):
    if i+1==n_lst[i]:
        ans[i+1]=0

#완전탐색
for i in range(N):
    if i in ans:
        continue
    for j in range(N):
        if j in ans:
            continue
        
        if n_lst[i]==j+1 and n_lst[j]==i+1:
            ans[i+1]=0
            ans[j+1]=0
        elif n_lst[j]==i+1:
            ans[i+1]=0
            n_lst[i]=j+1
        elif n_lst[i]==j+1:
            ans[j+1]=0
            n_lst[j]=i+1

print(len(ans))
for i in range(1,N+1):
    if i in ans:
        print(i)