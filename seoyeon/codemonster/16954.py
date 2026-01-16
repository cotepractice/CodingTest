#백준 #16954 움직이는 미로 탈출

from sys import stdin
from collections import deque

input = stdin.readline

# 9방향
dr = (0, -1, 0, 1, 1, 1, 0, -1, -1)
dc = (0, 1, 1, 1, 0, -1, -1, -1, 0)

def bfs():
    Q = deque([(7, 0)])
    time = 0
    while Q:
        visited = [[0] * 8 for _ in range(8)]
        qlen = len(Q)
        for _ in range(qlen):
            r, c = Q.popleft()
            if board[r][c] == "#":  # 이동 시작 위치가 벽이면
                continue
            if (r, c) == (0, 7):    # 탈출 성공
                return 1

            for d in range(9):
                nr = r + dr[d]
                nc = c + dc[d]
                # 격자 밖으로 나가면
                if not (0 <= nr < 8 and 0 <= nc < 8):
                    continue
                # 이동할 위치가 벽이거나 이미 방문했으면
                if board[nr][nc] == "#" or visited[nr][nc]:
                    continue
                visited[nr][nc] = 1
                Q.append((nr, nc))
        
        # 벽 이동
        board.pop()
        board.appendleft(['.', '.', '.', '.', '.', '.', '.', '.'])

        time += 1
        if time == 9:   # 9초 후 현존하는 벽 없으므로 탈출 가능
            return 1
    return 0    # 탈출 실패


board = deque(list(input().rstrip()) for _ in range(8))
print(bfs())