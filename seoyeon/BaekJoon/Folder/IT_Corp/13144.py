#백준 #13144 List of Unique Numbers
#8:25-

#수열에서 연속한 1개 이상의 수를 뽑을 때 같은 수가 여러 번 등장하지 않는 경우의 수
#Two Pointer

# 1. List, Two Pointer -> 시간초과
# N = int(input())
# N_lst = list(map(int,input().split()))

# start,end=0,1 #start 포함, end 미포함
# current = [N_lst[start]]
# cnt=0

# #O(N^2)
# while start<end:
#     #print(cnt," ",current,start,end)
#     cnt+=1

#     #end가 인덱스 내에 존재하고, current에 존재하지 않으면 current 추가
#     if end<N and N_lst[end] not in current:
#         #print("here1")
#         current.append(N_lst[end])
#         end+=1

#     #end가 끝까지 갔거나 current에 존재하면 다음 start에서 시작
#     elif end==N or N_lst[end] in current:
#         #print("here2")
#         start+=1
#         end=start+1
#         if start<N:
#             current=[]
#             current.append(N_lst[start])
#         else:
#             break
        

# print(cnt)


#2. Set 사용
# N = int(input())
# N_lst = list(map(int,input().split()))

# start,end=0,1 #start 포함, end 미포함
# current = set() 
# current.add(N_lst[start])
# cnt=0

# while start<end:
#     #print(cnt," ",current,start,end)
#     cnt+=1

#     #end가 인덱스 내에 존재하고, current에 존재하지 않으면 current 추가
#     if end<N and N_lst[end] not in current:
#         #print("here1")
#         current.add(N_lst[end])
#         end+=1

#     #end가 끝까지 갔거나 current에 존재하면 다음 start에서 시작
#     elif end==N or N_lst[end] in current:
#         #print("here2")
#         start+=1
#         end=start+1
#         #다음 start가 범위 내 존재하면 진행, 그렇지 않은 경우 break
#         if start<N:
#             current=set()
#             current.add(N_lst[start])
#         else:
#             break
        

# print(cnt)

#3. Two Pointer
N = int(input())
N_lst = list(map(int,input().split()))

start,end=0,0 #start 포함, end 포함
current = set()
cnt=0

#원소 1개만 있어도 되기 때문에 start<=end 등호 필요
#start와 end가 변경되는데 N보다는 작아야 함
while start<=end<N:

    #end 이동
    #current에 N_lst 없으면 증가
    if end<N and N_lst[end] not in current:
        current.add(N_lst[end])
        end+=1
        cnt+=end-start #start는 아래에서 계산

    #start 이동
    #N_lst[end]와 동일한 N_lst[idx] 찾을 때까지 탐색
    #start를 증가시키며 current에서 N_lst[start]제거
    #N_lst[end]가 current에 존재하지 않으면 while문 빠져나옴
    else:
        while N_lst[end] in current:
            current.remove(N_lst[start])
            start+=1

print(cnt)