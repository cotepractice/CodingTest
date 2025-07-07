#백준 #15650 N과 M(2)

N, M = map(int, input().split())

def backtracking(n, ans):

    if len(ans)== M:
        print(*ans)
        return
    
    for i in range(n,N+1):
        ans.append(i)
        backtracking(i+1,ans)
        ans.pop()

ans = []
backtracking(1, ans)