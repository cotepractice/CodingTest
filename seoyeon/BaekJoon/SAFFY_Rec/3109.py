#백준 #3109 빵집

def dfs(x,y):
    global ans, matrix, visited
    
    visited[x][y] = True
    
    if y == C-1:
        ans += 1
        return True
    
    if matrix[x][y]=="x":
        return 

    #오른쪽 위 대각선
    if x-1>=0 and y+1>=0 and matrix[x-1][y+1]=="." and visited[x-1][y+1]==False:
        if dfs(x-1,y+1):
            return True

    #오른쪽
    if x<R and y+1<C and matrix[x][y+1]=="." and visited[x][y+1]==False:
        if dfs(x,y+1):
            return True


    #오른쪽 아래 대각선
    if x+1<R and y+1<C and matrix[x+1][y+1]=="." and visited[x+1][y+1]==False:
        if dfs(x+1,y+1):
            return True

    return False



R, C = map(int,input().split())

matrix = [["" for _ in range(C)] for _ in range(R)]

for i in range(R):
    lst = input()
    matrix[i] = lst

#print(matrix[0][1])
visited = [[False for _ in range(C)] for _ in range(R)]
ans = 0

for i in range(R):
    dfs(i,0)

print(ans)