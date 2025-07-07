#백준 #5014 스타트링크
#백트래킹 문제
from collections import deque

F, S, G, U, D = map(int, input().split())
visited = [False for _ in range(F+1)] #방문여부
count = [0 for _ in range(F+1)] #횟수
check = False
move = [U, -D]

def BFS(depth):
    global check
    Q = deque()
    Q.append(depth)
    visited[depth] = True

    while Q:
        depth = Q.popleft()
        
        #종결 조건 => BFS이므로 가장 먼저 만족하는 값이 최솟값이 되므로 종결
        if depth == G:
            check = True
            return count[G]

        for k in range(2):
            move_depth = depth + move[k]
            #건물에 존재하는 층이어야 함
            if 1 <= move_depth <= F:
                #방문한 적 없어야 함
                if visited[move_depth] == False:
                    visited[move_depth] = True
                    count[move_depth] = count[depth] + 1
                    Q.append(move_depth)
    return count[G]

if BFS(S) == 0 and check==False:
    print("use the stairs")
else:
    print(count[G])