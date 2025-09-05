#백준 1446 지름길

N, D = map(int, input().split())

road_lst = []
dp = [i for i in range(D+1)]

for _ in range(N):
    s, e, d = map(int, input().split()) #시작위치, 도착위치, 지름길 길이
    if e-s > d:
        road_lst.append([s,e,d])

road_lst.sort()

for s,e,d in road_lst:
    
    #겹치는 경우
    for i in range(1,D+1):
        if i==e:
            dp[i] = min(dp[i], dp[s]+d)
        else:
            dp[i] = min(dp[i],dp[i-1]+1)
            
print(dp[D])