#백준 #14676 영우는 사기꾼?

#1. 기본 Python3의 경우, 시간 초과 발생 O(K*N)
# sys.stdin.readline과 pypy 활용해 시간복잡도 문제 해결
#성공

import sys

input = sys.stdin.readline

#N:건물 종류 개수, M:건물 사이 관계 개수, K:게임 정보 개수
N,M,K = map(int,input().split())

#connections[a]=[b1,b2,...]. a가 건설되기 위해 b1,b2,... 필요
connections = [[] for _ in range(N)]
#instructions=[[action1,building1], [action2,building2], ...]
instructions = []

for m in range(M):
    x,y = map(int,input().split())
    connections[y-1].append(x-1)
    #connections[y-1]+=1

for k in range(K):
    action, building = map(int,input().split())
    instructions.append([action,building-1])

#건설된 건물
build_n = [0 for _ in range(N)]

ans=True
for act,b in instructions:
    #1.act가 1인 경우, connections를 통해 현재 빌딩을 지을 수 있는지 확인
    # 지을 수 있는 경우 build_n 업데이트
    check=True
    if act==1:
            
        for prev in connections[b]:
            if build_n[prev]<=0:
                check=False
        
        if check==True:
            build_n[b]+=1
        else:
            ans=False
            break


    #2.act가 2인 경우, build_n을 통해 지어진 빌딩이 있는지 확인
    else:
        if build_n[b]>0:
            build_n[b]-=1
        else:
            ans=False
            break

if ans==False:
    print("Lier!")
else:
    print("King-God-Emperor")

