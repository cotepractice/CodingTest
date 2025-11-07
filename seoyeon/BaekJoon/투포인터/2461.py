#백준 #2461 대표 선수

import heapq

N, M = map(int,input().split())
classes=[]

for i in range(N):
    lst=list(map(int,input().split()))
    heapq.heapify(lst)
    classes.append(lst)

answer=1e9
max_val=-1
heap=[] #[val,i]. 값과 반을 함께 넣음

#반에서 가장 작은 학생을 뽑아 heap에 삽입, 가장 큰 값을 max_val로 선택
for i in range(N):
    k=heapq.heappop(classes[i]) 
    heapq.heappush(heap,[k,i])
    max_val=max(max_val,k)


#max_val이 heap에 존재하는 값 중 가장 큰 값
#heap은 항상 3개의 값 존재 
#1.heap에서 가장 작은 학생 now 선택
#2.answer 업데이트
#3.뽑은 now의 교실에 더이상 뽑을 학생이 없는 경우 종결
#4.뽑은 now의 교실에서 가장 작은 학생 tmp 뽑기&max_val 업데이트&heap에 넣기
while True:
    #가장 작은 학생 선택 
    now=heapq.heappop(heap) 
    if answer>abs(now[0]-max_val):
        answer=abs(now[0]-max_val)

    #더이상 뽑을 학생이 없는 경우
    if not classes[now[1]]:
        break
    
    #그 반(classes[now[1]])의 다음으로 가장 작은 학생 점수 뽑기
    tmp=heapq.heappop(classes[now[1]])
    max_val=max(max_val,tmp) #max_val 업데이트
    heapq.heappush(heap,[tmp,now[1]]) #heap에 학생 넣기. [값,방번호]

print(answer)