#백준 #1806 부분합

#1. Two Pointer -> 시간초과 발생
# N,S=map(int,input().split())
# N_lst=list(map(int,input().split()))

# start,end=0,0
# answer=float("inf")
# for idx,n in enumerate(N_lst):

#     #하나로 가능한 경우
#     if n>=S:
#         answer=min(answer,1)
#         break
#     #원소가 2개 이상인 경우
#     current=n
#     for next in range(idx+1,N):
#         current+=N_lst[next]
#         if current>=S:
#             answer=min(answer,next-idx+1)
#             continue

# if answer==float("inf"):
#     print(0)
# else:
#     print(answer)


#2. 누적합

N,S = map(int,input().split())
N_lst=list(map(int,input().split()))
dp = [0 for _ in range(N+1)]

#1) DP에 누적합 저장

for idx in range(1,N+1):
    dp[idx]=dp[idx-1]+N_lst[idx-1]
#print(dp)

#2) Two Poiner로 진행
answer=float("inf")

#합을 만드는 것이 힘든 경우
if dp[-1]<S:
    print(0)
#그 외의 경우 
else:
    start,end=1,1 #start,end 포함
    while start<=end:
        #print(start,end)

        #종결조건: dp는 dp[0]부터 dp[N]까지 존재하므로 N+1인 경우는 범위를 벗어남
        #이후는 start를 증가해도 S를 넘길 수 없으므로 종결
        if end==N+1: 
            break

        current=dp[end]-dp[start-1] #start를 포함해야 하므로 start-1
        #print(start,end)
        #print(current)

        #현재 start에서 S 이상을 탐색했으므로 start+1 탐색
        if current>=S:
            #print("here",start,end)
            answer=min(answer,end-start+1)
            start+=1
        elif current<S:
            end+=1

    print(answer)