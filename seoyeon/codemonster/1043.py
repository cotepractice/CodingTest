# #1. 테스크케이스 모두 성공. "3% 틀렸습니다" 
# from collections import defaultdict

# N, M = map(int,input().split())
# know = list(map(int,input().split()))

# partys = [[] for _ in range(M)]
# for m in range(M):
#     party = list(map(int,input().split()))
#     partys[m] = party

# #진실을 아는 사람과 같은 파티 가는 사람 체크

# #1)진실을 아는 사람, 진실을 모르는 사람 섞여있을 때 -> 진실로 대답
# #2)어떤 사람이 어떤 파티에서 진실을 듣고, 또다른 파티에서 과장된 이야기를 들으면 안 됨

# #1. 진실을 아는 사람 체크
# #+) party 순서에 따라 정답 다름. 확인 필요
# know_people = dict()
# for i in range(1,know[0]+1):
#     know_people[know[i]]=0

# partys.sort(reverse=True)

# for party in partys:
#     know_bool = 0 #아는 사람 있으면 1, 없으면 0
#     for i in range(1,party[0]+1):
#         if party[i] in know_people:
#             know_bool = 1
#     #아는 사람 한 명이라도 있으면, 그 파티의 모든 사람은 진실을 암
#     if know_bool==1:
#         for i in range(1,party[0]+1):
#             if party[i] not in know_people:
#                 know_people[party[i]]=0

# result = 0
# #2. 파티에서 한 명도 없어야 함
# for party in partys:
#     ans = 1
#     for i in range(1,party[0]+1):
#         if party[i] in know_people:
#             ans = 0

#     result += ans
# print(result)

#2. Find-Union
#O(M)
N, M = map(int,input().split())
know = list(map(int,input().split()))[1:]
parties = [[] for _ in range(M)]
parent = [i for i in range(N+1)]

#Find-Union
#find(): 연관된 가장 작은 parent 값 탐색
def find(parent,n):
    if parent[n]!=n:
        parent[n] = find(parent,parent[n])
    return parent[n]

#union(): 두 값 x,y가 알고 있는지 여부에 따라 1)알고 있는 값의 find() 값으로 통일 또는 2)둘 다 모르는 경우 더 작은 값으로 업데이트
def union(parent,x,y,know):
    x = find(parent,x)    
    y = find(parent,y)
    
    if x in know and y in know:
        return 
    #알고 있는 사람이 있는 경우 모르는 사람의 parent 값을 해당 사람으로 변경
    if x in know:
        parent[y]=x
    elif y in know:
        parent[x]=y
    #둘 다 모르는 경우, 더 작은 값으로 parent 업데이트
    else:
        if x<y:
            parent[y]=x
        else:
            parent[x]=y

for m in range(M):
    party_all = list(map(int,input().split()))
    party_n = party_all[0] #party 인원 수 
    party = party_all[1:] #party 인원 리스트
    parties[m] = party 
    #동일한 파티에 참석하는 인원 union
    for i in range(party_n-1):
        union(parent,party[i],party[i+1],know)

ans = 0
for i in range(M):
    for j in range(len(parties[i])):
        if find(parent, parties[i][j]) in know:
            break
    else:
        ans += 1
        
print(ans)