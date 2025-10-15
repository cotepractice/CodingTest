#1. RunTime Error (50/100)

#backtracking
def back(current,cnt,n,k):
    global answer
    if current>k:
        return
    
    if current==k:
        answer=min(answer,cnt)
        return
    
    back(current+n,cnt+1,n,k)
    back(current*2,cnt+1,n,k)
    back(current*3,cnt+1,n,k)
    return 
    
answer = float("inf")
def solution(x, y, n):
    
    back(x,0,n,y)
    
    if answer==float("inf"):
        return -1
    else:
        return answer
    
#2.BFS
from collections import deque   

def solution(x, y, n):
    
    Q = deque()
    Q.append([x,0])
    visited=set()
    visited.add(x)
    
    while Q:
        current,cnt = Q.popleft()
        
        if current>y:
            continue
        if current==y:
            return cnt
        
        for next in (current+n,current*2,current*3):
            if next not in visited:
                visited.add(next)
                Q.append([next,cnt+1])
    
    return -1
    

