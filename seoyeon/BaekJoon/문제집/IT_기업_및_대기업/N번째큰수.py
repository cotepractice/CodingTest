#백준 2075 N번째 큰 수

# #1. 메모리 초과 오류 발생
# N = int(input()) #N번째 큰 수
# lst = [[0 for _ in range(N)] for _ in range(N)]

# for i in range(N):
#     lst[i] = list(map(int, input().split()))

# dict_lst = [-1 for _ in range(N)]
# col = [(N-1) for _ in range(N)] #index

# for i in range(N):
#     last =  lst[N-1][i] #맨 뒤 숫자
#     dict_lst[i] = last

# #아래 반복
# #1. dict_lst에서 가장 큰 수 찾기
# #2. 해당 수 위에 존재하는 수로 dict_lst 업데이트

# cnt = 0
# while True:
#     cnt += 1
#     max_n = max(dict_lst)
#     for i in range(N):
#         if dict_lst[i]==max_n:
#             col[i] -= 1
#             dict_lst[i] = lst[col[i]][i]
#     if cnt == N:
#         print(max_n)
#         break

#2. heapq 사용해 메모리 줄임
import heapq

N = int(input())
heap = [] #heap은 오름차순으로 정렬됨

init_numbers = list(map(int, input().split()))
for num in init_numbers:
    heapq.heappush(heap, num) #init_numbers를 heap에 넣음

for i in range(N-1):
    numbers = list(map(int, input().split()))

    for num in numbers: #모든 수를 넣으면서 heap 내의 가장 작은 수인 heap[0]보다 큰 경우 heap에 들어감
        if heap[0] < num:
            heapq.heappush(heap,num) #heap[0]보다 큰 수 삽입
            heapq.heappop(heap) #가장 작은 수 삭제

print(heap[0])