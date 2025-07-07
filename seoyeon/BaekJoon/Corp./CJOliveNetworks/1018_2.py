N,M = map(int,input().split())
boards = [[] for _ in range(N)]

for i in range(N):
    boards[i] = list(input())

def black(x,y):
    result = 0
    for i in range(x,x+8):
        for j in range(y,y+8):
            if i%2==0:
                if j%2==0 and boards[i][j]!="B":
                    result += 1
                if j%2==1 and boards[i][j]!="W":
                    result += 1
            elif i%2==1:
                if j%2==0 and boards[i][j]!="W":
                    result += 1
                if j%2==1 and boards[i][j]!="B":
                    result += 1
    return result

def white(x,y):
    result = 0
    for i in range(x,x+8):
        for j in range(y,y+8):
            if i%2==0:
                if j%2==0 and boards[i][j]!="W":
                    result += 1
                if j%2==1 and boards[i][j]!="B":
                    result += 1
            elif i%2==1:
                if j%2==0 and boards[i][j]!="B":
                    result += 1
                if j%2==1 and boards[i][j]!="W":
                    result += 1
    return result

answer = float("inf")
for i in range(N-7):
    for j in range(M-7):
        ans = min(black(i,j), white(i,j))
        answer = min(answer,ans)
print(answer)