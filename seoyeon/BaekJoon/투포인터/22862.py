#백준 #22862 가장 긴 짝수 연속한 부분 수열(large)

#9:16-10:08

N,K = map(int,input().split())
S = list(map(int,input().split()))
answer = 0

#1. Backtracking, Two Pointer -> Recursion Error
# #start포함, end 미포함
# def backtracking(start,end,k,lst):
#     global answer

#     #종결조건1
#     if end==N:
#         answer=max(answer,len(lst))
#         return
    
#     #종결조건2
#     if S[end]%2==1 and k==K:
#         answer=max(answer,len(lst))
#         return
    
#     #짝수인 경우
#     if S[end]%2==0:
#         backtracking(start,end+1,k,lst+[S[end]])
#     #홀수인 경우
#     else:
#         backtracking(start,end+1,k+1,lst)

# for i in range(N):
#     if i%2==0:
#         backtracking(i,i,0,[i])

# print(answer)

#2.Two Pointer

start,end=0,1 #start 포함, end 미포함
if S[start]%2==0:
    k=0
else:
    k=1

#end는 포함되지 않으므로 범위가 N+1 미만
while end<N+1:
    
    answer=max(answer,end-start-k)
    #print(answer,start,end,k)

    #종결조건
    if end>=N:
        break

    #짝수인 경우
    if S[end]%2==0:
        end+=1
    
    #홀수인 경우
    #더 넣을 수 있는 경우와 없는 경우
    elif S[end]%2==1:
        #1.더 넣을 수 있는 경우
        if k<K:
            k+=1
        #2.더 넣을 수 없는 경우
        # start 값이 홀수면 start 1 증가, 짝수면 홀수를 한 번 지나쳐야 함
        else:
            #start 값이 홀수인 경우 start 1 증가
            if S[start]%2==1:
                start+=1
            #start 값이 짝수인 경우 홀수 찾기
            else:
                #홀수 찾기. 현재 값을 넣기 위해 
                while True:
                    if S[start]%2==1:
                        break
                    start+=1
                start+=1 #홀수 지나야 함
        end+=1

print(answer)