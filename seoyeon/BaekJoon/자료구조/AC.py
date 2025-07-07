#백준5430 AC
#자료구조

# #1
# import sys
# from collections import deque

# input = sys.stdin.readline
# T = int(input())

# for _ in range(T):
#     func = input()
#     n = int(input())
#     n_deque = deque()
#     #n_deque 생성
#     lst = input()

#     for i in range(2*n+1):
#         if (i%2!=0):
#             n_deque.append(int(lst[i]))

#     #func 확인
#     result = []
#     for k in range(len(func)):
#         if (func[k] == "R"):
#             n_deque.reverse()
#         if (func[k] == "D" and len(n_deque) == 0):
#             print("error")
#             continue
#         if (func[k] == "D"):
#             n_deque.popleft()
#         if (k == len(func)-1):
#             for j in range(len(n_deque)):
#                 result.append(n_deque[j])
#             print(result)

#2            
import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    func = input()
    n = int(input())    
    arr = input().strip()       #strip으로 공백이 없이 입력받기
    n_queue = deque(arr[1:-1].split(','))   #[]까지 받기에 [와 ]를 제거한 arr[1:-1] 받고. ','으로 수 분리
    if (n == 0):    #n = 0일때에도 위와 같이 하면 deque([""])로 len(n_queue)가 1이 됨
        n_queue = deque()   
    
    n_reverse = 0   #뒤집어지는 경우 카운트해서 마지막에 한 번에 뒤집기. 시간초과해결
    flag = 0    #flag == 1인 경우 n_queue 출력x

    for i in range(len(func)):
        if (func[i] == "D" and len(n_queue) == 0):
            print("error")
            flag = 1
            break
        if (func[i] == "D"):
            #뒤집어지는 횟수에 따라 왼쪽 또는 오른쪽 수 삭제
            if (n_reverse%2==0):
                n_queue.popleft()
            else:
                n_queue.pop()
        if (func[i] == "R"):
            n_reverse += 1

    if (flag == 1):
        continue
    else:
        if (n_reverse % 2 != 0):
            n_queue.reverse()
        print("["+ ",".join(n_queue)+"]") #리스트를 문자열로 변환해 출력