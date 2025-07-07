#백준 #1753 최단경로
#DP

import heapq
import sys
input = sys.stdin.readline

def solv(start_idx):
    global dp
    
    #DP 정의
    dp[start_idx]=0
    Q=[[0,start_idx]] #[가중치,지나는인덱스]
    heapq.heapify(Q)
    
    while Q:
        n,idx = heapq.heappop(Q)

        #현재 값이 더 크면 진행하지 않음
        if dp[idx] < n:
            continue

        for w,next_n in edges[idx]:
            next_w = n+w
            if next_w < dp[next_n]:
                dp[next_n] = next_w
                heapq.heappush(Q,[next_w,next_n])
    

V,E = map(int,input().split()) #V: 정점의 수,E:간선의 수
K = int(input()) #K:시작정점번호
edges = [[] for _ in range(V)] #[가중치,정점]
dp=[float("inf") for _ in range(V)]

for e in range(E):
    u,v,w = map(int,input().split()) #u,v:정점,w:가중치
    edges[u-1].append([w,v-1])

solv(K-1)

for i in range(V):
    if dp[i]==float("inf"):
        print("INF")
    else:
        print(dp[i])