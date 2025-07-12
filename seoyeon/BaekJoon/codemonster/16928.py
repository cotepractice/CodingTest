#16928 뱀과 사다리 게임

# 1. 21% 틀렷습니다 -> 실패
# N, M = map(int,input().split())

# ladder = dict()
# snake = dict()

# for n in range(N):
#     x,y = map(int,input().split()) #x->y로 이동 (x<y)
#     ladder[x] = y

# for m in range(M):
#     u,v = map(int,input().split()) #u->v로 이동(u>v)
#     snake[u] = v

# dp = [float('inf') for _ in range(101)] #주사위 굴려야 하는 최소 횟수
# dp[1] = 0

# current = 1
# while True:
#     if current == 100: 
#         break

#     #사다리가 있으면 사다리 타고 온 횟수
#     for i in range(1,7):
#         next = current+i
#         if 1<=next<101:
#             dp[next] = min(dp[next], dp[current]+1)
#             if next in ladder:
#                 dp[ladder[next]] = min(dp[ladder[next]], dp[next])
#     current += 1

# print(dp[100])

# # 2. 100->1. 1% 틀렸습니다 -> 실패
# ladder 또는 snake가 존재하는 경우 주사위 사용 x
# N, M = map(int,input().split())

# ladder = dict() #ladder[big]=small
# snake = dict()

# for n in range(N):
#     x,y = map(int,input().split()) #x->y로 이동 (x<y)
#     ladder[y]=x

# for m in range(M):
#     u,v = map(int,input().split()) #u->v로 이동(u>v)
#     snake[u]=v

# dp = [float("inf") for _ in range(101)]

# dp[100]=0
# current = 100

# while True:
#     #print("current",current)
#     #print(dp)
#     if current == 1:
#         break

#     if current in ladder:
#         dp[ladder[current]]=min(dp[ladder[current]],dp[current])
#         current -= 1
#         continue

#     if current in snake:
#         dp[snake[current]]=min(dp[snake[current]],dp[current])
#         current -= 1
#         continue

#     for i in range(1,7):
#         next = current-i
#         if 1<=next<100:
#             dp[next]=min(dp[next],dp[current]+1)


#     current -= 1

# #print(*dp)
# print(dp[1])


# #3. BFS -> 성공
# #DP로 해결하는 경우 이전 값으로 돌아가면 이후 값을 다시 계산해야 하므로 효과적이지 않아 BFS로 문제 해결해야 함
# from collections import deque
# import sys

# input = sys.stdin.readline

# N, M = map(int,input().split())

# ladder = dict()
# snake = dict()

# visited = [False for _ in range(101)]

# for n in range(N):
#     x,y = map(int,input().split()) #x<y
#     ladder[x]=y

# for m in range(M):
#     u,v = map(int,input().split()) #u>v
#     snake[u]=v

# def bfs(x):
#     Q = deque()
#     Q.append([x,0])

#     while Q:
#         current_index, current_cnt = Q.popleft()

#         if current_index==100:
#             print(current_cnt)
#             break

#         for i in range(1,7):
#             next_index = current_index + i 
#             #next_index 범위 확인
#             if next_index<1 or next_index>100:
#                 continue
#             #ladder 또는 snake에 있는 경우 반드시 해당 ladder,snake 거쳐야 함
#             if next_index in ladder:
#                 Q.append([ladder[next_index], current_cnt+1])
#             elif next_index in snake:
#                 Q.append([snake[next_index], current_cnt+1])
#             else:
#                 #방문 처리 안하는 경우 시간 초과 발생
#                 if visited[next_index]==False:
#                     visited[next_index]=True
#                     Q.append([next_index, current_cnt+1])

# bfs(1)

#4. heapq 사용 -> 성공

import heapq

N, M = map(int,input().split())

ladder = dict()
snake = dict()

for n in range(N):
    x,y = map(int,input().split()) #x<y
    ladder[x]=y
for m in range(M):
    u,v = map(int,input().split()) #u>v
    snake[u]=v

visited = [False for _ in range(101)]
visited[1]=True

heap = [[0,1]]
heapq.heapify(heap) #[cnt,index]. 앞 파라미터의 최솟값 탐색

while heap:
    cnt,x = heapq.heappop(heap)

    if x==100:
        print(cnt)
        break

    for i in range(1,7):
        next = x+i
        if 1<next<101:
            #1)ladder 또는 snake가 존재하는 인덱스의 경우 반드시 이동해야 함
            if next in ladder:
                heapq.heappush(heap, [cnt+1,ladder[next]])
            elif next in snake:
                heapq.heappush(heap, [cnt+1,snake[next]])
            else:
                #2)주사위 돌려서 가는 경우에는 이미 방문한 적 있으면 해당 값이 최솟값이므로 방문처리해야함
                if visited[next]==False:
                    visited[next]=True
                    heapq.heappush(heap, [cnt+1,next])