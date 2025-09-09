#백준 #14501 퇴사
#15:23-15:49

#BruteForce
from itertools import permutations

N = int(input())

T_lst = [0 for _ in range(N)]
P_lst = [0 for _ in range(N)]

maximum = 0

for i in range(N):
    T, P = map(int,input().split())
    T_lst[i]=T
    P_lst[i]=P

def bruteforce(day,cost):
    global maximum

    if day==N:
        maximum = max(maximum, cost)
        return
    
    #day 상담 안 하는 경우
    bruteforce(day+1,cost)
    #day 상담 하는 경우
    if day+T_lst[day]<=N:
        bruteforce(day+T_lst[day], cost+P_lst[day])

bruteforce(0,0)
print(maximum)