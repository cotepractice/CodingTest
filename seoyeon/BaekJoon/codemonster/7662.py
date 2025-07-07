#11:47-12:12

# #[1] 시간초과
# #시간복잡도 O(T*k*N). T:테스트케이스개수, k:연산개수, N:dict개수
# from collections import defaultdict

# dict = defaultdict(int)

# T = int(input()) #테스트케이스 개수

# for _ in range(T):
#     k = int(input()) #연산 개수
    
#     for _ in range(k):
#         str, n = input().split(" ")

#         #str이 I -> n을 Q에 삽입
#         #str이 D 1 -> Q에서 최댓값 삭제, str이 D -1 -> Q에서 최솟값 삭제
#         #1)이때 삭제하는 값이 둘 이상 존재하는 경우 하나만 삭제
#         #2)Q가 비어있는데 D 연산하는 경우 무시
        
#         if str == "I":
#             if n in dict:
#                 dict[int(n)] += 1
#             else:
#                 dict[int(n)] = 1
#         else:
#             if len(dict)==0:
#                 continue
#             #최댓값 삭제
#             if n=="1":
#                 max_n = max(dict.keys())
#                 dict[max_n] -= 1
#                 if dict[max_n]==0:
#                     del dict[max_n]
#             #최솟값 삭제
#             else:
#                 min_n = min(dict.keys())
#                 dict[min_n] -= 1
#                 if dict[min_n]==0:
#                     del dict[min_n]

#     if len(dict)==0:
#         print("EMPTY")
#     else:
#         print(max(dict.keys()), min(dict.keys()))

#[2] 시간초과: min(),max() 대신 heapq 사용
#시간복잡도 O(T*k)
# from collections import defaultdict
# import heapq

# dict = defaultdict(int)

# T = int(input()) #테스트케이스 개수

# for _ in range(T):
#     k = int(input()) #연산 개수
#     Q = []
#     heapq.heapify(Q)
#     for _ in range(k):
#         str, n = input().split(" ")

#         #str이 I -> n을 Q에 삽입
#         #str이 D 1 -> Q에서 최댓값 삭제, str이 D -1 -> Q에서 최솟값 삭제
#         #1)이때 삭제하는 값이 둘 이상 존재하는 경우 하나만 삭제
#         #2)Q가 비어있는데 D 연산하는 경우 무시
        
#         if str == "I":
#             if n in dict:
#                 dict[int(n)] += 1
#             else:
#                 heapq.heappush(Q, int(n))
#                 dict[int(n)] = 1
#         else:
#             if len(dict)==0:
#                 continue
#             #최댓값 삭제
#             if n=="1":
#                 max_n = Q[-1]
#                 #max_n = max(dict.keys())
#                 dict[max_n] -= 1
#                 if dict[max_n]==0:
#                     del dict[max_n]
#                     del Q[-1]
#             #최솟값 삭제
#             else:
#                 min_n = Q[0]
#                 #min_n = min(dict.keys())
#                 dict[min_n] -= 1
#                 if dict[min_n]==0:
#                     del dict[min_n]
#                     del Q[0]

#     if len(dict)==0:
#         print("EMPTY")
#     else:
#         print(max(dict.keys()), min(dict.keys()))

#[3] 시간초과 sys.stdin.readline, max_heap, min_heap 분리
# #시간복잡도 O(T*k)
# import sys
# from collections import defaultdict
# import heapq

# input = sys.stdin.readline

# dict = defaultdict(int)

# T = int(input()) #테스트케이스 개수

# for _ in range(T):
#     k = int(input()) #연산 개수
#     max_heap = []
#     min_heap = []
#     heapq.heapify(max_heap)
#     heapq.heapify(min_heap)

#     for _ in range(k):
#         str, n = input().split()
#         n = int(n)

#         if str == "I":
#             heapq.heappush(max_heap, -n)
#             heapq.heappush(min_heap, n)
#             if n in dict:
#                 dict[n] += 1
#             else:
#                 dict[n] = 1
#         else:
#             if len(dict)==0:
#                 continue
#             #1)최댓값 삭제
#             if n==1:   
#                 #while문 => max_heap 돌면서 유효한 최댓값 탐색
#                 #min_heap에서 제거된 수가 있을 수 있음 -> dict에 존재하는지 확인
#                 #dict에 존재하고 개수가 0보다 크면서 가장 큰 수 탐색
#                 while max_heap:
#                     max_n = -heapq.heappop(max_heap)
#                     if max_n in dict: #dict에 없는 경우 이전 단계에서 사라진 수이므로 그 다음으로 큰 수 탐색
#                         dict[max_n]-=1
#                         if dict[max_n]==0:
#                             del dict[max_n]
#                         break
#             #2)최솟값 삭제
#             else:
#                 while min_heap:
#                     min_n = heapq.heappop(min_heap)
#                     if min_n in dict:
#                         dict[min_n]-=1
#                         if dict[min_n]==0:
#                             del dict[min_n]
#                         break
 
#     # #가장 작은 수
#     # while min_heap:
#     #     min_num=heapq.heappop(min_heap)
#     #     if min_num in dict and dict[min_num]>0:
#     #         break 
#     # #가장 큰 수
#     # while max_heap:
#     #     max_num=-heapq.heappop(max_heap)
#     #     if max_num in dict and dict[max_num]>0:
#     #         break 
#     while min_heap and dict[min_heap[0]]==0:
#         heapq.heappop(min_heap)
#     while max_heap and dict[-max_heap[0]]==0:
#         heapq.heappop(max_heap)

#     if not min_heap or not max_heap:
#         print("EMPTY")
#     else:
#         print(-max_heap[0], min_heap[0])

#[4] 정답 코드 -> 서칭. valid로 존재하는 원소 개수 카운트
# import sys
# import heapq
# from collections import defaultdict

# input = sys.stdin.readline

# T = int(input())
# for _ in range(T):
#     n = int(input())
#     min_queue = []
#     max_queue = []
#     heapq.heapify(min_queue)
#     heapq.heapify(max_queue)
#     del_list = defaultdict(int)
#     vaild = 0 # 남아있는 전체 원소 개수
#     for _ in range(n):
#         txt, num = input().rstrip().split()
#         num = int(num)
#         if txt == "I":
#             heapq.heappush(min_queue, num)
#             heapq.heappush(max_queue, -num)
#             if num in del_list:
#                 del_list[num] += 1 # 해당 번호를 방문해야함
#             else:
#                 del_list[num] = 1

#             vaild += 1 # 힙에 추가된 원소 수
#         elif txt == "D":
#             if num == -1:
#                 while min_queue:
#                     del_num = heapq.heappop(min_queue)
#                     if del_num in del_list:
#                         del_list[del_num] -= 1 # 해당 번호 방문 처리
#                         if del_list[del_num]==0:
#                             del del_list[del_num]
#                         vaild -= 1 # pop한 원소 빼기
#                         break

#             elif num == 1:
#                 while max_queue:
#                     del_num = -heapq.heappop(max_queue)
#                     if del_num in del_list:
#                         del_list[del_num] -= 1 # 해당 번호 방문처리
#                         if del_list[del_num]==0:
#                             del del_list[del_num]
#                         vaild -= 1 # pop한 원소 빼기
#                         break

#     if vaild > 0 : # 원소 수가 남아있다면
#         while True:
#             min_ = heapq.heappop(min_queue)
#             if min_ in del_list: # 힙 안에 남아있으면서 가장 작은 값
#                 break
#         while True:
#             max_ = -heapq.heappop(max_queue)
#             if max_ in del_list: # 힙 안에 남아있으면서 가장 큰 값
#                 break
#         print(max_, min_)
#     else:
#         print("EMPTY")

#[5] 직접 코딩
#시간복잡도 O(T*k*logN). logN:heapq.heappop()
import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

T = int(input()) #테스트케이스 개수

for _ in range(T):
    dict = defaultdict(int) #**dict가 테스트반복문 내에 존재해야 함
    k = int(input()) #연산 개수
    max_heap = []
    min_heap = []
    heapq.heapify(max_heap)
    heapq.heapify(min_heap)

    for _ in range(k):
        str, n = input().split()
        n = int(n)

        if str == "I":
            heapq.heappush(max_heap, -n)
            heapq.heappush(min_heap, n)
            if n in dict:
                dict[n] += 1
            else:
                dict[n] = 1
        else:
            if len(dict)==0:
                continue
            #1)최댓값 삭제
            if n==1:   
                #while문 => max_heap 돌면서 유효한 최댓값 탐색
                #min_heap에서 제거된 수가 있을 수 있음 -> dict에 존재하는지 확인
                #dict에 존재하는 가장 큰 수 탐색
                while max_heap:
                    max_n = -heapq.heappop(max_heap)
                    if max_n in dict: #dict에 없는 경우 이전 단계에서 사라진 수이므로 그 다음으로 큰 수 탐색
                        dict[max_n]-=1
                        if dict[max_n]==0:
                            del dict[max_n]
                        break
            #2)최솟값 삭제
            else:
                while min_heap:
                    min_n = heapq.heappop(min_heap)
                    if min_n in dict:
                        dict[min_n]-=1
                        if dict[min_n]==0:
                            del dict[min_n]
                        break

    if len(dict)!=0:
        while min_heap:
            min_num = heapq.heappop(min_heap)
            if min_num in dict:
                break
        while max_heap:
            max_num = -heapq.heappop(max_heap)
            if max_num in dict:
                break
        print(max_num, min_num)
    else:
        print("EMPTY")