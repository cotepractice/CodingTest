#백준 #1806 부분합
#16:28-16:39

N, S = map(int,input().split())
lst = list(map(int,input().split()))

start,end=0,0 #start,end 포함
s=lst[start]  #초기값
l=float("inf") #길이

#start와 end가 같아도 됨 -> 숫자 하나가 S 이상인 경우
while start<=end:
    
    #1. S 이상인 경우
    # 길이 l 업데이트, start 제거(가장 짧은 것의 길이를 구하기 위해)
    if s>=S:
        l=min(l, end-start+1)
        s-=lst[start]
        start+=1
    #2. S 미만인 경우
    # end 1 추가(값을 더 추가해야 함)
    # 이때 end가 N인 경우 모두 탐색한 것
    else:
        end+=1
        #종결조건
        if end==N:
            break
        else:
            s+=lst[end]

if l==float("inf"):
    print(0)
else:
    print(l)