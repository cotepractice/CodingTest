# #BFS
# from collections import deque
# def solution(n, edge):
#     answer = 0
    
#     edge_n = [[] for _ in range(n+1)]
#     visited = [False for _ in range(n+1)]
    
#     for e in edge:
#         x,y = e
#         edge_n[x].append(y)
#         edge_n[y].append(x)
    
#     Q = deque()
#     Q.append([0,1]) #[간선길이,노드]
#     visited[1]=True
#     max_len = 0
#     while Q:
#         len, node = Q.popleft()
#         if len>=max_len:
#             if len==max_len:
#                 answer += 1
#             else:
#                 max_len = len
#                 answer = 1
#         for next in edge_n[node]:
#             if visited[next]==False:
#                 visited[next]=True
#                 Q.append([len+1,next])
    
#     return answer

import heapq

#find_parent()
#union()
def solution(n, edge):
    global nodes, min_d
    
    nodes = [[] for _ in range(n)]
    min_d = [float("inf") for _ in range(n)]
    visited = [False for _ in range(n)]
    
    answer = 0
    
    #가장 멀리 떨어진 노드: 최단 경로로 이동했을 때 간선의 개수가 가장 많은 노드 의미
    #출력: 1번 노드에서 가장 멀리 떨어진 노드 개수
    
    for x,y in edge:
        nodes[y-1].append(x-1)
        nodes[x-1].append(y-1)
    
    visited[0]=True
    min_d[0]=0
    
    heap=[[0,0]]
    heapq.heapify(heap)
    
    while heap:
        cnt, x = heapq.heappop(heap)
        #print("cnt,x",cnt,x)
        lst = nodes[x]
        for l in lst:
            if visited[l]==False:
                min_d[l] = cnt+1
                visited[l]=True
                heapq.heappush(heap, [cnt+1, l])
    
    max_n = -float("inf")
    #print("min_d",min_d)
    for i in range(n):
        if min_d[i]>max_n:
            max_n = min_d[i]
            answer = 1
        elif min_d[i]==max_n:
            answer += 1
            
    return answer