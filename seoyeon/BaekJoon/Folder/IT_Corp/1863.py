#백준 #1863 스카이라인 쉬운거
#19:50-

#구현
#최소 건물 개수
from collections import defaultdict
N=int(input())
skyline_dict=dict()
skyline_pos=[0 for _ in range(N)] 
height_x=defaultdict(list) #0은 넣지 않음


for i in range(N):
    x,y = map(int,input().split()) 
    skyline_pos[i]=y
    skyline_dict[x]=y
    if y!=0:
        height_x[y].append(i)

#이미 앞에 나온 높이인 경우 pass, 그렇지 않으면 answer+=1
#고려사항: 
# 1.같은 높이여도 사이에 본인보다 낮은 건물이 있으면 각각 계산
# 2.본인보다 낮은 건물이 없으면 하나로 계산
answer=0
for height in height_x:
    lst=height_x[height]

    start=lst[0]
    end=lst[-1]

    if start==end:
        answer+=1
        continue

    cnt=1 #높이가 height일 때 건물의 개수. 최초 건물 수 1
    check=True #check로 이전 height 건물과 이어지는지 판단
    while start<end+1:

        #1)이어져 있는 상황에 자신보다 작은 빌딩 존재하는 경우, check=False
        if check==True and skyline_pos[start]<height:
            check=False

        #2)이어져 있지 않을 때 height 건물을 마주한 경우 check=True 변경 후 cnt 1 증가
        if check==False and skyline_pos[start]==height:
            check=True
            cnt+=1
        
        start+=1
    
    answer+=cnt

print(answer)

