#백준 #1005 ACM Craft
#위상정렬
#DP

from collections import deque

T = int(input())
for t in range(T):
    N,K = map(int,input().split()) #N:건물의 개수,K:건설규칙의 개수
    times = list(map(int,input().split())) #times:해당 건물을 건설하는데 걸리는 시간
    connections = [0 for _ in range(N+1)] #connections[i]는 i보다 먼저 건설되어야 하는 건물 수
    connect_prev = [[] for _ in range(N+1)] #connect[i]는 i보다 먼저 건설되어야 하는 건물 리스트
    connect_next = [[] for _ in range(N+1)]
    dp = [0 for _ in range(N+1)] #dp: 해당 건물을 건설하는데 걸리는 총 시간

    for k in range(K):
        x,y = map(int,input().split()) #x->y
        connections[y] += 1
        
        connect_prev[y].append(x)
        connect_next[x].append(y)

    Q = deque()
    for i in range(1,N+1):
        if connections[i]==0:
            Q.append(i)

    while Q:
        current = Q.popleft()
        
        if len(connect_prev[current])==0:
            dp[current] = times[current-1]
        else:
            for prev in connect_prev[current]:
                dp[current] = max(dp[current],times[current-1],dp[prev]+times[current-1])
            
        for next in connect_next[current]:
            connections[next] -= 1
            if connections[next]==0:
                Q.append(next)

    W = int(input())
    print(dp[W])