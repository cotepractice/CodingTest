#백준 #14889 스타트와 링크
#삼성 SW 역량 테스트 기출
#알고리즘: 브루트포스&백트래킹

N = int(input())
graph = [[0 for _ in range(N)] for _ in range(N)]
visit = [False for _ in range(N)]   #visit에 속하면 Start group
result = float("inf")

for i in range(N):
    graph[i] = list(map(int, input().split()))

def backTracking(depth, idx):
    global result
    if depth == N//2:
        start, link = 0,0
        for i in range(N):
            for j in range(N):
                if visit[i] and visit[j]:
                    start += graph[i][j]
                elif not visit[i] and not visit[j]:
                    link += graph[i][j]
        result = min(result, abs(start-link))
        return

    for i in range(idx, N):
        if not visit[i]:
            visit[i] = True
            backTracking(depth+1,i+1)
            visit[i] = False

backTracking(0,0)
print(result)