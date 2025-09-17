#백준 #12891 DNA 비밀번호
#14:54 - 15:08


# #1. 시간초과
# from collections import defaultdict

# words_lst = ['A','C','G','T']

# words_dict = dict()

# for w in words_lst:
#     words_dict[w]=0

# #1. 부분문자열 뽑기. 부분문자열 길이 P가 주어짐
# #2. 부분문자열의 문자 개수가 특정 개수 이상이어야 함. (A,C,G,T)
# #부분문자열이 등장하는 위치가 다르면 부분문자열이 같아도 다른 문자열로 취급
# #출력: 만들 수 있는 비밀번호의 수

# S, P = map(int,input().split()) #S:DNA 문자열 길이,P:부분문자열 길이
# DNA = list(input())
# minimum_n = list(map(int,input().split())) #[A,C,G,T] 최소 길이 
# answer = 0

# for i in range(S-P+1):

#     part = DNA[i:i+P] #슬라이싱

#     part_d = defaultdict(int)

#     #부분문자열의 개수 카운트
#     for p in part:
#         if p in part_d:
#             part_d[p] += 1
#         else:
#             part_d[p] = 1

#     #개수 비교
#     for i in range(4):
#         if part_d[words_lst[i]]<minimum_n[i]:
#             continue

#         if i==3:
#             answer += 1


# print(answer)


#2.성공
from collections import defaultdict

words_lst = ['A','C','G','T']

words_dict = dict()

for w in words_lst:
    words_dict[w]=0

#1. 부분문자열 뽑기. 부분문자열 길이 P가 주어짐
#2. 부분문자열의 문자 개수가 특정 개수 이상이어야 함. (A,C,G,T)
#부분문자열이 등장하는 위치가 다르면 부분문자열이 같아도 다른 문자열로 취급
#출력: 만들 수 있는 비밀번호의 수

S, P = map(int,input().split()) #S:DNA 문자열 길이,P:부분문자열 길이
DNA = list(input())
minimum_n = list(map(int,input().split())) #[A,C,G,T] 최소 길이 
part_d = defaultdict(int) #부분문자열에 존재하는 문자열
answer = 0

#처음 
for i in range(P):
    if DNA[i] in part_d:
        part_d[DNA[i]]+=1
    else:
        part_d[DNA[i]]=1

for i in range(4):
    if part_d[words_lst[i]] < minimum_n[i]:
        break

    if i==3:
        answer += 1

for i in range(1,S-P+1):
    #이전 단어 제거
    part_d[DNA[i-1]] -= 1 #이전 단어 제거
    #추가된 단어 추가
    if DNA[i+P-1] in part_d:
        part_d[DNA[i+P-1]] += 1
    else:
        part_d[DNA[i+P-1]] = 1

    #비교
    for i in range(4):
        if part_d[words_lst[i]] < minimum_n[i]:
            break

        if i==3:
            answer += 1


print(answer)