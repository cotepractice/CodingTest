K,N = map(int,input().split())
lan_lst = [0 for _ in range(K)]

for k in range(K):
    lan_lst[k]=int(input())

#Two Pointer
start,end = 0,max(lan_lst) #mid는 가질 수 있는 최대 랜선의 길이
answer = 1

while start<=end:
    mid = (start+end)//2
    if mid==0:
        break

    cnt = 0 #가질 수 있는 최대 개수
    for lan in lan_lst:
        cnt += lan//mid
    
    if cnt>=N: #가질 수 있는 개수가 N보다 크거나 같은 경우 길이를 더 키워도 됨
        start = mid+1
        answer = max(answer,mid)
    else:
        end = mid-1

print(answer)