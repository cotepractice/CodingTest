#백준 #1012 유기농 배추
#그래프 문제
#1:06

# # #1. bfs 사용 => 성공 ! 
# #시간초과 발생 => 방문처리를 queue에 넣은 후 하는 것이 아니라 queue에 넣기 전에 하는 것이 핵심
# #<https://www.acmicpc.net/blog/view/70> 참고
from collections import deque
import sys

input = sys.stdin.readline

T = int(input())

def bfs(graph, x,y):
    #print("x,y",x,y)
    queue = deque()
    queue.append((x,y))

    while queue:
        #print("queue",queue)
        i, j = queue.popleft()
        #graph[i][j] = 0    #기존에는 방문처리 여기에서 진행
        #print(cnt,"while queue",i,j)

        dx = [0,0,-1,1]
        dy = [-1,1,0,0]
        for k in range(4):
            I = i + dx[k]
            J = j + dy[k]
            #print("I,J",I,J)

            if (0<=I<m and 0<=J<n and graph[I][J] == 1):
                graph[I][J] = 0 #방문처리(graph[x][y]=0)를 queue에 넣기 전에 하는 것이 핵심! 그렇지않은경우 중복처리될수있음
                queue.append((I,J))
    
    return graph


for _ in range(T):

    m, n, k = map(int, input().split())
    #graph 결정
    graph = [[0 for _ in range(n)] for _ in range(m)]

    for l in range(k):
        x,y = map(int, input().split())

        graph[x][y] = 1

    #bfs 사용
    cnt = 0
    for i in range(m):
        for j in range(n):
            if (graph[i][j] == 1):
                cnt += 1
                bfs(graph, i,j)

    print(cnt)

#2. dfs 사용 => 성공 !
#틀렸습니다 => dfs에서 재귀함수인 경우 return dfs(nx,ny)로 했을 때에는 틀렸다고 나오는데 return을 제거하면 정답
#재귀함수에서의 return은 필요한 경우가 있지만 이때의 경우 재귀함수를 사용해 graph를 변경하고 함수 외부에서 원하는 값(cnt)을 계산하므로 return 필요없음
from collections import deque
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

T = int(input())

def dfs(x,y):
    graph[x][y] = 0
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    for l in range(4):
        nx = x+dx[l]
        ny = y+dy[l]

        if (nx<0 or nx>=n or ny<0 or ny>=m):
            continue
        if (graph[nx][ny] == 1):
            dfs(nx,ny)

for _ in range(T):
    m, n, k = map(int, input().split())

    #graph 생성
    graph = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if (graph[i][j] == 1):
                cnt += 1
                dfs(i,j)
    print(cnt)