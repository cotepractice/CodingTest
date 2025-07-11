#1. 테스크케이스 모두 성공. "3% 틀렸습니다" 
from collections import defaultdict

N, M = map(int,input().split())
know = list(map(int,input().split()))

partys = [[] for _ in range(M)]
for m in range(M):
    party = list(map(int,input().split()))
    partys[m] = party

#진실을 아는 사람과 같은 파티 가는 사람 체크

#1)진실을 아는 사람, 진실을 모르는 사람 섞여있을 때 -> 진실로 대답
#2)어떤 사람이 어떤 파티에서 진실을 듣고, 또다른 파티에서 과장된 이야기를 들으면 안 됨

#1. 진실을 아는 사람 체크
#+) party 순서에 따라 정답 다름. 확인 필요
know_people = dict()
for i in range(1,know[0]+1):
    know_people[know[i]]=0

partys.sort(reverse=True)

for party in partys:
    know_bool = 0 #아는 사람 있으면 1, 없으면 0
    for i in range(1,party[0]+1):
        if party[i] in know_people:
            know_bool = 1
    #아는 사람 한 명이라도 있으면, 그 파티의 모든 사람은 진실을 암
    if know_bool==1:
        for i in range(1,party[0]+1):
            if party[i] not in know_people:
                know_people[party[i]]=0

result = 0
#2. 파티에서 한 명도 없어야 함
for party in partys:
    ans = 1
    for i in range(1,party[0]+1):
        if party[i] in know_people:
            ans = 0

    result += ans
print(result)