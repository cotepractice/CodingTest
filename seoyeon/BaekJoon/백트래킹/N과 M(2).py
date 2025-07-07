#백준 #15650 N과 M(2)
#백트래킹 문제
import copy

N, M = map(int,input().split())
visited = [False for _ in range(N+1)]
answers = []

def backtracking(answer,visited):
    if len(answer)==M:
        answers.append(answer)
        return
    else:
        for k in range(answer[-1],N+1):
            ansCopy = copy.deepcopy(answer)
            visitedCopy = copy.deepcopy(visited)
            if visited[k] == False:
                ansCopy.append(k)
                visitedCopy[k] = True
                backtracking(ansCopy,visitedCopy)
                ansCopy = copy.deepcopy(answer)
                visitedCopy = copy.deepcopy(visited)


for m in range(1,N+1):
    answer = [m]
    visited[m] = True
    backtracking(answer,visited)
    visited[m] = False

for i in range(len(answers)):
    print(*answers[i], sep=" ")