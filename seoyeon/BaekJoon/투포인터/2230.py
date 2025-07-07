#백준 #2230 수 고르기
#투포인터

#1. 시간초과
# answer = float("inf")
# def two_pointer(m):
#     global answer
#     start,end = 0,1

#     while True:
#         #print(start,end)
#         if abs(lst[start]-lst[end])>=m:
#             answer = min(answer,abs(lst[start]-lst[end]))

#         if end+1==N:
#             #print("1")
#             start += 1
#             end = start+1
#         else:
#             #print("2")
#             end += 1
        
#         if start==N-1:
#             return

# N, M = map(int,input().split())
# lst = []

# for i in range(N):
#     lst.append(int(input()))

# two_pointer(M)
# print(answer)

# 2.수열임을 인지
#시간복잡도 O(A[i] 개수)
# answer = float("inf")
# def two_pointer(m):
#     global answer
#     start,end = 0,1

#     while end<N:
#         #print(start,end)
#         #start==end인 경우 0이므로 자동으로 else로 이동
#         #조건1. m보다 커야 함
#         if lst[end]-lst[start]>=m:
#             #더 작은 값이 있는지 확인 -> start+=1
#             #조건2. answer보다 작아야 함
#             if lst[end]-lst[start]<answer:
#                 answer = lst[end]-lst[start]
#                 start+=1
#         #차이가 m보다 크지 않은 경우 차이를 벌려야 함
#         else:
#             end += 1

#3. 정답코드
import sys
input = sys.stdin.readline

def two_pointer(N,M,lst):
    answer = float("inf")
    start,end = 0,0
    while end<N:
        #lst[end]-lst[start]가 m보다 큰 첫 인덱스만 찾고 다음 start로 넘어감
        if lst[end]-lst[start]>M:
            answer = min(lst[end]-lst[start], answer)
            start += 1
        elif lst[end]-lst[start]<M:
            end+=1
        else:
            return M
    return answer

N, M = map(int,input().split())

lst = []

for i in range(N):
    lst.append(int(input()))
#lst 오름차순 정렬
lst.sort()

answer = two_pointer(N,M,lst)

print(answer)