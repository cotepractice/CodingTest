#백준 #1943 동전 분배
#14:22 - 15:48

#1. Greedy Algorithm
# #공평하게 분리하는 것 같지만 
# #반례: [2,2,3,4,5] -> 8만큼 가져갈 수 있음
# while True:
#     try:
#         N = int(input())
#         coins = []

#         for i in range(N):
#             coin, coin_n = map(int,input().split())
#             coins.append([coin,coin_n])

#         coins.sort() #오름차순 정렬

#         #a와 b는 두 사람이 가지는 돈의 합
#         a,b = 0,0
            
#         #coins를 큰 값부터 하나씩 빼서 더 작은 돈의 합을 가진 곳에 더하기
#         while coins:
#             c,cnt = coins.pop()
#             while cnt>0:
#                 if a<=b:
#                     a+=c
#                 else:
#                     b+=c
#                 cnt-=1
#         print(a,b)
#         if a==b:
#             print(1)
#         else:
#             print(0)
#     except:
#         break

# #2. DP
# #단순히 더하는 방식으로 선택하지 않은 경우의 수를 고려하지 않음 
# while True:
#     try:
#         N = int(input())
#         #print("N",N)
#         ans = 0
        
#         coins = []
#         coins_sum = 0
#         coins_cnt = 0 #전체 코인 개수
#         for _ in range(N):
#             coin, coin_n = map(int,input().split())
#             coins_cnt+=coin_n
#             for _ in range(coin_n):
#                 coins_sum+=coin
#                 coins.append(coin)

#         #종결조건: 총합이 홀수인 경우 절대 나눌 수 없음
#         if coins_sum%2==1:
#             print(0)
#             continue

#         #한명이 가질 수 있는 모든 경우의 수     
#         dp = [[0 for _ in range(N)] for _ in range(coins_cnt)]
    
#         #coin 하나씩 빼서 선택하는 경우: 0-1 KnapSack
#         #1) 초기 값 dp[0][0]
#         dp[0][0]=coins[0]
#         #2) 다음 경우의 수 진행
#         # dp[i][j]는 이전 경우의 수 dp[i-1][m]에 현재 coin 값을 더하는 모든 경우의 수 (0<=m<N)
#         for i in range(1,coins_cnt):
#             for j in range(N):
#                 dp[i][j]=dp[i-1][j]+coins[i]

#         #테스트
#         # for k in range(coins_cnt):
#         #     print(*dp[k])

#         for x in range(coins_cnt):
#             for y in range(N):
#                 if dp[x][y]==coins_sum//2:
#                     ans=1
#         print(ans)

#     except:
#         break

#3. DP
# PyPy3로 문제 해결
# for _ in range(3):
#     N = int(input())
#     ans = 0
        
#     coins = []
#     coins_sum = 0 #전체 동전의 합

#     for _ in range(N):
#         coin,coin_n = map(int,input().split())
#         coins.append([coin,coin_n])
#         coins_sum += coin*coin_n
        
#     target = coins_sum // 2

#     #종결조건: 전체가 홀수인 경우 굳이 확인 안 해도 됨
#     if coins_sum%2==1:
#         print(0)
#         continue

#     #dp[n]은 동전을 활용해 금액 n을 만들 수 있는지 여부
#     dp = [False for _ in range(target+1)]
#     dp[0] = True #아무것도 선택하지 않은 경우
        
#     #coins[i] 즉, 한 종류의 동전 탐색
#     for c,c_n in coins:
            
#         #시간초과 발생 코드: 한 번 추가한 경우에서 반복적으로 추가할 수 있음
#         # #dp에서 가능한 금액의 경우 k에 한 종류의 동전이 할 수 있는 모든 경우의 수 True
#         # for k in range(coins_sum//2+1):
#         #     #가능한 경우 동전 선택
#         #     if dp[k]:
#         #         for next in range(1,c_n+1):
#         #             if k+c*next<coins_sum//2+1:
#         #                 dp[k+c*next]=True   
            
#         #시간초과 해결 코드: 역순으로 해결
#         #현재 값 k에서 (k-c)가 가능하면 k부터 k 이상 값 업데이트하므로 중복 X
#         #k-c*cnt가 True인 경우 k True
#         for k in range(target,c-1,-1):
#             #(범위)
#             if k-c<0:
#                 continue
                
#             #현재 값인 k에서 dp[k-c]가 존재하면 현재 코인 c를 1~c_n까지 선택할 수 있음
#             if dp[k-c]:
#                 for ccnt in range(1,c_n+1):
#                     next = (k-c)+c*ccnt
#                     #(범위)
#                     if next<0 or next>target:
#                         continue
#                     dp[next] = True

#             if dp[-1]:
#                 ans=1
#                 break
        
#     print(ans)


#4. dp 대신 비트마스크 사용
# Python3로 문제 해결

for _ in range(3):
    line = input()
    
    N = int(line)
    coins = []
    coins_sum = 0

    for _ in range(N):
        coin, coin_n = map(int, input().split())
        coins.append((coin, coin_n))
        total = coin * coin_n
        coins_sum += total
        
    # 1. 홀수면 절대 반으로 나눌 수 없음
    if coins_sum % 2 == 1:
        print(0)
        continue
            
    target = coins_sum // 2
        
    # 2. 비트마스크 초기화 (dp = [False] * (target + 1) 대용)
    # dp의 i번째 비트가 1이면 'i원 만들기 가능(True)'을 의미함
    # 0원을 만들 수 있으므로 1(2^0)로 시작
    dp = 1
        
    for c, c_n in coins:
        # 현재 동전 c를 c_n개 사용하여 만들 수 있는 모든 경우를 dp에 반영
        # 각 동전의 개수를 1, 2, 4... 처럼 2의 거듭제곱 묶음으로 처리 (이진 분할)
        # 이 로직을 통해 3중 루프를 완전히 제거합니다.
        num = c_n
        k = 1
        while num > 0:
            use = min(k, num)
            # 현재 가능한 모든 금액(dp)을 (동전 가치 * 개수)만큼 shift하여 합치기
            print("dp1",dp)
            dp |= (dp << (c * use))
            print("dp2",dp)
            num -= use
            k *= 2
            
        # 3. 중간에 target 금액 비트가 1이 되면 조기 종료
        if (dp >> target) & 1:
            break
        
    # target 위치의 비트가 1(True)인지 확인
    if (dp >> target) & 1:
        print(1)
    else:
        print(0)

