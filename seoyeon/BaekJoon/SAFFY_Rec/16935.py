#백준 #16935 배열 돌리기 3
from collections import deque

N,M,R = map(int,input().split())

matrix = [[0 for _ in range(M)] for _ in range(N)]

for n in range(N):
    n_lst = list(map(int,input().split()))
    matrix[n] = n_lst

def func1():
    global matrix
    N = len(matrix)
    M = len(matrix[0])

    Q = deque()
    for n in range(N):
        for m in range(M):
            Q.append(matrix[n][m])
    
    ans_matrix = [[0 for _ in range(M)] for _ in range(N)]
    for n in range(N-1,-1,-1):
        for m in range(M):
            ans_matrix[n][m] = Q.popleft()
    return ans_matrix

def func2():
    global matrix
    N = len(matrix)
    M = len(matrix[0])

    Q = deque()
    for n in range(N):
        for m in range(M):
            Q.append(matrix[n][m])
    
    ans_matrix = [[0 for _ in range(M)] for _ in range(N)]
    for n in range(N):
        for m in range(M-1,-1,-1):
            ans_matrix[n][m] = Q.popleft()
    return ans_matrix

def func3():
    global matrix
    N = len(matrix)
    M = len(matrix[0])

    Q = deque()
    for n in range(N):
        for m in range(M):
            Q.append(matrix[n][m])
    
    ans_matrix = [[0 for _ in range(N)] for _ in range(M)]
    for n in range(N-1,-1,-1):
        for m in range(M):
            q = Q.popleft()
            ans_matrix[m][n] = q

    return ans_matrix

def func4():
    global matrix
    N = len(matrix)
    M = len(matrix[0])

    Q = deque()
    for n in range(N):
        for m in range(M):
            Q.append(matrix[n][m])
    
    ans_matrix = [[0 for _ in range(N)] for _ in range(M)] #matrix[M][N]
    for n in range(N):
        for m in range(M-1,-1,-1):
            q = Q.popleft()
            ans_matrix[m][n] = q

    return ans_matrix

def func5():
    global matrix
    N = len(matrix)
    M = len(matrix[0])

    Q = deque()
    for n in range(N//2):
        for m in range(M//2):
            Q.append(matrix[n][m])
    for n in range(N//2):
        for m in range(M//2,M):
            Q.append(matrix[n][m])
    for n in range(N//2,N):
        for m in range(M//2,M):
            Q.append(matrix[n][m])
    for n in range(N//2,N):
        for m in range(M//2):
            Q.append(matrix[n][m])
    
    ans_matrix = [[0 for _ in range(M)] for _ in range(N)]
    for n in range(N//2):
        for m in range(M//2,M):
            #print("nm",n,m)
            ans_matrix[n][m] = Q.popleft()
    for n in range(N//2,N):
        for m in range(M//2,M):
            #print("nm",n,m)
            ans_matrix[n][m] = Q.popleft()
    for n in range(N//2,N):
        for m in range(M//2):
            #print("nm",n,m)
            ans_matrix[n][m] = Q.popleft()
    for n in range(N//2):
        for m in range(M//2):
            #print("nm",n,m)
            ans_matrix[n][m] = Q.popleft()
    return ans_matrix 

def func6():
    global matrix
    N = len(matrix)
    M = len(matrix[0])
    
    Q = deque()
    for n in range(N//2):
        for m in range(M//2):
            Q.append(matrix[n][m])
    for n in range(N//2):
        for m in range(M//2,M):
            Q.append(matrix[n][m])
    for n in range(N//2,N):
        for m in range(M//2,M):
            Q.append(matrix[n][m])
    for n in range(N//2,N):
        for m in range(M//2):
            Q.append(matrix[n][m])
    
    ans_matrix = [[0 for _ in range(M)] for _ in range(N)]
    for n in range(N//2,N):
        for m in range(M//2):
            ans_matrix[n][m] = Q.popleft()
    for n in range(N//2):
        for m in range(M//2):
            ans_matrix[n][m] = Q.popleft()
    for n in range(N//2):
        for m in range(M//2,M):
            ans_matrix[n][m] = Q.popleft()
    for n in range(N//2,N):
        for m in range(M//2,M):
            ans_matrix[n][m] = Q.popleft()
    
    return ans_matrix

inp = list(map(int,input().split()))
for r in range(R):
    if inp[r] == 1:
        matrix = func1()
        
    if inp[r] == 2:
        matrix = func2()
        #print(func2())
    if inp[r] == 3:
        matrix = func3()
        #print(func3())
    if inp[r] == 4:
        matrix = func4()
        #print(func4())
    if inp[r] == 5:
        matrix = func5()
        #print(func5())
    if inp[r] == 6:
        matrix = func6()
        #print(func6())
for x in range(len(matrix)):
    print(*matrix[x], sep=" ",end="\n")