#백준 #22866 탑보기
#17:16-

#출력: i번째에서 볼 수 있는 건물 개수, 그중 가장 가까우면서 작은 번호 
#현재 건물 높이가 L인 경우 높이가 L보다 큰 곳의 건물만 볼 수 있음

# #1. 시간복잡도 O(N**2) -> 시간초과 발생
# N = int(input())
# n_lst = list(map(int,input().split()))

# #1. Two Pointer로 진행
# #2. (현재 인덱스) for문으로 하나 고정하고, 뒤로 가면서 탐색
# #2-1. 가장 큰 값 max_n 설정. 초기값은 현재 높이
# #2-2. 뒤로 갈 수록 max_n보다 큰 경우 존재하면 현재 인덱스 리스트에 추가
# #3. (뒤 인덱스) 뒤에 해당하는 경우
# #3-1. 다음 인덱스가 max_n보다 큰 경우 리스트 비우고 해당 인덱스 리스트에 추가
# #3-2. 다음 인덱스가 본인 높이보다 크면서 max_n보다 작은 경우 해당 인덱스 리스트에 추가

# possible = [[] for _ in range(N)]

# for i in range(N):
#     max_n = n_lst[i] #최대 높이
#     current = n_lst[i] #현재 높이

#     #현재 건물 왼쪽: 현재부터 시작해 왼쪽으로 이동
#     for j in range(i,-1,-1):
#         next = n_lst[j]
#         if next>max_n:
#             possible[i].append(j)
#             max_n=next

#     max_n = n_lst[i] #최대 높이
#     #현재 건물 오른쪽: 현재부터 시작해 오른쪽으로 이동
#     for j in range(i+1,N):
#         next = n_lst[j]
#         #i 처리: max_n보다 큰 경우
#         if next>max_n:
#             possible[i].append(j)
#             max_n=next
    

# def calc(idx,lst):
#     diff = float("inf")
#     res = -1
#     for l in lst:
#         if abs(l-idx)<diff:
#             diff=abs(l-idx)
#             res=l
#     return res+1

# answer = []
# for idx,p in enumerate(possible):
#     ans = len(p)
#     if ans==0:
#         answer.append([ans])
#     else:
#         answer.append([ans, calc(idx,p)])

# for i in range(len(answer)):
#     print(*answer[i])


#2. 시간복잡도 O(N**2). 89% 시간초과
import heapq

N = int(input())
n_lst = list(map(int,input().split()))

heap = []
for idx, val in enumerate(n_lst):
    heap.append([-val,idx])

heapq.heapify(heap)

visited = set()

res = [set() for _ in range(N)]

while heap:
    val, idx = heapq.heappop(heap)
    val = -val
    
    visited.add(idx)
    
    #왼쪽 계속 탐색
    #같은 높이 존재할 수 있음
    left=idx-1
    while True:
        if left in visited or left<0 or n_lst[left]==val:
            break
        res[left].add(idx)
        left -= 1

    #오른쪽 계속 탐색
    right=idx+1
    while True:
        if right in visited or right>=N or n_lst[right]==val:
            break
        res[right].add(idx)
        right+=1

def calc(idx,lst):
    diff=float("inf")
    diff_ans=-1
    for l in lst:
        if abs(idx-l)<diff:
            diff_ans=l
            diff=abs(idx-l)
        elif abs(idx-l)==diff:
            diff_ans=min(diff_ans,l)
    return diff_ans+1

answer = []
for idx,r in enumerate(res):

    if len(r)==0:
        answer.append([len(r)])
    else:
        closest = calc(idx,r)
        answer.append([len(r), closest])

for k in range(N):
    print(*answer[k])