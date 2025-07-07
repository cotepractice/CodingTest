#백준 #2839 설탕 배달

N = int(input())

rotate = N//5
ans = 0
for k in range(rotate,-1,-1):
    cur_N = N - 5*k
    
    if cur_N % 3 == 0:
        ans = k + cur_N//3
        break
    
if ans == 0:
    print(-1)
else:
    print(ans)