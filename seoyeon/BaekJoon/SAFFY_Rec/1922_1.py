#백준 #1922 네트워크 연결
#Prim's Algorithm
import heapq

def prim(idx):
    visited = [False for _ in range(N)]
    weight = [float("inf") for _ in range(N)]

    #시작노드
    weight[idx]=0
    
    #heapq
    edges_heap = [[0,idx]] # [가중치,노드]
    heapq.heapify(edges_heap)

    while edges_heap:
        w,node = heapq.heappop(edges_heap)
        
        if visited[node]==False:
            visited[node]=True
            #갈 수 있는 노드 찾아서 heapq에 삽입
            for next_w,next_node in edges[node]:
                #방문한 적 없고 최솟값인 경우
                if visited[next_node]==False and weight[next_node] > next_w:
                    weight[next_node] = next_w
                    heapq.heappush(edges_heap, [next_w,next_node])
    print(sum(weight))


N = int(input())
M = int(input())
edges = [[] for _ in range(N)]

for m in range(M):
    a,b,c = map(int,input().split())
    edges[a-1].append([c,b-1])
    edges[b-1].append([c,a-1])

prim(0)
