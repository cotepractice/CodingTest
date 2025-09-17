#백준 #9935 문자열 폭발

#폭발 문자열이 폭발하면, 그 문자는 문자열에서 사라지며 남은 문자열은 합쳐짐
#1. 문자열이 폭발 문자열을 포함하고 있는 경우, 모든 폭발 문자열 폭발. 
# 남은 문자열은 순서대로 이어 붙여 새로운 문자열 생성
#2. 새로 생긴 문자열에 폭발 문자열이 포함되어 있을 수도 있음
#3. 폭발은 폭발 문자열이 문자열에 없을 때까지 계속됨

#출력: 모든 폭발이 끝난 후 남는 문자열. 남아 있는 문자열이 없는 경우 FRULA 출력
from collections import deque

sentences = input()
bomb = list(input())

Q = deque(sentences)

Q = []
for x in sentences:
    Q.append(x)
    #슬라이싱 시간 복잡도 O(리스트내원소개수) -> Q[a:b]는 O(b-a)
    if Q[len(Q)-len(bomb):len(Q)]==bomb:
        for _ in range(len(bomb)):
            Q.pop()

if len(Q)==0:
    print("FRULA")
else:
    print(*Q,sep="")



# # #구현 => 시간 초과 발생
# while True:
    
#     sentence = []
#     check = deque()
#     idx = 0
#     cnt = 0

#     while Q:
        
#         x = Q.popleft()
        
#         #1. x와 bomb[idx] 일치하지 않는 경우, check 초기화
#         if idx!=0 and x!=bomb[idx]:
            
#             idx = 0
#             while check:
#                 y = check.popleft()
#                 sentence.append(y)

#         #1. 일치하는 경우
#         # 시작 인덱스 0부터 하나씩 증가하고 값이 같으면 lst와 idx 추가
#         if x==bomb[idx]:
#             check.append(x)
#             idx += 1

#             # idx와 bomb길이-1이 같은 경우는 lst에 값이 정확히 일치한 경우
#             # 다음에 나올 폭발 문자열 탐색
#             if idx==len(bomb):
#                 check = deque()
#                 idx = 0
#                 cnt += 1

#         else:
#             sentence.append(x)

    
#     if cnt==0:
#         if len(sentence)==0:
#             print("FRULA")
#         else:
#             print(*sentence,sep="")
#         break
    
#     Q = deque(sentence)