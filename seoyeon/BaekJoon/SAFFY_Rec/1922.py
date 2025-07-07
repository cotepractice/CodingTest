#백준 #1922 네트워크 연결
#MST(Minimum Spanning Tree) -> Kruskal's Algorithm

def find_parent(parent,n):

    if parent[n]!=n:
        parent[n] = find_parent(parent,parent[n])
    return parent[n]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b
    return parent

N = int(input())
M = int(input())
parent = [i for i in range(N)]

edges = []

for m in range(M):
    a,b,c = map(int,input().split())

    edges.append([c,a-1,b-1])

#오름차순 정렬
edges.sort()

ans = 0

for edge in edges:
    c,a,b = edge

    #find_parent가 같은 경우 이미 연결되어 있음
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        ans += c

print(ans)