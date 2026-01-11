#백준 #14658 하늘에서 별똥별이 빗발친다

#N:별똥별이 떨어지는 가로길이, M:세로길이, L:트램펄린 한 변의 길이, K:별똥별 개수
N,M,L,K = map(int,input().split())

stars = [[-1,-1] for _ in range(K)]

for k in range(K):
    x,y = map(int,input().split())
    stars[k]=[x,y]

#O(K**3)
# 두 별을 포함한다고 가정
# i번째 별의 x좌표를 트램펄린의 왼쪽 변(tx)으로 설정
max_cnt = 0
for i in range(K):
    # j번째 별의 y좌표를 트램펄린의 위쪽 변(ty)으로 설정
    for j in range(K):
        cnt = 0
        tx = stars[i][0]
        ty = stars[j][1]
        
        # 설정된 (tx, ty) ~ (tx+L, ty+L) 범위 안에 몇 개의 별이 있는지 확인
        for k in range(K):
            sx, sy = stars[k]
            # 경계면(L)을 포함하므로 <= 로 비교
            if tx <= sx <= tx + L and ty <= sy <= ty + L:
                cnt += 1
        
        max_cnt = max(max_cnt,cnt)

print(K-max_cnt)