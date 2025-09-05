#백준 #1927 최소 힙
import sys
import heapq

input = sys.stdin.readline

heap = []

N = int(input())

for i in range(N):
    x = int(input())

    #1.x가 자연수인 경우 배열에 X 추가
    if x>0:
        heapq.heappush(heap, x)
    #2.x가 0인 경우 배열에서 가장 작은 값 출력 후 배열에서 해당 값 제거
    if x==0:
        if len(heap)==0:
            print(0)
        else:
            print(heapq.heappop(heap))