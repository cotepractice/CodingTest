#백준 #2075 N번째 큰 수
import heapq

N = int(input())

heap = list(map(int,input().split())) #heap에 큰 수 N개 넣기
heapq.heapify(heap)

for i in range(N-1):
    lst = list(map(int,input().split()))
    for next in lst:
        current_min = heapq.heappop(heap)
        if next>current_min:
            heapq.heappush(heap,next)
        else:
            heapq.heappush(heap,current_min)

print(heapq.heappop(heap))