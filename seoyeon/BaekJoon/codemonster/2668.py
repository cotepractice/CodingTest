# #1. 완전탐색 -> 4% 틀렸습니다
# N = int(input()) #N: 최대 100
# n_lst = [-1 for _ in range(N)]

# for i in range(N):
#     k = int(input())
#     n_lst[i]=k

# ans = dict() #1부터 시작
 
# #현재 상황
# for i in range(N):
#     if i+1==n_lst[i]:
#         ans[i+1]=0

# #완전탐색
# for i in range(N):
#     if i in ans:
#         continue
#     for j in range(N):
#         if j in ans:
#             continue
        
#         if n_lst[i]==j+1 and n_lst[j]==i+1:
#             ans[i+1]=0
#             ans[j+1]=0
#         elif n_lst[j]==i+1:
#             ans[i+1]=0
#             n_lst[i]=j+1
#         elif n_lst[i]==j+1:
#             ans[j+1]=0
#             n_lst[j]=i+1

# print(len(ans))
# for i in range(1,N+1):
#     if i in ans:
#         print(i)

#2. DFS

N = int(input())
boards = [-1 for _ in range(N+1)]

for i in range(1,N+1):
    n = int(input())
    boards[i]=n

n_dict = dict() #n_dict[i]=k. i:index,k:i번째값
result = []

#방문한 적 없으면 해당 index 숫자로 다시 dfs() 진행
def dfs(index,i): #파라미터 index, 초기 숫자(해당 숫자로 사이클 형성 판단)
    visited[index]=True
    current_n = boards[index]
    #현재 index의 숫자를 방문한 적 없는 경우, 재귀로 계속 탐색
    #boards[index] -> boards[boards[index]] -> ...
    #사이클을 이루는 숫자 탐색 !
    if visited[current_n]==False:
        dfs(current_n,i)
    #현재 index의 숫자를 방문한 적 있는 경우, 재귀로 찾은 현재 숫자 값 current_n이 초기 숫자값 i와 같은 경우 result 추가
    elif visited[current_n]==True and current_n==i:
        result.append(current_n) #current_n=i
        #Q.current_n만 넣는 것이 아니라 전체 사이클 모든 숫자를 넣어야 하는 것 아닌가?
        #A.main문에서 for문 돌면서 초기 숫자를 넣기 때문에 가능

result = []
for i in range(1,N+1):
    visited = [False for _ in range(N+1)]
    dfs(i,i)

print(len(result))
result.sort()

for n in result:
    print(n)