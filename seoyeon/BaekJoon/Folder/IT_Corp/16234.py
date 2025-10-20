#백준 #16234 인구 이동
from collections import deque

from collections import deque

# 입력
N, L, R = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

# 상하좌우
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, visited):
    Q = deque()
    Q.append((x, y))
    union = [(x, y)]
    visited[x][y] = True
    total_population = maps[x][y]

    while Q:
        cx, cy = Q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                diff = abs(maps[cx][cy] - maps[nx][ny])
                if L <= diff <= R:
                    visited[nx][ny] = True
                    Q.append((nx, ny))
                    union.append((nx, ny))
                    total_population += maps[nx][ny]
    return union, total_population

days = 0

while True:
    visited = [[False]*N for _ in range(N)]
    is_moved = False  # 이번 턴에 이동이 있었는지

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                union, total = bfs(i, j, visited)
                if len(union) > 1:  # 연합이 있으면 인구 이동
                    move_n = total // len(union)
                    for ux, uy in union:
                        maps[ux][uy] = move_n
                    is_moved = True

    if not is_moved:  # 이동 없으면 종료
        break
    days += 1

print(days)