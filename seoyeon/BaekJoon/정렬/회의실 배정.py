#백준 #1931
#정렬 문제
#회의실 배정
#피드백: 1. (a,b)일 때 두 개의 원소로 동시에 sort할 수 있는줄 몰랐음
#2. (1)의 이유로 재귀함수로 사용했으나 시간초과 발생. 원소 두개로 정렬 후 원하는 값 계산

#1. 메모리 초과
# import sys
# from collections import deque

# input = sys.stdin.readline

# N = int(input())

# lst = []

# for i in range(N):
#     a, b = map(int, input().split())

#     lst.append((a,b))

# #end 오름차순 정렬 후 첫번째 index 선택 -> 선택한 end 이후의 start와 end만 남겨두고 반복
# def sortAndRemove(lst,cnt):
#     tmp_lst = []

#     lst.sort(key=lambda x:x[1]) #2번째 원소로 오름차순 정렬
#     tmp = lst[0][1] #끝나는 시간
#     del lst[0]
#     cnt += 1
    
#     for i in range(len(lst)):
#         if (lst[i][0] >= tmp):
#             tmp_lst.append(lst[i])
#     if (len(tmp_lst) == 1):
#         cnt += 1
#         return cnt
#     elif (len(tmp_lst) == 0):
#         return cnt
#     return sortAndRemove(tmp_lst, cnt)  #sortAndRemove(tmp_lst,cnt)로 해도 될 줄 알았는데 return으로 써야함. 그렇지 않은 경우 len(lst) == 0이 아니면 아무것도 리턴하지 않음. 재귀함수 사용시 반드시 자기자신 리턴해야함! 정답만 리턴X

# cnt = 0
# print(sortAndRemove(lst,cnt))

#2. 시간 초과
# import sys

# input = sys.stdin.readline

# N = int(input())

# lst = []

# for i in range(N):
#     a, b = map(int, input().split())

#     lst.append((a,b))

# #end 오름차순 정렬 후 첫번째 index 선택 -> 선택한 end 이후의 start와 end만 남겨두고 반복
# def sortAndRemove(lst,cnt):
#     tmp_lst = [(2**31-1,2**31-1) for _ in range(N)]

#     lst.sort(key=lambda x:x[1]) #2번째 원소로 오름차순 정렬
#     tmp = lst[0][1] #끝나는 시간
#     del lst[0]
#     cnt += 1
#     tmp_n = 0
    
#     for i in range(len(lst)):
#         if (lst[i][0] >= tmp):
#             tmp_lst[tmp_n] = lst[i]
#             tmp_n += 1
#     if (tmp_lst[0][0] == 2**31-1):
#         return cnt
#     if (tmp_lst[1][0] == 2**31-1):
#         cnt += 1
#         return cnt
#     return sortAndRemove(tmp_lst, cnt)  #sortAndRemove(tmp_lst,cnt)로 해도 될 줄 알았는데 return으로 써야함. 그렇지 않은 경우 len(lst) == 0이 아니면 아무것도 리턴하지 않음. 재귀함수 사용시 반드시 자기자신 리턴해야함! 정답만 리턴X

# cnt = 0
# print(sortAndRemove(lst,cnt))

#3. 
import sys

input = sys.stdin.readline

N = int(input())

lst = []

for i in range(N):
    a, b = map(int, input().split())

    lst.append((a,b))

#sort: 2번째 원소 오름차순 정렬 후 1번째 원소 오름차순 정렬
#끝나는 시간 오름차순 -> 끝나는 시간이 같은 경우 늦게 시작하는 경우가 최적의 경우
lst.sort(key=lambda x:(x[1],x[0]))
tmp = lst[0][1] #끝나는 시간
cnt = 1

for i in range(1,N):
    if (lst[i][0] >= tmp):  #위에서 정렬한 lst이므로 (0,len(lst)-1)까지 차례대로 비교. 시작시간이 이전에 끝난시간보다 큰 경우 카운트
        tmp = lst[i][1]
        cnt += 1

print(cnt)
