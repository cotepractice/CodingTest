#백준 #1946 신입사원
#정렬문제

#1. 시간초과
# import sys
# input = sys.stdin.readline
# T = int(input())

# for _ in range(T):
#     n = int(input())

#     score = [0 for _ in range(n)]

#     for i in range(n):
#         a, b = map(int, input().split())
#         score[i] = (a,b)
    
#     score.sort(key=lambda x:(-x[0],-x[1]))
#     print("score",score)
#     cnt = 0
#     for l in range(n-1):
#         second_score = score[l][1]
#         for m in range(l+1, n, 1):
#             if (second_score > score[m][1]):    #second_score까지 큰 경우(못 본 경우) break
#                 break
#             if (m==n-1):
#                 cnt += 1
#     cnt += 1   #마지막 수의 경우 무조건 통과
#     print(cnt) 

#2. 
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    n = int(input())

    score = [0 for _ in range(n)]

    for i in range(n):
        a, b = map(int, input().split())
        score[i] = (a,b)
    
    score.sort(key=lambda x:(x[0],x[1]))   #첫번째 원소,두번째 원소 오름차순
    
    highest_score = score[0][1]
    cnt = 0

    for k in range(1,n):
        my_second = score[k][1]
        #seconds에 존재하는 원소들과 비교
        if (my_second < highest_score):
            highest_score = my_second
            cnt += 1


    cnt += 1    #첫번째원소
    print(cnt)
