#백준 #2644 촌수계산

def dfs(current,end,ans):
    global relations,answer,visited

    #종결조건
    if current==end:
        answer = ans
        return
    
    for relation in relations[current]:
        if visited[relation]==False:
            visited[relation]=True
            dfs(relation,end,ans+1)


N = int(input())

#촌수 계산해야 하는 서로 다른 두 사람의 번호
inp_lst = list(map(int,input().split()))

#부모 자식들간의 관계 개수
M = int(input())
relations = [[] for _ in range(N+1)] #relations[0]은 1의 자식 리스트
visited=[False for _ in range(N+1)]

for _ in range(M):
    parent,child = list(map(int,input().split()))
    relations[parent].append(child)
    relations[child].append(parent)

answer = -1
visited[inp_lst[0]]=True
dfs(inp_lst[0],inp_lst[1],0)

if answer==-1:
    print(-1)
else:
    print(answer)
