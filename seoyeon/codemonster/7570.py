#백준 #7570 줄 세우기
from collections import deque


N = int(input())
n_lst = list(map(int,input().split()))

# 한 명을 제일 앞이나 뒤로 보낼 수 있음
# 번호 순서대로 줄 세울 수 있는 최솟값

#1. Q 사용 -> 경우에 따라 현재 값을 앞으로 보낼지 앞의 값을 뒤로 보낼지 달라져 정확하게 계산 안 됨 
# prev = n_lst[0]
# ans = 0
# Q = deque() #Q는 오름차순 정렬 상태

# for n in n_lst:
#     #Q가 존재하고 최근 값이 n보다 큰 경우 빼기
#     while Q:
#         #Q의 가장 큰 값보다 큰 경우, 1)현재 값을 앞으로 보내거나 2)가장 큰 값을 뒤로 보내야 함
#         if Q[-1]<n:
#             Q.pop()
#             ans += 1
#         #Q의 가장 작은 값보다 작은 경우
#         elif n<Q[0]:
#             ans += 1
            
#     #현재 값 넣기
#     Q.append(n)
    
#2. 가장 긴 수열 탐색

dp = [0] * (N + 1)
max_cnt = 0

for n in n_lst:
    # 내 번호(n)보다 1 작은 번호(n-1)가 이전에 몇 번 연속됐었는지 확인
    # 만약 n-1이 나온 적 없다면 dp[n-1]은 0일 것이고, n은 새로운 시작(1)이 됨
    dp[n] = dp[n-1] + 1
    
    if dp[n] > max_cnt:
        max_cnt = dp[n]

print(N - max_cnt)