#백준 #2230 수 고르기

# #1. 틀렸습니다 -> Two Pointer 아님
# N,M=map(int,input().split())
# N_lst=[0 for _ in range(N)]

# for i in range(N):
#     N_lst[i]=int(input())

# result=float("inf")

# start,end=0,1 #start 포함,end 포함

# while start<end:
#     #종결조건
#     if start==N:
#         break

#     diff=abs(N_lst[start]-N_lst[end])
#     if diff>=M and diff<result:
#         result=diff
    
#     start+=1

# print(result)

#2. Two Pointer
import sys
input = sys.stdin.readline

N,M=map(int,input().split())
N_lst=[0 for _ in range(N)]

for i in range(N):
    N_lst[i]=int(input())

N_lst.sort() #Two Pointer는 반드시 정렬 필요

start,end=0,1 #start,end 둘 다 포함
result=float("inf")

#while start<end<N으로 하는 경우 틀렸습니다 발생
#루프 조건에 강제하면 탐색이 조기에 끝남
while end<N:
    #M보다 작은 경우 큰 수(N_lst[end])를 더 크게 해야 함
    if N_lst[end]-N_lst[start]<M:
        end+=1
    #M보다 큰 경우 그 차이를 줄여야 하므로 start+1
    elif N_lst[end]-N_lst[start]>M:
        result=min(result,N_lst[end]-N_lst[start])
        start+=1
    #정확히 M인 경우 종결
    else:
        result=M
        break

print(result)