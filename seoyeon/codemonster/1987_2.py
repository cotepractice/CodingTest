#백준 #1987 알파벳
from collections import deque

R, C = map(int,input().split())
boards = [[] for _ in range(R)]

for i in range(R):
    inp = list(input())
    boards[i] = inp

d = [[0,1],[0,-1],[1,0],[-1,0]]
alpha_dict = dict()

x,y = 0,0
answer = -1

Q = deque()
Q.append([x,y])
#초기값 
visited = set()
visited.add(boards[x][y])

def backtracking(x,y,visited):
    global answer

    answer = max(answer, len(visited))

    for dx,dy in d:
        nx = x+dx
        ny = y+dy
        if 0<=nx<R and 0<=ny<C and boards[nx][ny] not in visited:
            if boards[nx][ny] not in visited:
                visited.add(boards[nx][ny])
                backtracking(nx,ny,visited)
                visited.remove(boards[nx][ny])


backtracking(0,0,visited)
print(answer)