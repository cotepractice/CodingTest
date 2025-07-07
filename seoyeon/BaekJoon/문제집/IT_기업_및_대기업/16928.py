#백준 #16928 뱀과 사다리 게임

#1. Greedy. 틀렸습니다
# from collections import defaultdict

# N,M = map(int,input().split())
# ladder = defaultdict() #ladder[x]=y. x<y
# snake = defaultdict() #snake[u]=v. u>v

# for i in range(N):
#     x,y = map(int,input().split())
#     ladder[x]=y
# for i in range(M):
#     u,v = map(int,input().split())
#     snake[u]=v


# #ladder 타야함
# current = 1
# dice = [i for i in range(1,7)]

# cnt = 0
# while True:
#     print("current",current)
#     cnt += 1
#     next = current #현재 최종 위치
#     max_next = current
#     for i in dice:
#         next = current+i
#         if next in snake:
#             next = snake[next]
#         if next in ladder:
#             next = ladder[next]
#         max_next = max(max_next,next)
#     if max_next>=100:
#         break
#     current = max_next

# print(cnt)

#2. BFS&DP
#DP로 해결하는 경우 뱀을 거치면 관련된 모든 값이 변경되어야 하는데 그러지 않고 해당 값만 변경되어 해결할 수 없음
# from collections import defaultdict

# N,M = map(int,input().split())
# ladder = defaultdict() #ladder[x]=y. x<y
# snake = defaultdict() #snake[u]=v. u>v

# for i in range(N):
#     x,y = map(int,input().split())
#     ladder[x]=y
# for i in range(M):
#     u,v = map(int,input().split())
#     snake[u]=v

# dp = [float("inf") for _ in range(101)]
# dp[1]=0

# for i in range(1,101):
#     for j in range(1,7):
#         next = i+j
#         if next >= 101:
#             continue
#         if next in ladder:
#             next = ladder[next]
#         if next in snake:
#             next = snake[next]
#         dp[next]=min(dp[next],dp[i]+1)

# print(dp[100])

#3.BFS

from collections import deque
N,M = map(int,input().split())

boards = [0 for _ in range(101)]
visited = [False for _ in range(101)]

for i in range(N):
    x,y = map(int,input().split())
    boards[x]=y
for i in range(M):
    u,v = map(int,input().split())
    boards[u]=v

Q = deque()
Q.append(1)
visited[1]=True

dice = [i for i in range(1,7)]
answer = [0 for _ in range(101)]

while Q:
    current = Q.popleft()

    for i in dice:
        next = current+i
        if next > 100:
            continue

        if boards[next]!=0:
            next = boards[next]

        if visited[next]==False:
            visited[next]=True
            answer[next] = answer[current]+1
            Q.append(next)

print(answer[100])