#백준 #20055 컨베이어 벨트 위의 로봇
#삼성 SW 역량 테스트 기출

#1. 문제 이상하게 해석
# N, K = map(int, input().split())
# belt = list(map(int, input().split()))
# dp = [False for _ in range(N*2)]

# #각 칸 위에 있는 로봇과 함께 한 칸 회전
# def rotateAll(lst, dp):
#     #조건에 따라 이동
#     for i in range(2*N-1,-1,-1):    #index가 N=6인 경우 5,4,3,2,1,0
#         if (dp[i] == True and i < 2*N-1):   #마지막은 어차피 내려가니까 
#             if  (i+1<2*N and dp[i+1] == False and lst[i+1] > 0):
#                 lst[i+1] -= 1
#                 dp[i] = False
#                 dp[i+1] = True

#     #조건에 따라 이동 & 이동한 경우 내구도 1 감소

#     return lst

# def rotate(lst,dp):
#     #뒤 index부터 이동할 수 있으면 회전
#     for i in range(2*N-1,-1,-1):
#         if (dp[i] == True and i<2*N-1 and lst[i+1]>0):
#             if  (i+1<2*N and dp[i+1] == False and lst[i+1] > 0):
#                 lst[i+1] -= 1
#                 dp[i] = False
#                 dp[i+1] = True
#     return lst

#     #그렇지 않은 경우 가만히 있기

# #올리는 위치의 내구도가 0이 아니라면 로봇 올리기
# def up(lst,dp):
#     if (lst[0] > 0):
#         lst[0] -= 1
#         dp[0] = True
#     return lst

# #내구도가 0인 칸의 개수가 K개 이상인 경우 종료
# def check(lst):
#     cnt = 0
#     for i in range(2*N):
#         if (lst[i] == 0):
#             cnt += 1
#     return cnt

# count = 0
# while True:
#     #1단계
#     belt = rotateAll(belt, dp)
#     print("1",belt, dp)
#     #2단계
#     rotate(belt,dp)
#     print("2",belt, dp)    
#     #3단계
#     up(belt,dp)
#     print("3",belt, dp)    
#     #4단계
#     count += 1
#     cnt = check(belt)
#     print("4",belt, dp)
#     if cnt >= K:
#         print(count)
#         break

#2. deque 사용
from collections import deque

N, K = map(int, input().split())
belt = deque(list(map(int, input().split())))
dp = deque([0] * N)   #robot 있으면 1, 없으면 0

result = 0
while True:
    result += 1

    #1단계
    belt.rotate(1)  #rotate(1)은 오른쪽으로 이동
    dp.rotate(1)
    dp[-1] = 0

    #2단계
    if sum(dp):
        for i in range(N-2,-1,-1):
            if (dp[i]==1 and dp[i+1]==0 and belt[i+1]>=1):
                dp[i] = 0
                dp[i+1] = 1
                belt[i+1] -= 1
        dp[-1] = 0

    #3단계
    if dp[0] == 0 and belt[0] >= 1:
        dp[0] = 1
        belt[0] -= 1

    #4단계
    if (belt.count(0) >= K):
        print(result)
        break
