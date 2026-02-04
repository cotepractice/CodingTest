#백준 #2473 세 용액
#20:43-21:00

#1. (Python3)시간초과+(Pypy)틀렸습니다
#2. (Pypy)맞았습니다
# O(N^2)
N = int(input())
lst = list(map(int,input().split()))

lst.sort()

ans=float("inf")
ans_lst=[]

#Two Pointer
for idx,val in enumerate(lst):
    left=0
    right=N-1

    while left<right:

        if left==idx:
            left+=1
            continue
        if right==idx:
            right-=1
            continue
        
        s=lst[left]+lst[right]

        if abs(s+val)<ans:
            ans=abs(s+val)
            ans_lst=[lst[left],lst[idx],lst[right]]
        #동일하면 종결
        if abs(s+val)==0:
            ans=0
            ans_lst=[lst[left],lst[idx],lst[right]]
            break
        #Two Pointer
        #elif s<=val: #이렇게 하면 틀림
        elif s+val<0: 
            left+=1
        elif s+val>0:
        #elif s>val: #이렇게 하면 틀림
            right-=1

ans_lst.sort()
print(*ans_lst)
