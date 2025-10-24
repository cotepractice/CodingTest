#백준 #1253 좋다

#1. Two Pointer: 같은 수가 중복되는 경우, 이를 처리하지 못함
# N = int(input())
# N_lst=list(map(int,input().split()))
# N_dict=dict()

# N_lst.sort()
# for i in range(N-1):
#     for j in range(i+1,N):
#         N_dict[N_lst[i]+N_lst[j]]=0

# answer=0
# for val in N_lst:
#     if val in N_dict:
#         answer+=1

# print(answer)

#2.Two Pointer
N = int(input())
N_lst=list(map(int,input().split()))
N_lst.sort()

answer=0
for i in range(N):
    current=N_lst[i]
    tmp=N_lst[:i]+N_lst[i+1:]
    start,end=0,len(tmp)-1

    while start<end:
        if tmp[start]+tmp[end]==current:
            answer+=1
            break
        
        elif tmp[start]+tmp[end]<current:
            start+=1
        elif tmp[start]+tmp[end]>current:
            end-=1

print(answer)