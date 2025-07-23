#1548 부분 삼각 수열
from itertools import combinations

N = int(input()) #최대 50
lst = list(map(int,input().split()))
lst.sort() #정렬해야 뒤 3중 for문에서 break 사용 가능
result = 2

def solv(solv_lst,k):
    #print("k",k)
    solv_lst.append(lst[k])
    combi = list(combinations(solv_lst,3))
    #print("combi",combi)
    for a,b,c in combi:
        if a+b<=c or a+c<=b or b+c<=a:
            return False

    return True

#N<3인 경우는 그냥 패스
if N<3:
    result = N
#N>=3인 경우 처리
else:
    #i,j,k는 인덱스 (0<=i,j,k<N)
    for i in range(N-2):
        for j in range(i+1,N-1):
            ans_lst = [lst[i],lst[j]]
            for k in range(j+1,N):
                if solv(ans_lst[:],k)==True:
                    ans_lst.append(lst[k])
                    result = max(result,len(ans_lst))
                else:
                    break

print(result)