#백준 #11866 요세푸스 문제0
#구현 문제

from collections import deque

n, k = map(int, input().split())

lst = [(i+1) for i in range(n)]
Q = deque((i+1) for i in range(n))
result = []


while (lst != []):
    #print("f")
    for i in range(k):
        first = Q.popleft()
        if (i != k-1):
            Q.append(first)
    result.append(first)
    if (first in lst):
        lst.remove(first)
    #print(first, lst, result)

print("<",end="")
for i in range(n-1):
    print(result[i],end=", ")
print(result[n-1], end = "")
print(">",end="")