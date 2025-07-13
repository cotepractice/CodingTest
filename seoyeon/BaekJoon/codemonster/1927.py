import heapq, sys

input = sys.stdin.readline
N = int(input())

heap = []
heapq.heapify(heap)

for _ in range(N):
    x = int(input())
    if x>0:
        heapq.heappush(heap,x)
    else:
        if len(heap)==0:
            print(0)
        else:
            print(heapq.heappop(heap))
    