from collections import deque

M,N,H = map(int,input().split()) #for i in range(N): for j in range(M))

box = [[[-1 for _ in range(M)] for _ in range(N)] for _ in range(H)]
visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]

Q = deque()
first_lst = []

for h in range(H):
    for i in range(N):
        box[h][i] = list(map(int,input().split()))
        for j in range(M):
            if box[h][i][j]==1:
                Q.append([h,i,j])
                first_lst.append([h,i,j])
                visited[h][i][j]=True

d = [[0,0,1],[0,0,-1],[1,0,0],[-1,0,0],[0,1,0],[0,-1,0]]

prev_cnt = 0
cnt = len(first_lst)
t = 0
count = -1
while True:
    prev_cnt = cnt

    lst = []
    count = 0
    while Q:
        current_h,current_x,current_y = Q.popleft()

        for dx,dy,dh in d:
            nx = current_x+dx
            ny = current_y+dy
            nh = current_h+dh

            if 0<=nx<N and 0<=ny<M and 0<=nh<H and visited[nh][nx][ny]==False and box[nh][nx][ny]==0:
                visited[nh][nx][ny]=True
                lst.append([nh,nx,ny])
                count += 1
    if count==0 and t==0:
        answer = 0
        break
    if count==0:
        break
    cnt = len(lst)
    Q = deque(lst)
    t += 1
    
answer = t
for h in range(H):
    for x in range(N):
        for y in range(M):
            if visited[h][x][y]==False and box[h][x][y]!=-1:
                answer = -1
                break
print(answer)