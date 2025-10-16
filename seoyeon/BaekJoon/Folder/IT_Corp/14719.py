#백준 #14719 빗물

H, W = map(int,input().split()) #H:세로,W:가로

h_lst = list(map(int,input().split()))

maps = [[0 for _ in range(W)] for _ in range(H)]

for i in range(W):
    h = h_lst[i]
    for j in range(H-h,H):
        maps[j][i]=1

answer = 0
for h_idx in range(H):
    check = 0 #check=0인 경우 시작하지 않음.check=1인 경우 시작 벽 존재
    current = 0 #마지막에 막히는 경우 answer에 추가
    for k in range(W):
        if check==0 and maps[h_idx][k]==1:
            check = 1
        elif check == 1 and maps[h_idx][k]==1:
            answer += current
            current = 0
        elif check == 1 and maps[h_idx][k]==0:
            current += 1

print(answer)