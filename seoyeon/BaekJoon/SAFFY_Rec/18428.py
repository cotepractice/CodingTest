#백준 #18428 감시 피하기
from collections import defaultdict

N = int(input())

lst = [["" for _ in range(N)] for _ in range(N)]

t_pos = defaultdict(list)
s_pos = defaultdict(list)

t_lst = []

for i in range(N):
    lst[i] = list(input().split())
    for j in range(N):
        if lst[i][j]=="T":
            if i in t_pos:
                t_pos[i].append(j)
            else:
                t_pos[i] = [j]
            t_lst.append([i,j])
        if lst[i][j]=="S":
            if i in s_pos:
                s_pos[i].append(j)
            else:
                s_pos[i] = [j]

#print(lst) 
#print("t", t_pos)
#print("s", s_pos)

dx = [0,0,-1,1]
dy = [1,-1,0,0]

cnt = 0 #장애물 개수
ans = 0 #결과
for x,y in t_lst:

    for k in range(4): #방향. 상하좌우
        for m in range(1,N): #해당 방향으로 몇 번 갈지
            nx = x+dx[k]*m
            ny = y+dy[k]*m

            if 0<=nx<N and 0<=ny<N:
                #장애물 만난 경우 for m in range(1,N) 더 이상 진행 X
                if lst[nx][ny] == "O":
                    print("nxny111",nx,ny)
                    break

                if lst[nx][ny]=="S":
                    #T 바로 옆의 S인 경우 NO
                    if m==1:
                        ans = 1
                        break
                    #바로 옆이 아닌 위치에 S인 경우 S 바로 앞에 장애물 놓기
                    else:
                        nx -= dx[k]
                        ny -= dy[k]
                        lst[nx][ny] = "O"
                        print("nxny",nx,ny)
                        cnt += 1
                    
if ans == 1 or cnt > 3:
    print("NO")
else:
    print("YES")
