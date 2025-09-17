#백준 #1697 숨바꼭질
#17:10 - 18:04

#N:수빈, K:동생
N, K = map(int,input().split())
dp1 = [float("inf") for _ in range(100000*2)]
dp2 = [float("inf") for _ in range(100000*2)]
dp = [float("inf") for _ in range(100000*2)]

#수빈
## 1초
## 1. 걷기 x -> x-1 또는 x+1
## 2. 순간이동 x -> 2*x

#1.걷기
dp1[N]=0
for i in range(N+1,K+1):
    dp1[i]=dp1[i-1]+1

#2.순간이동
## i번째에서 순간이동 하는 경우
idx = K
K_close = -1 #K를 넘는 가장 가까운 수
for i in range(N,K+1):
    #걷기 전
    if i==N:
        tmp = i*2
        dp2[tmp]=1
        while True:
            tmp *= 2
            dp2[tmp] = dp2[tmp//2]+1
            #넘어가고 뒤로 가는 상황도 있으므로
            if tmp>K:
                break
        continue

    #한 번이라도 걸은 후
    tmp = i
    while True:
        tmp *= 2
        print("tmp",tmp)
        #초기: 걸은 시간에서 1초 추가
        if tmp == i*2:
            dp2[tmp] = dp1[i]+1
        #그외: 이전 
        else:
            dp2[tmp] = dp2[tmp//2]+1        
        if tmp>K:
            break

## K를 넘고 x-1로 걸어서 오는 경우
dp2[K] = min(dp2[K], dp2[K_close]+(K_close-K))


print("dp1",dp1[:K*2])
print("dp2",dp2[:K*2])

print(min(dp1[K], dp2[K]))
