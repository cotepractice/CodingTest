#백준 #13911 집 구하기

# #1. Dijkstra -> 시간초과 발생
# # Dijkstra는 하나의 정점에서 진행할 때 유리
# import heapq,sys

# input = sys.stdin.readline

# V, E = map(int,input().split())
# connections = [[] for _ in range(V)]

# for e in range(E):
#     u,v,w = map(int,input().split())

#     #양방향
#     connections[u-1].append([v-1,w])
#     connections[v-1].append([u-1,w])

# #M:맥도날드 수, x:맥세권 조건
# M, x = map(int,input().split())
# #m_lst: 맥도날드 정점 번호
# m_set = set()
# m_lst = []

# m_lst = list(map(int,input().split()))
# for mm in m_lst:
#     m_set.add(mm-1)

# #S: 스타벅스 수, y:스세권 조건 
# S, y = map(int,input().split())
# #s_lst: 스타벅스 저점 번호
# s_set = set()
# s_lst = []

# s_lst = list(map(int,input().split()))
# for ss in s_lst:
#     s_set.add(ss-1)

# #조건:맥세권이면서 스세권 중 거리가 가장 작은 정점

# answer = float("inf")

# def dijkstra(start):
#     distance = [float("inf") for _ in range(V)]
#     distance[start]=0

#     heap = []
#     heapq.heapify(heap)
#     heapq.heappush(heap, [0,start])

#     while heap:
#         current_weight, current = heapq.heappop(heap)
#         #print("connections",connections)
#         for next,next_weight in connections[current]:
#             weight = current_weight + next_weight
#             if weight < distance[next]:
#                 distance[next] = weight
#                 heapq.heappush(heap,[weight, next])

#     m_distance=float("inf")
#     s_distance=float("inf")

#     for i in range(V):
#         if i==start:
#             continue
#         if i in m_set and distance[i]!=float("inf"):
#             m_distance = min(m_distance,distance[i])
#         if i in s_set and distance[i]!=float("inf"):
#             s_distance = min(s_distance,distance[i])
    
#     if m_distance!=float("inf") and s_distance!=float("inf"):
#         return m_distance+s_distance
#     else:
#         return float("inf")


# for i in range(V):
    
#     #집만 탐색
#     if i in m_set or i in s_set:
#         continue

#     answer = min(answer, dijkstra(i))

# if answer==float("inf"):
#     print(-1)
# else:
#     print(answer)


#2. 맥도날드, 스타벅스 기준
import heapq,sys

input = sys.stdin.readline


V, E = map(int,input().split())
connections = [[] for _ in range(V)]

for e in range(E):
    u,v,w = map(int,input().split())

    #양방향
    connections[u-1].append([v-1,w])
    connections[v-1].append([u-1,w])

#M:맥도날드 수, x:맥세권 조건
M, x = map(int,input().split())
#m_lst: 맥도날드 정점 번호
m_lst = list(map(int,input().split()))

#S: 스타벅스 수, y:스세권 조건 
S, y = map(int,input().split())
#s_lst: 스타벅스 저점 번호
s_lst = list(map(int,input().split()))

#맥도날드
#O(VlogE)
m_distance = [float("inf") for _ in range(V)]

heap = []
for mm in m_lst:
    heap.append([0,mm-1])
    m_distance[mm-1]=0
heapq.heapify(heap)

while heap:
    current_distance, current = heapq.heappop(heap)

    if m_distance[current]<current_distance:
        continue

    for next, next_distance in connections[current]:
        distance = current_distance+next_distance
        if distance<m_distance[next]:
            m_distance[next]=distance
            heapq.heappush(heap,[distance,next])

#틀린 경우: O(M*VlogE)
# for xx in m_lst:
#     xx -= 1
#     heap=[]
#     m_distance[xx]=0
#     heapq.heapify(heap)
#     heapq.heappush(heap,[0,xx])

#     while heap:
#         current_distance, current = heapq.heappop(heap)

#         if m_distance[current]<current_distance:
#             continue

#         for next, next_distance in connections[current]:
#             distance = current_distance+next_distance
#             if distance<m_distance[next]:
#                 m_distance[next]=distance
#                 heapq.heappush(heap,[distance,next])


#스타벅스
s_distance = [float("inf") for _ in range(V)]

heap = []
for ss in s_lst:
    heap.append([0,ss-1])
    s_distance[ss-1]=0
heapq.heapify(heap)

while heap:
    current_distance, current = heapq.heappop(heap)

    if s_distance[current]<current_distance:
        continue

    for next, next_distance in connections[current]:
        distance = current_distance+next_distance
        if distance<s_distance[next]:
            s_distance[next]=distance
            heapq.heappush(heap,[distance,next])

#print("m_distance",m_distance)
#print("s_distace",s_distance)

answer = float("inf")
for idx in range(V):

    ans = float("inf")

    if 0<m_distance[idx]<=x and 0<s_distance[idx]<=y:
        ans = m_distance[idx]+s_distance[idx]
    answer = min(answer,ans)

if answer==float("inf"):
    print(-1)
else:
    print(answer)
