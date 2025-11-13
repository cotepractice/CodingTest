#백준 #2179 비슷한 단어

# #1. 시간초과. O(N^2 * 100)
# N = int(input())
# n_lst = [[] for _ in range(N)]

# for n in range(N):
#     n_lst[n]=list(input())


# answer=[0,"",""]

# for i in range(N-1):
#     for j in range(i+1,N):
#         length=min(len(n_lst[i]),len(n_lst[j]))
#         idx=0

#         while idx<length:
#             if n_lst[i][idx]!=n_lst[j][idx]:
#                 break
#             idx+=1
#         if idx>answer[0]:
#             answer=[idx,n_lst[i],n_lst[j]]

# print(*answer[1],sep="")
# print(*answer[2],sep="")

#2. 
N = int(input())
n_lst = [[] for _ in range(N)]

for n in range(N):
    n_lst[n]=list(input())

#사전순으로 정렬
n_sorted = sorted(list(enumerate(n_lst)), key=lambda x:x[1])

#x와 y가 겹치는 횟수 cnt 반환
def check(x,y):
    cnt=0
    for idx in range(min(len(x),len(y))):
        if x[idx]==y[idx]:
            cnt+=1
        else:
            break
        
    return cnt

max_n=0
length=[0]*(N+1)
answer=[[],[]]

#i와 i+1 비교
for i in range(N-1):
    #common_n: n_sorted[i][1]과 n_sorted[i+1][1]의 겹치는 접두사 개수
    common_n=check(n_sorted[i][1],n_sorted[i+1][1])
    max_n=max(max_n,common_n)

    #자기 접두사 길이 업데이트
    length[n_sorted[i][0]]=max(length[n_sorted[i][0]],common_n)
    length[n_sorted[i+1][0]]=max(length[n_sorted[i+1][0]],common_n)

first=0
for i in range(N):
    #비교할 두 수 중 첫 번째 수에 해당
    if first==0:
        #현재 접두사의 길이가 최장 접두사인 경우
        if length[i]==max(length):
            first=n_lst[i]
            print(*first,sep="")
            pre=n_lst[i][:max_n] #두 수 중 두 번째 수가 pre
    #비교할 두 수 중 두 번째 수에 해당
    else:
        if length[i]==max(length) and n_lst[i][:max_n]==pre:
            print(*n_lst[i],sep="")
            break

