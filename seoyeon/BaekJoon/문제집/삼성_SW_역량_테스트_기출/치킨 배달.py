#백준 #15686 치킨 배달
#삼성 SW 역량 테스트 기출
#16:13-
from itertools import combinations

N, M = map(int, input().split())
Maps = [[0 for _ in range(N)] for _ in range(N)]
chickens = []   #치킨 좌표
houses = []     #집 좌표


for i in range(N):
    Maps[i] = list(map(int, input().split()))

chickenCnt = 0
houseCnt = 0
for i in range(N):
    for j in range(N):
        if Maps[i][j] == 2:
            chickens.append((i,j))
            chickenCnt += 1            
        elif Maps[i][j] == 1:
            houses.append((i,j))
            houseCnt += 1

#모든 조합 찾아 가장 작은 치킨거리 찾기
answer = 1000000
#print(combinations(chickens,M))
for combi in combinations(chickens,M):  #chickens에 있는 원소들 중 M개 선택. combination
    #print("combi",combi)
    sum_distance = 0    #모든 집에서의 치킨거리
    for house in houses:
        temp = 1000000  #하나의 집에서의 치킨거리 찾기
        #집 기준 모든 치킨집과의 조합에서 가장 작은 치킨거리 찾기
        for x,y in combi:   #모든 조합 중 가장 작은 치킨거리 찾기
            temp = min(temp, abs(x-house[0])+abs(y-house[1]))   
        sum_distance += temp
    answer = min(answer, sum_distance)  #도시의 치킨거리 찾기
print(answer)