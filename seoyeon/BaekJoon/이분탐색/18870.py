#백준 #18870 좌표압축

N = int(input())
N_lst = list(map(int,input().split()))
tmp_lst = N_lst
tmp_set = list(set(tmp_lst))
tmp_set.sort()

#end 탐색
def binary(target,start,end):
    mid = (start+end)//2
    
    if start>end:
        return 0
    if tmp_set[mid]==target:
        return mid
    if tmp_set[mid]>target:
        return binary(target,start,mid-1)
    elif tmp_set[mid]<target:
        return binary(target,mid+1,end)

answer = []
for n in N_lst:
    answer.append(binary(n,0,len(tmp_set)-1))
print(*answer)