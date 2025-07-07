#백준 #1561 놀이공원

N, M = map(int,input().split())

play_t = list(map(int,input().split()))

#초기에는 모든 놀이 기구가 비어있어 앞에서부터 순서대로 탐 
if N<=M:
    print(N)
#이후에는 0부터 가능한 최대 시간까지 이분탐색으로 탑승한 인원 체크
else:
    left,right = 0, max(play_t)*N #최대 시간은 (가장 긴 놀이 기구 시간 * N)

    #1. left, right 조정해 마지막 인원의 "탑승 시간" 결정
    while left<right:
        mid = (left+right)//2 #mid: 시간 의미

        #1-1. mid 시간까지 탑승한 인원 수 계산
        rides = M #현재까지 탑승한 인원 수. 초기에는 M명 태울 수 있음
        for t in play_t:
            rides += mid//t #[중요] mid 시간까지 각 놀이기구에서 태운 인원 수 
        
        #1-2. 이분 탐색으로 탐색 범위 조정
        #rides가 N보다 큰 경우 0~mid 까지 재탐색
        if rides>=N:
            right = mid
        #rides가 N보다 작은 경우 mid~0까지 재탐색
        else:
            left = mid + 1

    #2. 마지막 인원이 탄 놀이기구 탐색
    rides = M #초기값
    #2-1. left-1초까지 탐승합 인원 수 rides
    for t in play_t:
        rides += (left-1) // t
    
    #2-2. left 초에 탑승하는 놀이기구 탐색
    for i,t in enumerate(play_t):
        #left초에 놀이기구가 비어있으면 새로 태울 수 있음
        if left%t == 0:
            rides += 1
        #rides==N인 경우 종결. enumerate는 인덱스 값을 포함시키므로 i+1을 출력해야 함
        if rides == N:
            print(i+1)
            break