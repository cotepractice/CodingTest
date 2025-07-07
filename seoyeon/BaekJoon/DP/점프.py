#백준 #1890 점프
#DP문제

N = int(input())
lst = [[0 for _ in range(N)] for _ in range(N)]
check = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    lst[i] = list(map(int, input().split()))
check[0][0] = 1

for i in range(N):
    for j in range(N):
        if lst[i][j] != 0 and check[i][j] != 0:
            if i+lst[i][j]<N:
                check[i+lst[i][j]][j] += check[i][j]
            if j+lst[i][j]<N:
                check[i][j+lst[i][j]] += check[i][j]

print(check[-1][-1])