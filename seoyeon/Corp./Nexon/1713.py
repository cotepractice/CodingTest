#백준 #1713 후보 추천하기
from collections import defaultdict

N = int(input()) #N:사진틀 개수 
M = int(input()) #M:len(recommends)
recommends = list(map(int,input().split()))

#1.비어있는 사진틀이 없는 경우 현재까지 추천받은횟수가 가장 적은 학생 삭제 후 새로운 학생 게시
# 이때 추천 받은 횟수가 가장 적은 학생이 2명 이상인 경우, 게시된지 가장 오래된 사진 삭제
#2.게시된 학생이 다른 학생의 추천을 받은 경우 추천받은 횟수 증가

#O(M*N)
dict = defaultdict(list) #[추천횟수,게시된시간]
for t in range(M):
    #기존에 존재
    if recommends[t] in dict:
        dict[recommends[t]][0] += 1
        continue
    #기존에 존재 X
    #1.즉시 넣을 수 있는 경우
    if len(dict)<N:
        dict[recommends[t]]=[1,t]
    #2.그렇지 않은 경우, 처리 필요
    else:
        lst = [] #[학생번호,추천횟수,게시된시간]
        for d in dict:
            lst.append([d,dict[d][0],dict[d][1]])
        lst.sort(key=lambda x:(-x[1],-x[2])) #추천횟수 많고,게시된 시간은 최근(커야함)
        del dict[lst[-1][0]] #마지막 삭제
        dict[recommends[t]]=[1,t]

answer = []
for d in dict:
    answer.append(d)
answer.sort()
print(*answer)