#백준 #1956 운동

V, E = map(int, input().split())

matrix = [[float("inf")] * (V+1) for _ in range(V+1)]
for _ in range(E):
    x, y, c = map(int, input().split())
    matrix[x][y] = c

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            if matrix[i][k] + matrix[k][j] < matrix[i][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]

answer = float("inf")
for i in range(1, V+1):
    answer = min(answer, matrix[i][i])

#최소값이 없으면 -1, 있으면 최소값을 출력
if answer == float("inf"):
    print(-1)
else:
    print(answer)