#백준 #13911 집 구하기
import heapq,sys

input = sys.stdin.readline #안 하면 시간초과

#V: 정점개수, E:도로개수
V, E = map(int,input().split())

connections = [[] for _ in range(V)] 

for e in range(E):
    u,v,w = map(int,input().split())
    #양방향
    connections[u-1].append([w,v-1])
    connections[v-1].append([w,u-1])

#M:맥도날드 수, x:맥세권 조건
M, x = map(int,input().split())
#m_lst: 맥도날드 정점.이때 이때 인덱스 빼야 함
m_lst = list(map(int,input().split()))

#S:스타벅스 수, y:스세권 조건
S, y = map(int,input().split())
#s_lst: 스타벅스 정점. 이때 인덱스 1 빼야 함
s_lst = list(map(int,input().split()))

#맥도날드
m_heap = []
m_distance = [float("inf") for _ in range(V)]
heapq.heapify(m_heap)
for mm in m_lst:
    heapq.heappush(m_heap,[0,mm-1]) #핵심! 아무 맥도날드에서나 가장 가까운 거리를 구하면 되기 때문
    m_distance[mm-1]=0

while m_heap:
    current_d, current = heapq.heappop(m_heap)

    #현재 거리가 m_distance 값보다 크면 더이상 진행 X
    if m_distance[current]<current_d:
        continue

    for next_d, next in connections[current]:
        d = current_d+next_d
        if d<m_distance[next]:
            m_distance[next]=d
            heapq.heappush(m_heap,[d,next])

#헷갈릴 수 있는 경우: Dijkstra는 한 지점에서 출발한다고 했으므로 for문으로 m_lst를 돌면서 heapq 사용하면 안 됨 
#시간복잡도 O(len(m_lst) * E log V)
# for mm in m_lst:
#     heap = []
#     heapq.heapify(heap)
#     heapq.heappush(heap,[0,mm])

#     while heap:
#         current_d,current = heapq.heappop(heap)
#         ...(계속)

#스타벅스
s_heap = []
s_distance = [float("inf") for _ in range(V)]
heapq.heapify(s_heap)
for ss in s_lst:
    heapq.heappush(s_heap,[0,ss-1])
    s_distance[ss-1]=0

while s_heap:
    current_d, current = heapq.heappop(s_heap)

    #현재 거리가 m_distance 값보다 크면 더이상 진행 X
    if s_distance[current]<current_d:
        continue

    for next_d, next in connections[current]:
        d = current_d+next_d
        if d<s_distance[next]:
            s_distance[next]=d
            heapq.heappush(s_heap,[d,next])

answer = float("inf")
for idx in range(V):
    #맥도날드거나 스타벅스면 더이상 진행 X
    if m_distance[idx]==0 or s_distance[idx]==0:
        continue
    
    #맥세권이면서 스세권인 경우, 최단 거리 answer 업데이트
    if m_distance[idx]<=x and s_distance[idx]<=y:
        answer = min(answer,m_distance[idx]+s_distance[idx])

if answer==float("inf"):
    print(-1)
else:
    print(answer)