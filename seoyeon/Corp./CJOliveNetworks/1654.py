#백준 #1654 랜선 자르기

#K: 1<=K<=10,000
#N: 1<=N<=1,000,000
#항상 K<=N
K, N = map(int,input().split())
len_lst = [0 for _ in range(K)]

for i in range(K):
    len_lst[i]=int(input())

#[출력] N개를 만들 수 있는 랜선의 최대 길이
#Two Pointer

start,end = 0, max(len_lst)
answer = 1 #+) 랜선을 만들 수 없는 경우는 없다고 가정했으므로 최소 answer=1로 설정
while start<=end:
    mid = (start+end)//2 #mid는 가질 수 있는 최대 랜선의 길이
    ans = 0

    if mid==0:
        break
    
    for length in len_lst:
        ans += length//mid
    
    if ans>=N:
        answer = max(answer,mid)
        start = mid+1
    else:
        end = mid-1

print(answer)