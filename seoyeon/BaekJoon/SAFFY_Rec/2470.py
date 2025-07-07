#백준 #2470 두 용액
#투포인터

N = int(input())

all_lst = list(map(int,input().split()))

all_lst.sort()

start, end = 0,N-1
min = float("inf")
answer = [-1,-1]
print("all_lst",all_lst)

def sol(start,end):
    global answer,min
    while True:
        print("start,end",start,end)
        if start>=end:
            break
        #문제에 주어진대로
        cur = all_lst[start]+all_lst[end]
        if abs(cur) < abs(min):
            min = cur
            answer = [all_lst[start], all_lst[end]]
        
        #start,end 처리
        if all_lst[start]+all_lst[end-1] < cur:
            sol(start,end-1)
        sol(start+1,end)

sol(0,N-1)
print(*answer)