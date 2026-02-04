#백준 3151 합이 0

#세 팀원의 코딩 실력의 합이 0이 되는 팀
#대회에 출전할 수 있는 경우의 수
from collections import defaultdict

N = int(input())
lst = list(map(int,input().split()))

lst.sort()

#정렬
#하나씩 탐색
#이분탐색

#current가 가장 작은 수
answer=0

for idx,current in enumerate(lst):
    
    left=idx+1
    right=len(lst)-1
    
    while left<right:
        sum=current+lst[left]+lst[right]

        #sum==0인 경우 중복 처리 핵심
        if sum==0:
            if lst[left]==lst[right]: 
                answer+=(right-left+1) * (right-left) //2
                break
            else:
                l_val = lst[left]
                l_cnt = 1
                while left + l_cnt < right and lst[left + l_cnt] == l_val:
                    l_cnt += 1

                r_val = lst[right]
                r_cnt = 1
                while right - r_cnt > left and lst[right - r_cnt] == r_val:
                    r_cnt += 1
                answer+=l_cnt*r_cnt
                left+=l_cnt
                right-=r_cnt
        elif sum<0:
            left+=1
        else:
            right-=1
        
print(answer)