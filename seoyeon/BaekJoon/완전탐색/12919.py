#12919 A와 B2

# from collections import deque

# #1. Deque 사용
# # Dequee는 함수의 인자로 전달될 때 참조로 동작하기 때문에 solv1과 solv2 함수 내에서 pop(),reverse()할 때 원본 객체가 변경
# S = input()
# T = input()
# result = 0
# #가능한 연산
# #1. 문자열 뒤에 A 추가
# #2. 문자열 뒤에 B 추가 후 문자열 뒤집음

# #A 제거
# def solv1(Q):
#     Q.pop()
    
#     return Q

# def solv2(Q):
#     Q.reverse()
#     Q.pop()

#     return Q

# def ans(S,Q):
#     global result

#     answer = ""

#     while Q:
#         answer += Q.popleft()
#     print("answer",answer)
#     if S == answer:
#         print("WOW")
#         result = 1


# def dfs(S,Q):

#     if len(Q)==0:
#         return
#     if len(S)==len(Q):
#         ans(S,Q)
#         return
#     print("Q1",Q)
#     if Q[-1]=="A":
#         tmp2 = solv1(Q)
#         dfs(S,tmp2)
#     print("Q2",Q)
#     if Q[0]=="B":
#         tmp1 = solv2(Q)
#         dfs(S,tmp1)


# Q = deque()

# for t in T:
#     Q.append(t)

# dfs(S,Q)
# print(result)

#2. list
S = input()
T = input()

#T -> S
result = 0
def dfs(t):
    global result

    #종결조건
    if len(t)==len(S):
        if t==S:
            result = 1
        return 

    if t[0]=="B":
        dfs(t[1:][::-1]) #문자열 슬라이싱하는 경우, 원본 문자열은 변경되지 않고 새로운 문자열 객체 생성
    if t[-1]=="A":
        dfs(t[:-1])

dfs(T)
print(result)