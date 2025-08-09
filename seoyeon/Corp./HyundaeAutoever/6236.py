#통장에서 뺀 돈으로 하루 살 수 있으면 그대로 사용하고, 모자르면 남은 금액 넣고 다시 K원 출금
#[?] 정확히 M번을 맞추기 위해 남은 금액이 그날 사용할 금액보다 많더라도 남은 금액은 통장에 넣고 다시 K원 인출 가능

N,M = map(int,input().split()) #N:N일동안사용,M:돈빼는횟수

n_lst = [-1 for _ in range(N)] #i번째 날에 이용할 금액

for n in range(N):
    k = int(input())
    n_lst[n]=k

start, end = max(n_lst), sum(n_lst) #이용할 금액. n_lst보다는 커야 함. [TIP]최대값은 n_lst를 한 번에 사용할만큼의 돈

while start<=end:
    mid = (start+end)//2 #K
    
    current = mid #남은 금액
    m = 1 #출금한 횟수
    for n in n_lst:
        #출금안해도되는경우
        if n<=current:
            current-=n
        #출금해야하는경우
        else:
            current = mid
            m += 1
            current -= n

    #출금한 횟수가 많으면 K 키워야 함
    if m>M:
        start=mid+1
    #출금한 횟수가 적으면 K를 더 줄여도 됨
    else:
        end=mid-1
    
print(mid)