#1:집 존재 2:집X
#연결된다는 것은 좌우위아래 연결되어 있다는 것

#BFS
from collections import deque

N = int(input())
boards = ["" for _ in range(N)] 

answer_boards = [[0 for _ in range(N)] for _ in range(N)] #방문처리 동시에 진행
result = []

for i in range(N):
    line = input()
    boards[i] = line

d = [[1,0],[-1,0],[0,1],[0,-1]]

def bfs(x,y,cnt):
    global answer_boards

    Q = deque()
    Q.append([x,y])
    answer_boards[x][y]=cnt
    answer_n = 0

    while Q:
        current_x, current_y = Q.popleft()
        answer_n += 1

        for dx,dy in d:
            nx = current_x+dx
            ny = current_y+dy
            if 0<=nx<N and 0<=ny<N:
                #집이 존재하고, 방문한적없는 경우
                if boards[nx][ny]=="1" and answer_boards[nx][ny]==0:
                    answer_boards[nx][ny]=cnt
                    Q.append([nx,ny])
    return answer_n

cnt = 0
for i in range(N):
    for j in range(N):
        if boards[i][j]=="1" and answer_boards[i][j]==0:
            cnt += 1
            answer_n = bfs(i,j,cnt)
            result.append(answer_n)

print(len(result))
result.sort()
for i in range(len(result)):
    print(result[i])