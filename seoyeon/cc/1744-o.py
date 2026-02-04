#백준 #1744 수 묶기

N = int(input())
left = []
right = []

for _ in range(N):
    n=int(input())
    if n<=0: #0이 left에 있는게 더 유리
        left.append(n)
    else:
        right.append(n)

left.sort()
right.sort(reverse=True)

ans = 0

l_idx=0
r_idx=0

#음수 계산
for l_idx in range(0,len(left),2):
    if l_idx+1<len(left):
        ans += left[l_idx]*left[l_idx+1]
    else:
        ans += left[l_idx]

#양수 계산
for r_idx in range(0,len(right),2):
    if r_idx+1<len(right):
        #1인 경우는 더하기
        if right[r_idx+1]==1:
            ans += right[r_idx]+right[r_idx+1]
        else:
            ans += right[r_idx]*right[r_idx+1]
    else:
        ans += right[r_idx]
print(ans)