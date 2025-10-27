#백준 #1987 알파벳

#1. DFS 시간 초과 -> 재귀 시간 초과 가능 높음
# R, C = map(int,input().split())
# boards=["" for _ in range(R)]

# for r in range(R):
#     boards[r]=input()

# alpha=dict()
# answer=1
# d=[[0,1],[0,-1],[1,0],[-1,0]]

# def dfs(cnt,x,y,alpha):
#     global answer
#     answer=max(answer,cnt)

#     for dx,dy in d:
#         nx=x+dx
#         ny=y+dy
#         if 0<=nx<R and 0<=ny<C and boards[nx][ny] not in alpha:
#             alpha[boards[nx][ny]]=0
#             dfs(cnt+1,nx,ny,alpha)
#             del alpha[boards[nx][ny]]

# alpha[boards[0][0]]=0
# dfs(1,0,0,alpha)
# print(answer)

#2. BFS

R, C = map(int,input().split())
boards = ["" for _ in range(R)]

for i in range(R):
    board = input()
    boards[i] = board

def bfs():
    max_depth = 0 

    Q = set() #set(). 중복 방지. Q = [[x1,y1,visited_alpha],...] 
    Q.add((0,0,boards[0][0]))

    d = [[0,-1],[0,1],[-1,0],[1,0]]
    while Q:
        x,y,visited_alpha = Q.pop()
        max_depth = max(max_depth, len(visited_alpha))

        if max_depth == 26: #알파벳 총 26
            return 26

        for dx,dy in d:
            nx = x+dx
            ny = y+dy
            if 0<=nx<R and 0<=ny<C and boards[nx][ny] not in visited_alpha:
                Q.add((nx,ny,visited_alpha+boards[nx][ny]))
    return max_depth

print(bfs())