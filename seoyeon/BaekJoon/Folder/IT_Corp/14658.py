#백준 #14658 하늘에서 별똥별이 빗발친다
#14:20-15:40

#N:별똥별 떨어지는 구역의 가로길이, M:세로길이, L:트램펄린 한 변의 길이, K:별똥별 수
#N,M<=500,000 , L<=100,000, K<=100
#트램펄린은 L*L 크기. 최대한 많은 별똥별을 튕겨내도록 트램펄린 배치
N,M,L,K = map(int,input().split())
stars = [[-1,-1] for _ in range(K)]

for k in range(K):
    x,y = map(int,input().split())
    stars[k]=[x,y]


#stars가 트램폴린의 왼쪽위, 오른쪽위, 왼쪽아래, 오른쪽아래인 경우
answer=0

#[sx,sy]와 [nx,ny] 별똥별을 걸치는 트램폴린의 가장 왼쪽 상단 좌표 [lx,ly]
for sx,sy in stars:
    for nx,ny in stars:
        
        lx=min(sx,nx)
        ly=min(sy,ny)

        #[lx,ly]를 왼쪽 상단 좌표로 가지는 트램폴린에서 다른 stars 카운트
        cnt=0
        for cx,cy in stars:
            if lx<=cx<=lx+L and ly<=cy<=ly+L:
                cnt+=1
        answer=max(answer,cnt)

print(K-answer)