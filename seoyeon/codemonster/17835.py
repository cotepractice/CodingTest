#백준 #17835 면접보는 승범이네
import heapq,sys

input = sys.stdin.readline

N,M,K = map(int,input().split())

connections = [[] for _ in range(N)]

for m in range(M):
    u,v,c=map(int,input().split())
    connections[v-1].append([c,u-1])
 
starts = list(map(int,input().split()))
distance = [float("inf") for _ in range(N)]

heap = []
heapq.heapify(heap)

for s in starts:
    heapq.heappush(heap,[0,s-1])
    distance[s-1]=0

while heap:
    current_d,current = heapq.heappop(heap)
    
    if distance[current]<current_d:
        continue

    for next_d,next in connections[current]:
        d = current_d+next_d
        if d<distance[next]:
            distance[next]=d
            heapq.heappush(heap,[d,next])

answer = [0,-1] #[가장먼도시번호,거리]
for idx,dd in enumerate(distance):
    if answer[1]<dd:
        answer[0]=idx
        answer[1]=dd

print(answer[0]+1)
print(answer[1])