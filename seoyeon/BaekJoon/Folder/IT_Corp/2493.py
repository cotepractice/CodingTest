#1. 시간복잡도 O(N*N). N:500,000 -> 사간초과
# N = int(input())

# tops = list(map(int,input().split()))
# answer = [0 for _ in range(N)]

# #i: 0->N-1
# for i in range(1,N):
#     #j: 1->i-1
#     for j in range(i-1,-1,-1):
#         if tops[i]<=tops[j]:
#             answer[i]=j+1
#             break

# print(*answer)

#2. stack 사용

N = int(input())
tops = list(map(int,input().split()))

answer = [0 for _ in range(N)]

stack = [] #for문 돌면서 현재 높이보다 작은 값은 pop()

for i in range(N):
    #stack 돌면서 현재 tops 높이와 비교
    while stack:
        #가장 마지막
        if stack[-1][1] > tops[i]:
            answer[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    #stack에 [현재index,현재높이] 삽입
    stack.append((i,tops[i]))

print(*answer)