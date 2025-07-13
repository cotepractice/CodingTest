#1. 시간복잡도 O(N*N). N:500,000 -> 사간초과
N = int(input())

tops = list(map(int,input().split()))
answer = [0 for _ in range(N)]

#i: 0->N-1
for i in range(1,N):
    #j: 1->i-1
    for j in range(i-1,-1,-1):
        if tops[i]<=tops[j]:
            answer[i]=j+1
            break

print(*answer)
