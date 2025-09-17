N = int(input()) #N: 학생 수
M = int(input()) #M: 인간관계 수

enemy = [[] for _ in range(N+1)]
parent = [i for i in range(N+1)]

#find()
def find(parent,x):
    if parent[x]!=x:
        parent[x] = find(parent,parent[x])
    return parent[x]

#union()
def union(parent,x,y):
    x = find(parent,x)
    y = find(parent,y)

    if x<y:
        parent[y]=x
    else:
        parent[x]=y

for _ in range(M):
    relation, a, b = input().split()
    a = int(a)
    b = int(b)

    if relation=="F":
        union(parent,a,b)
    else:
        enemy[a].append(b)
        enemy[b].append(a)

for i in range(1,N+1):
    #공통된 적(i)를 가지는 친구들은 모두 친구
    #공통된 적 i. 그의 적: enemy[i]
    #즉, enemy[i]=[3,1]인 경우 3과 1은 서로 친구
    #enemy[i]에서 e1번째와 e2번째는 서로 친구
    for e1 in range(len(enemy[i])):
        for e2 in range(e1+1,len(enemy[i])):
            union(parent,enemy[i][e1],enemy[i][e2])

answer = set()
for i in range(1,N+1):
    answer.add(find(parent,i))

print(len(answer))