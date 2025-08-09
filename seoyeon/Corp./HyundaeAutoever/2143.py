import bisect

T = int(input())

N = int(input())
N_lst = list(map(int,input().split()))
M = int(input())
M_lst = list(map(int,input().split()))

Nsum = []
Msum = []

for i in range(N):
    s = N_lst[i]
    Nsum.append(s)
    for j in range(i+1,N):
        s+=N_lst[j]
        Nsum.append(s)

for i in range(M):
    s = M_lst[i]
    Msum.append(s)
    for j in range(i+1,M):
        s+=M_lst[j]
        Msum.append(s)

Nsum.sort()
Msum.sort()
answer = 0 

#T = Nsum+Msum 이므로 Msum = T-Nsum
for i in range(len(Nsum)):
    l = bisect.bisect_left(Msum,T-Nsum[i])
    r = bisect.bisect_right(Msum,T-Nsum[i])
    answer += r-l 
print(answer)