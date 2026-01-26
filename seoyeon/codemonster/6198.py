#백준 #6198 옥상 정원 꾸미기
#22:15-

#1. 시간초과
# from collections import deque
# import sys

# input = sys.stdin.readline

# N = int(input())
# h_lst = [0 for _ in range(N)]

# for n in range(N):
#     h_lst[n]=int(input())

# ans = []
# for i in range(N-1,-1,-1):
#     #print("i",i)
#     Q=deque(h_lst[i:])
#     #print('q',Q)
#     current = h_lst[i-1] #현재 건물 옥상
#     max_h = h_lst[i-1] #앞의 건물 중 가장 큰 건물
    
#     res = []

#     #오른쪽에서부터 탐색
#     #조건: 현재 옥상보다 작아야 함. 앞의 건물보다 작아야 함
#     while Q:

#         x=Q.popleft()
#         #print('x',x)
#         #현재 건물보다 작아야 옥상 볼 수 있음
#         #앞 건물보다 커야 함
#         if x<current:
#             if res and x>res[-1]:
#                 res.append(x)
#             else:
#                 res.append(x)
#         #앞 건물 중 하나라도 현재 건물보다 큰 경우 종결
#         else:
#             break
        

#     #print('res',res)
#     ans.append(len(res))

# print(sum(ans))

#2. stack

from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
h_lst = [0 for _ in range(N)]

for n in range(N):
    h_lst[n]=int(input())

stack = deque() 
answer = 0

#본인을 볼 수 있는 관리인의 수 구하기
#stack 안의 빌딩 중 자신을 볼 수 있는 빌딩 관리인 수 탐색
for cur in h_lst:
    #stack이 존재하고 현재 값보다 작은 경우, stack에서 값 제거
    #뒤에서 볼 때 현재 높이인 cur에 가려지므로 뒤 신경쓰지 않고 제거해도 됨
    while stack and stack[-1]<=cur:
        stack.pop()
    #남은 stack은 cur을 볼 수 있는 빌딩 관리인 리스트 의미
    answer += len(stack)
    #현재 높이 cur 추가
    stack.append(cur)

print(answer)