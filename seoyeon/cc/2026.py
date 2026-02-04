#백준 #2026 소풍

#1. Backtracking 시간초과발생
# O(nCk)

# K,N,F = map(int,input().split())
# friends = [[] for _ in range(N)]

# for f in range(F):
#     #양방향 
#     x,y = map(int,input().split()) 
#     friends[x-1].append(y-1)
#     friends[y-1].append(x-1)

# #K명 선발
# # 단 첫 번째 학생의 번호가 제일 작은 순서대로 출력

# ans = 0
# def dfs(idx,lst,current_n):
#     global ans

#     if current_n==K:
#         ans=lst
#         return
    
#     if idx>=N:
#         return
    
#     #1)넣는 경우
#     #현재 모두와 친구인 경우
#     #friends[idx]가 K 미만인 경우 패스

#     current_lst = friends[idx]
#     check = True #모두와 친구인 경우
#     for ff in lst:
#         if ff not in current_lst:
#             check = False
#     if check==True:
#         tmp=lst[:]
#         tmp.append(idx)
#         dfs(idx+1,tmp,current_n+1)
    
#     #2)넣지 않는 경우
#     dfs(idx+1,lst,current_n)

# dfs(0,[],0)

# for aa in ans:
#     print(aa+1)

# #2. 
# import sys

# input = sys.stdin.readline

# K,N,F = map(int,input().split())

# #friends[x1]=[y1,y2,...]는 x1과 y1, x1과 y2가 좋아하는 사이
# #단, 중복을 방지하기 위해 x1은 x1과 y1 중 작은 값, y1은 x1과 y1의 큰 값 의미
# friends = [[] for _ in range(N)]

# for f in range(F):
#     #양방향 
#     x,y = map(int,input().split()) 
#     friends[min(x-1,y-1)].append(max(x-1,y-1))
#     friends[max(x-1,y-1)].append(min(x-1,y-1))

# dp = [False for _ in range(N)]

# ans = []

# #friends[idx] 내 친구 탐색
# #idx는 반드시 포함
# def backtracking(main_idx,current,lst,cnt):
#     global ans 

#     if cnt==K:
#         ans = lst
#         return

#     if current >= len(friends[main_idx]):
#         return

#     #1) 현재 current의 friends 리스트 탐색
#     current_lst = friends[friends[main_idx][current]]

#     if len(current_lst)<K:


#     #2) 이전까지 담은 친구 리스트 존재하는지 확인
#     # 존재하지 않는 경우 check=False
#     check = True
#     #print("current_lst",current_lst)
#     for l in lst:
#         #print("l",l)
#         if l!=current and l not in current_lst:
#             check = False
#     #모두 만족하는 경우 친구 리스트 넣을 수 있음
#     if check:
#         tmp = lst[:]
#         tmp.append(friends[main_idx][current])
#         backtracking(main_idx,current+1,tmp,cnt+1)
#     #3) ㅊ니구리스트 넣지 않는 경우
#     backtracking(main_idx,current+1,lst,cnt)


# for nn in range(N):
#     #friends[nn] 길이가 K보다 크거나 같은 경우에만 backtracking 실행
#     if len(friends[nn])>=K-1:
#         backtracking(nn,0,[nn],1)
#         if ans!="[]":
#             break

# if len(ans)==0:
#     print(-1)
# else:
#     for aa in ans:
#         print(aa+1)

#3. 
from sys import stdin
from heapq import heappush,heappop

input = stdin.readline

k,n,f = map(int, input().split())
adj_list = [[] for _ in range(n+1)]
adj_mat = [[False]*(n+1) for _ in range(n+1)]

#인접행렬 모두 True 설정
for _ in range(f):
    a,b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

    adj_mat[a][b] = adj_mat[b][a] = True

for idx in range(1,n+1):
    adj_list[idx].sort()
end = -1

#인덱스를 모두 돌며 bfs() 함수 실행
#정렬을 통해 문제에 주어진대로 출력
def solv():
    for start in range(1,n+1):
            rst = bfs(start)
            if rst:
                rst.sort()
                for num in rst:
                    print(num)
                return
    print(-1)

#bfs()
# 시작지점 start를 heapq에 삽입
# 인접 행렬 모두 탐색해 방문한 적 없는 경우, 방문 처리 &현재까지의 path를 모두 돌며 가지고 있는지 확인
# 이때 path에 해당하는 인접행렬이 하나라도 False인 경우 flag=True. 친구 리스트에 들어갈 수 없음
# flag=False인 경우 path에 추가 & path 총 길이가 k인 경우 종결
def bfs(start):
    visited = [False]*(n+1)
    path = [start]
    pq = [start]
    visited[start] = True
    while pq:
        now = heappop(pq)
        for nxt in adj_list[now]:
            if not visited[nxt]:
                visited[nxt] = True
                flag = False
                for target in path:
                    if not adj_mat[nxt][target]:
                        flag = True
                        break
                if not flag:
                    path.append(nxt)
                    if len(path) == k:
                        return path
                    heappush(pq,nxt)
    return None

if k == 1:
    print(1)
else:
    solv()