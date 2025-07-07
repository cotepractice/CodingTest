#백준 #11659 구간 합 구하기4
#누적합 문제

#1. 시간초과
# import sys

# input = sys.stdin.readline

# n, m = map(int, input().split())

# # numbers = list(map(int, input().split()))
# numbers = list(int, input().split())

# for _ in range(m):
#     i, j = map(int, input().split())
#     sum = 0
#     for k in range(i-1, j):
#         sum += numbers[k]
#     print(sum)

#2
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

numbers = list(map(int, input().split()))

my_sum = 0  #누적합 계산. 해당 리스트는 0부터 해당 인덱스까지 더한 값
my_sum_lst = [0]    #my_sum_lst로 계산할 때 index가 0 일 때가 존재해야함   

#my_sum_lst 구하기
for k in range(n):
    my_sum += numbers[k]
    my_sum_lst.append(my_sum)

#i,j에 따라 원하는 값 출력
for l in range(m):
    i,j = map(int, input().split())
    print(my_sum_lst[j]-my_sum_lst[i-1])