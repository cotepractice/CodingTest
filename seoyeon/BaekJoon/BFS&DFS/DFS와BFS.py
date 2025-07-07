# DFS와 BFS
from collections import deque

#입력
#N:정점의 개수, M:간선의 개수, V:탐색을 시작할 정점 번호
N, M, V = map(int,input().split())

#이중리스트
lst = [[False for _ in range(N+1)] for _ in range(N+1)]

for i in range(M):
    s, e = map(int,input().split())
    #양방향 연결
    lst[s][e] = True
    lst[e][s] = True 

#DFS는 재귀함수
def dfs(lst, dfs_ans,dfs_visited,start):
    dfs_ans.append(start) #중복불가능
    dfs_visited[start] = True #방문처리
    
    for i in range(1,N+1):
        if lst[start][i]==True and dfs_visited[i]==False: #연결되고 방문하지 않은 경우 방문
            dfs(lst, dfs_ans, dfs_visited, i) #재귀
    
    return dfs_ans

#BFS는 Queue 사용
def bfs(lst, bfs_ans,bfs_visited,start):
    Q = deque()
    Q.append(start)
    bfs_visited[start] = True
    while Q:
        s = Q.popleft()
        bfs_ans.append(s)
        for i in range(1,N+1):
            if lst[s][i] == True and bfs_visited[i] == False: #연결되고 방문하지 않은 경우 방문
                bfs_visited[i] = True
                Q.append(i)
    return bfs_ans

#DFS
dfs_ans = [] #결과
dfs_visited = [False for _ in range(N+1)]
print(*dfs(lst, dfs_ans, dfs_visited, V))

#BFS
bfs_ans = [] #결과
bfs_visited = [False for _ in range(N+1)]
print(*bfs(lst, bfs_ans, bfs_visited, V))