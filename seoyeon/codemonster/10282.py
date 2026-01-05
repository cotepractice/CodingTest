#백준 #10282 해킹

#19:00-19:37

#1. deque() 사용
# #시간복잡도 O(T*logn)
# # a가 b에 의존하면, b 감염 후 일정 시간 후 a 감염
# from collections import deque

# T = int(input())

# for _ in range(T):
#     #n: 컴퓨터 개수, d: 의존성 개수, c: 해킹 당한 컴퓨터 번호
#     n,d,c = map(int,input().split())
#     #answer = [총 감염되는 컴퓨터 수, 마지막 컴퓨터가 감염되기까지 걸리는 시간]
#     answer = [0,-1]

#     #connections[m]=[n,s] 은 n이 m에 의존. 
#     connections = [[] for _ in range(n)]
#     #감염되는 시간
#     time = [-1 for _ in range(n)]

#     for dd in range(d):
#         #a가 컴퓨터 b를 의존하며, 컴퓨터 b가 감염된 후 s초 후 a도 감염됨
#         a,b,s = map(int,input().split())
#         connections[b-1].append([a-1,s])
    
#     #c부터 진행
#     Q = deque()
#     Q.append(c-1)
#     time[c-1]=0 #초기 컴퓨터 감염 시간 0
#     #다음 진행할 노드 시간 업데이트, Q 삽입
#     while Q:
#         current = Q.popleft()
#         for next,t in connections[current]:
#             time[next]=time[current]+t
#             Q.append(next)
    
#     for tt in time:
#         if tt>=0:
#             answer[0]+=1
#             answer[1]=max(answer[1],tt)
        
#     print(*answer)


#2. heapq + visited. 틀렸습니다 -> 늦게 와도 시간이 더 짧을 수 있어 visited 사용하면 안 됨
#DP로 처리해야 하나? -> t가 각각 다름. 늦게 와도 시간 더 짧을 수 있음

#시간복잡도 O(T*logn)
# a가 b에 의존하면, b 감염 후 일정 시간 후 a 감염
# import heapq

# T = int(input())

# for _ in range(T):
#     #n: 컴퓨터 개수, d: 의존성 개수, c: 해킹 당한 컴퓨터 번호
#     n,d,c = map(int,input().split())
#     #answer = [총 감염되는 컴퓨터 수, 마지막 컴퓨터가 감염되기까지 걸리는 시간]
#     answer = [0,-1]

#     #connections[m]=[n,s] 은 n이 m에 의존. 
#     connections = [[] for _ in range(n)]
#     #감염되는 시간
#     time = [-1 for _ in range(n)]

#     for dd in range(d):
#         #a가 컴퓨터 b를 의존하며, 컴퓨터 b가 감염된 후 s초 후 a도 감염됨
#         a,b,s = map(int,input().split())
#         connections[b-1].append([a-1,s])
    
#     #c부터 진행
#     heap = []
#     heapq.heapify(heap)
#     heapq.heappush(heap, [0,c-1])
#     visited = set()
#     visited.add(c-1)
#     time[c-1]=0 #초기 컴퓨터 감염 시간 0
    
#     #방문한 적 없는 경우, 방문 처리&시간업데이트
#     while heap:
#         current_time, current = heapq.heappop(heap)
#         for next,t in connections[current]:
#             if next in visited:
#                 continue
#             visited.add(next)
#             time[next]=time[current]+t
#             heapq.heappush(heap, [time[next], next])
    
#     for tt in time:
#         if tt>=0:
#             answer[0]+=1
#             answer[1]=max(answer[1],tt)
        
#     print(*answer)

#3. Dijkstra
# t가 달라 늦게 와도 시간이 더 짧을 수 있음
# heapq 대신 deque로 하면 시간 초과 발생
# heapq+sys까지 해야함
import heapq
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    #n: 컴퓨터 개수, d: 의존성 개수, c: 해킹 당한 컴퓨터 번호
    n,d,c = map(int,input().split())
    #answer = [총 감염되는 컴퓨터 수, 마지막 컴퓨터가 감염되기까지 걸리는 시간]
    answer = [0,-1]
    #connections[x]=[y,t] x가 감염된 후 y는 t초 후 감염
    connections = [[] for _ in range(n)]
    time = [float("inf") for _ in range(n)]

    for dd in range(d):
        #a가 컴퓨터 b를 의존하며, 컴퓨터 b가 감염된 후 s초 후 a도 감염됨
        a,b,s = map(int,input().split())
        connections[b-1].append([s,a-1])

    heap=[]
    heapq.heapify(heap)
    heapq.heappush(heap,[0,c-1])
    time[c-1]=0
    while heap:
        current_time, current = heapq.heappop(heap)

        for t,next in connections[current]:
            next_t = current_time+t
            #작은 경우 업데이트
            if next_t<time[next]:
                time[next]=next_t
                heapq.heappush(heap,[next_t,next])

    for tt in time:
        if tt!=float("inf"):
            answer[0]+=1
            answer[1]=max(answer[1],tt)
    print(*answer)