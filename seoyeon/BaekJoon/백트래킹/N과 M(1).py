#백준 #15649 N과M(1)
#백트래킹 문제
import copy

N, M = map(int, input().split())
answers = []
visited = [False for _ in range(N+1)]

def backtracking(answer, visited):
    if len(answer)==M:
        answers.append(answer)
        return
    else:
        for k in range(1,N+1):
            if visited[k] == False:
                ansCopy = copy.deepcopy(answer)
                ansCopy.append(k)
                visitedCopy = copy.deepcopy(visited)
                visitedCopy[k] = True
                backtracking(ansCopy, visitedCopy)
                ansCopy = copy.deepcopy(answer)
                visitedCopy = copy.deepcopy(visited)
            
        
for k in range(1,N+1):
    answer = [k]
    visited[k] = True
    backtracking(answer,visited)
    visited[k] = False

for i in range(len(answers)):
    print(*answers[i], sep=" ")