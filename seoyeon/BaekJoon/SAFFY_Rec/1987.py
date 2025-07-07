#백준 #1987 알파벳

def dfs(x, y):
    global board, R, C

    movement_array = [[-1,0],[1,0],[0,-1],[0,1]]

    max_depth = 0
    queue = set() # 중복 방지. 동일한 위치 오지 않도록 함
    queue.add((x, y, board[x][y]))
    while queue: 
        current_x, current_y, current_visited = queue.pop() #current_visited는 문자열
        
        max_depth = max(max_depth, len(current_visited))
        if max_depth == 26: #알파벳 개수
            return 26
        for movement in movement_array:
            next_x = current_x + movement[0]
            next_y = current_y + movement[1]
            if 0 <= next_x < R and 0 <= next_y < C and board[next_x][next_y] not in current_visited:
                queue.add((next_x, next_y, current_visited + board[next_x][next_y]))
    return max_depth       



R, C = map(int,input().split())
board = ["" for _ in range(R)]

for r in range(R):
    lst=input()
    board[r]=lst

visited=[[False for _ in range(C)] for _ in range(R)]

visited[0][0]=True

print(dfs(0,0))

#print(max_depth)