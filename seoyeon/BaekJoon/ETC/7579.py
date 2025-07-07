#백준 #7579 앱

# #1. Two Pointer? -> 아님
# from collections import defaultdict
# N, M = map(int,input().split())

# m_lst = list(map(int,input().split())) #메모리 사용
# c_lst = list(map(int,input().split())) #비활성화->실행시 드는 비용

# #m_lst의 합이 M이 넘고 c_lst의 합이 가장 작아야 함
# #two pointer

# cm_dict = defaultdict(int)

# for i in range(N):
#     cm_dict[m_lst[i]] = c_lst[i]
# #print(cm_dict)

# #Two Pointer 사용할 것이기 때문에 정렬
# m_lst.sort()

# start,end = 0,0
# #print("m_lst",m_lst)
# #print("dict",cm_dict)

# min_cost = float("inf")
# current_memory = m_lst[start] #M보다 커야함
# current_cost = cm_dict[m_lst[start]] #M보다 큰 경우 가장 작은 cost 찾아야 함
# while end<N-1:
#     #print("start",start,end)
#     #print("current_cost",current_cost)
#     #print("current_memory",current_memory)
    
#     if current_memory<M:
#         end += 1
#         current_cost += cm_dict[m_lst[end]]
#         current_memory += m_lst[end]
    
#     else:
#         #print("here")
#         min_cost = min(min_cost,current_cost)
#         current_cost -= cm_dict[m_lst[start]]
#         current_memory -= m_lst[start]
#         start += 1
# print(min_cost)

#2. DFS -> 시간초과. O(2^N)

# from collections import defaultdict
# N, M = map(int,input().split())

# m_lst = list(map(int,input().split())) #메모리 사용
# c_lst = list(map(int,input().split())) #비활성화->실행시 드는 비용

# min_cost = float("inf")

# def dfs(idx, current_cost,current_memory):
#     global min_cost
#     #print("idx",idx,current_cost,current_memory)
#     if idx==N:
#         return
    
#     if current_memory>=M:
#         min_cost = min(min_cost,current_cost)
#         return
    
#     #현재 idx 넣을지 말지
#     dfs(idx+1,current_cost+c_lst[idx],current_memory+m_lst[idx])
#     dfs(idx+1,current_cost,current_memory)
    
    
# dfs(0,0,0)
# print(min_cost)

#3. DP
# 시간복잡도 O(N*len(c_lst)).N:100,len(c_lst):100

N, M = map(int,input().split())

m_lst = list(map(int,input().split()))
c_lst = list(map(int,input().split()))
row = sum(c_lst) #row는 cost의 합. cost 0부터 row-1까지 탐색
answer = sum(c_lst)

dp = [[0 for _ in range(row)] for _ in range(N)] #dp[i][j]는 메모리. i는 앱의 개수, j는 cost

for i in range(N):
    memory = m_lst[i]
    cost = c_lst[i]

    for j in range(row):
        #j에 담을 수 있는가?
        #1. j<cost: j에 담을 수 없음
        if j<cost:
            dp[i][j] = dp[i-1][j]
        #2. j>=cost: j에 담을 수 있음. 이전과 그대로(dp[i-1][j]) or 앱 비활성화(dp[i-1][j-cost]+memory)
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost]+memory)

        if dp[i][j] >= M:
            answer = min(answer, j)

print(answer)