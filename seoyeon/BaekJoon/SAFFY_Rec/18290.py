# #백준 #18290 NM과 K(1)

# N, M, K = map(int, input().split())

# lst = [[0 for _ in range(M)] for _ in range(N)]

# for i in range(N):
#     l = list(map(int,input().split()))
#     lst[i] = l

# max_n = -1 * float("inf")

# def backtracking(x,y,sum,cnt):
#     global lst, max_n

#     if cnt == K:
#         max_n = max(max_n,sum)
#         return

#     for i in range(x,N):
#         for j in range(y if i==x else 0,M):
#             #자기자신과 인접한 칸인 경우 제외
#             if (i==x and j==y) or (abs(i-x)+abs(j-y) == 1):
#                 continue

#             sum += lst[i][j]
#             cnt += 1
#             backtracking(i,j,sum,cnt)
#             sum -= lst[i][j]
#             cnt -= 1

# for i in range(N):
#     for j in range(M):
#         sum = lst[i][j]
#         backtracking(i,j,sum,1)

# print(max_n)

#백준 #18290 NM과 K(1)

N, M, K = map(int, input().split())

lst = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    l = list(map(int,input().split()))
    lst[i] = l

max_n = -1 * float("inf")

def backtracking(x,y,sum,cnt):
    global lst, max_n

    if cnt == K:
        max_n = max(max_n,sum)
        return

    for i in range(x,N):
        for j in range(y if i==x else 0,M): #i==x인 경우 j는 y<=j<M, 이후의 i부터는 0<=j<M
            if [i, j] not in Q:
                #[i,j]는 Q 안의 모든 좌표와 비교했을 때 인접하면 안 됨
                if ([i+1,j] not in Q) and ([i-1,j] not in Q) and ([i,j+1] not in Q) and ([i,j-1] not in Q):
                    Q.append([i,j])
                    backtracking(i,j,sum+lst[i][j],cnt+1)
                    Q.pop()


Q = []
backtracking(0,0,0,0)
print(max_n)