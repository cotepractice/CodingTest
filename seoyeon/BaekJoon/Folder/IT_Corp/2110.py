#백준 #2110 공유기 설치

#15:00-

#Backtracking
#도현의 집 N개가 수직선 위에 존재, 집에 공유기 설치
#공유기 C개 설치하고, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치
N, C = map(int,input().split())
house=[]

for _ in range(N):
    house.append(int(input()))

house.sort()
max_d=0


#투 포인터
def check(lst):
    left=0

    current_d=float("inf")

    for i in range(1,len(lst)):
        right=i

        current_d=min(current_d,lst[right]-lst[left])
        left=right

    return current_d


def back(idx,cnt,lst):
    global max_d

    #종결조건: cnt=0인 경우 더 할 필요 없음
    if idx==N or cnt==0:
        if len(lst)!=C:
            return
        distance=check(lst)
        max_d=max(max_d,distance)
        #print(distance, lst)
        return
    
    #공유기 설치하는 경우
    back(idx+1,cnt-1,lst+[house[idx]])

    #공유기 설치하지 않는 경우
    back(idx+1,cnt,lst)

    
back(0,C,[])
print(max_d)