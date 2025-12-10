#백준 #1744 수 묶기

#수열의 합 구하기
#1. 그냥 더하기
#2. 두 수를 묶으면 서로 곱한 후 더하기
# 모든 수는 단 한 번만 묶거나 묶지 않아야 함

#1. 테케 모두 성공
N = int(input())
lst = [0 for _ in range(N)]

for i in range(N):
    lst[i]=int(input())

lst.sort()

#뒤에서부터 진행
visited=set()
ans=0
for idx in range(N-1,-1,-1):
    #print("idx",idx)
    #1.이미 묶인 경우
    if idx in visited:
        #print("here1",ans)
        continue
    #종결조건: 마지막 인덱스인 경우 진행 X
    if idx==0:
        ans+=lst[idx]
        break

    #2.묶을지 말지 결정
    val=lst[idx]*lst[idx-1]
    #print("VAL:",val)
    
    #곱할 때 0인 경우
    # 1) 나머지 값이 음수이면 0이 최댓값. ans 업데이트
    # 2) 나머지 값이 양수이면 
    if val==0:
        if lst[idx]<0 or lst[idx-1]<0:
            ans+=val
            visited.add(idx)
            visited.add(idx-1)
        else:
            if lst[idx]!=0:
                ans+=lst[idx]
            
    #음수인 경우 또는 합이 더 큰 경우, 묶지않음
    elif val<0 or val<lst[idx]+lst[idx-1]: 
        ans+=lst[idx]
        #print("here2",ans)
        continue
    #양수인 경우, 묶음 => lst를 정렬했으므로 최댓값 보장
    elif val>0:
        visited.add(idx)
        visited.add(idx-1)
        ans+=val
        #print("here3",ans)
    #print("ans",ans)

print(ans)
