#백준 #12912 A와B2
#Greedy

#22:00 - 22:22 
 
# 1. 완전탐색 DFS -> 시간 초과 발생
# (2^10)) 32*32 (2^20) 900*900=810,000 (2^40) 810,000*810,000 = 640,000,000,000

# 2. Greedy? 하다가 해가 아니면 다시 되돌아가는 알고리즘. Stack 사용. T->S
# 1)맨 뒤의 A 삭제
# 2)맨 앞의 B 삭제 후 문자열 뒤집기
from collections import deque

answer = []
def solv(current_str,current_cnt):
    Q = deque(current_str)
    if current_cnt==cnt:
        answer.append(current_str)
        return
    
    if current_str[-1]=="A":
        tmp = current_str[:-1]
        solv(tmp, current_cnt+1)
    if current_str[0]=="B":
        Q.popleft()
        tmp = []
        for _ in range(len(Q)):
            q = Q.pop()
            tmp.append(q)
        solv(tmp, current_cnt+1)

S = list(input())
T = list(input())

cnt=len(T)-len(S) #cnt만큼 연산

solv(T,0)

result = 0
for ans in answer:
    if ans == S:
        result = 1

print(result)