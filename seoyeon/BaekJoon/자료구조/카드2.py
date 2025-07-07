#백준 #2164 카드2
#자료구조

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

Q = deque(i+1 for i in range(n))

while len(Q)!=1:
    Q.popleft()
    #print("1",Q)
    if (len(Q) == 1):
        break
    a = Q.popleft()
    #print(Q)
    Q.append(a)
    #print("2",Q)

print(Q.popleft())    