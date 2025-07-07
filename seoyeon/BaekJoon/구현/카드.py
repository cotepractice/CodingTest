#백준 #2161 카드
#구현

from collections import deque

n = int(input())

lst = deque((i+1) for i in range(n))

result = [-1 for i in range(n-1)]

for i in range(n-1):
    #print("i",i)
    first = lst.popleft()
    result[i] = first
    second = lst.popleft()
    lst.append(second)

print(*result, lst.popleft())