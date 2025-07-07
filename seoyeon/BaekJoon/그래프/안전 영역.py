#백준 #2468 안전 영역
#그래프 문제
#16:28-17:17
#이전 문제들은 조건에 부합하는 경우가 area에 해당한다면, 해당 문제는 조건에 부합하는 경우가 벽이 되어 반대로 생각해야했음
#visited 용도의 check_lst 존재
#sum_lst는 k에 따른 area의 개수를 나타내는데 k가 1이상 100이하이기에 sum_lst = [0 for _ in range(101)], k가 (1,101)로 설정
#위의 경우 모두 sum_lst[0]은 반드시 0이 되는데 이 경우를 없애야 함 => 코드 상에서 이렇게 처리하지 않으면 오류 발생하는데 정렬하는데 왜 그런지 모르겠음 

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, input().split()))

#print(graph)
    
#bfs 함수
def bfs(i,j,height):
    #cnt = 1
    Q = deque()
    Q.append((i,j))
    check_lst[i][j] = True

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    while Q:
        #print("Q",Q)
        x,y = Q.popleft()
        for p in range(4):
            nx = x+dx[p]
            ny = y+dy[p]

            if (0<=nx<n and 0<=ny<n):
                if (graph[nx][ny] > height and check_lst[nx][ny] == False):
                    check_lst[nx][ny] = True
                    #graph[nx][ny] = 101
                    #cnt += 1
                    Q.append((nx,ny))
    #print("k,i,j",k,i,j)
    #print("check_lst",check_lst)

    return

sum_lst = [0 for _ in range(100)]

for k in range(100):    #높이가 최대 100인 정수
    #print("k",k)
    check_lst = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if (graph[i][j] > k and check_lst[i][j] == False):
                bfs(i,j,k)
                sum_lst[k] += 1
#print("sum_lst",sum_lst)
sum_lst.sort(reverse=True)
print(sum_lst[0])
    