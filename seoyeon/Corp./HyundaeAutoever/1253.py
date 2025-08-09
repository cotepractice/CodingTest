# #1253 좋다
# #21:17-

# #1. 누적합 -> 65% 틀렸습니다.
# N = int(input())
# n_lst = list(map(int,input().split()))

# boards = [[-1 for _ in range(N)] for _ in range(N)]
# #boards
# # [1,-1,-1,-1,...]
# # [1,2,-1,-1,...]
# # [1,2,3,-1,-1,...]

# n_dict = dict()

# for i in range(N):
#     #boards[0]인 경우
#     if i==0:
#         boards[i][0]=n_lst[i]
#         continue
#     #boards[k]. k>0인 경우
#     boards[i] = boards[i-1][:] #이전까지 동일
#     boards[i][i] = n_lst[i]
#     #두 수의 합
#     for j in range(0,i): #boards[i]의 0~i-1까지 돌면서 두 개의 합 dict에 넣기
#         sum = boards[i][j]+n_lst[i]
#         if sum not in n_dict:
#             n_dict[sum]=0

# # for l in range(N):
# #     print(boards[l])
# # print("n_dict",n_dict)

# #N개의 수 확인
# answer = 0
# for n in n_lst:
#     if n in n_dict:
#         answer += 1
# print(answer)


#2. 누적합 

N = int(input())
n_lst = list(map(int,input().split()))
n_lst.sort()

answer = 0

for i in range(N):
    target = n_lst[i]
    #두 수에 본인이 들어가면 안 됨
    temp = n_lst[:i]+n_lst[i+1:] 
    start, end = 0,len(temp)-1

    while start<end:
        
        if temp[start]+temp[end]==target:
            answer+=1
            break

        elif temp[start]+temp[end]<target:
            start += 1
        elif temp[start]+temp[end]>target:
            end -= 1

print(answer)