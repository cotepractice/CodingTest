#백준 #10816 숫자카드2

from collections import defaultdict
N = int(input())
N_lst = list(map(int,input().split()))
M = int(input())
M_lst = list(map(int,input().split()))

dict = defaultdict(int)

for i in range(N):
    if N_lst[i] in dict:
        dict[N_lst[i]] += 1
    else:
        dict[N_lst[i]] = 1

answer = []
for i in range(M):
    if M_lst[i] in dict:
        answer.append(dict[M_lst[i]])
    else:
        answer.append(0)
print(*answer)