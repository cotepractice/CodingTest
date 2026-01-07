#백준 #2240 자두나무
#16:40-18:30

#매초 두 나무 중 하나에서 열매가 떨어짐
#떨어지는 순간 그 나무 아래에 서 있으면 받아먹을 수 있음
#두 나무를 이동하는 시간은 1초보다 훨씬 잛음
#(과일)자두는 T초동안 떨어지고, (인간)자두는 최대 W번만 움직이고 싶음
#자두가 받을 수 있는 자두의 개수 출력
#자두는 1번 자두나무 아래에 위치

# #1. Backtracking. 시간초과 
# #시간복잡도 O(2**T)

# #pos: 현재 서 있는 나무 위치, change_cnt: 위치 변경 횟수
# #count: 받은 자두 개수, idx: 현재 인덱스, lst: 자두 리스트
# def backtracking(pos,change_cnt,count,idx,lst):
#     global answer
#     #종결 조건: idx=len(lst)-2인 경우, 다음이 마지막 인덱스
#     if idx==len(lst)-2:
#         if lst[idx+1]==pos:
#             count+=1
#         elif lst[idx+1]!=pos and change_cnt<W:
#             count+=1
#         answer = max(answer,count)
#         return

#     #현재 떨어지는 자두가 서 있는 위치 pos와 일치하는 경우 count만 증가
#     if lst[idx+1]==pos:
#         backtracking(pos,change_cnt,count+1,idx+1,lst)
#     #일치하지 않는 경우, 1)변경하거나 2)뛰어넘기
#     else:
#         #1) 위치 변경
#         if change_cnt<W:
#             if pos==0: tmp_pos=1
#             else: tmp_pos=0

#             backtracking(tmp_pos, change_cnt+1,count+1,idx+1,lst)
#         #2) 위치 변경하지 않음
#         next = idx+1
#         while True:
#             if next<len(lst) or lst[next]==pos:
#                 break
#             next+=1

#         if next<len(lst):
#             backtracking(pos,change_cnt,count+1,next,lst)

# T, W = map(int,input().split())
# trees = [0 for _ in range(T)]
# answer = 0

# for i in range(T):
#     tree = int(input()) #자두가 떨어지는 나무 번호
#     trees[i]=tree-1 #자두 나무 1,2 -> 0,1로 변경

# backtracking(0,0,0,0,trees)
# print(answer)

#2. DP.Bottom Up
# 시간복잡도 O(T*N)

T,W = map(int,input().split())
trees = [0 for _ in range(T+1)]

for t in range(1,T+1):
    c=int(input())
    trees[t]=c-1

dp = [[0 for _ in range(W+1)] for _ in range(T+1)]

for t in range(1,T+1):
    current_pos = trees[t] #현재 위치: 0 또는 1

    #0부터 W(포함)까지
    for w in range(W+1):
        #초기 위치는 0
        #w%2=0인 경우, 위치 0
        #w%2=1인 경우, 위치 1
        if w%2==0:
            pos = 0
        else:
            pos = 1
        
        #current_pos와 pos 비교해 현재 자두를 추가할 수 있는지 확인
        if current_pos == pos:
            score = 1
        else:
            score = 0

        #1) 가만히 있는 경우
        #이전 시간(t-1)에서 w 값 동일
        dp[t][w] = dp[t-1][w] + score

        #2) 움직이는 경우: 이전 시간(t-1)의 이전 이동 획수(w-1)에서 옴
        #현재 값( 직전 1)에서 진행한 값) 또는 이전에서 온 경우의 최댓값
        if w>0:
            dp[t][w] = max(dp[t][w], dp[t-1][w-1] + score)

print(max(dp[T]))

#** 위치와 이동횟수
#t초에 w번 움직였을 때 가질 수 있는 최대 자두 개수 -> 이해하기 더 쉬움
#w번 움직였을 때 t초에 가질 수 있는 최대 자두 개수

