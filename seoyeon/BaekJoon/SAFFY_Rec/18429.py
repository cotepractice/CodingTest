#백준 #18429 근손실
import heapq
from collections import deque

N, K = map(int, input().split()) #N개의 운동 키트 존재, 매일 K만큼 중량 감소

exercise = list(map(int, input().split()))

power = 0 #운동 증감

check = [False for _ in range(N)]
result = 0

def f(cnt, weight):
    global result

    if weight < 0:
        return
    if cnt >= N:
        result += 1
        return
    for i in range(N):
        if check[i]==False:
            check[i] = True
            f(cnt+1, weight+exercise[i]-K)
            check[i] = False

f(0,0)

print(result)