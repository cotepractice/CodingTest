#백준 #2138 전구와 스위치

#23:00-23:37
#i번 스위치 누르면 i-1,i,i+1 전구 변화
#꺼져 있는 전구는 켜지고, 켜져 있는 전구는 꺼짐
#N개의 전구와 만들고자 하는 상태를 만들기 위해 최소 몇 번 눌러야 하는지

N = int(input())

current_str=list(map(int,input()))
target_str=list(map(int,input()))

def change(current,idx):
    if current[idx]==0:
        return 1
    else:
        return 0

cnt1=0
cnt2=1

#0번 인덱스는 idx=0,1일 때 두 번 변경될 수 있음
#1)current_str1: 0 index 바꾸지 않는 경우
#2)current_str2: 0 index 바꾸는 경우
current_str1=current_str[:]

#index 변경
current_str2=current_str[:]
current_str2[0]=change(current_str2,0)
current_str2[1]=change(current_str2,1)

#모두 for문 1이상 N미만으로 진행. 1 포함 N 미포함 (버튼이 인덱스 형태. 0부터 N-1까지 존재)
#1. current_str1
for i in range(1,N):
    #i-1 비교해 진행
    #다를 경우, i-1,i,i+1 변경
    if current_str1[i-1]!=target_str[i-1]:
        cnt1+=1

        #i-1,i,i+1 변경
        current_str1[i-1]=change(current_str1,i-1)
        if i<N:
            current_str1[i]=change(current_str1,i)
        if i+1<N:
            current_str1[i+1]=change(current_str1,i+1)

#2.current_str2
for i in range(1,N):
    #i-1 비교해 진행
    #다를 경우, i-1,i,i+1 변경
    if current_str2[i-1]!=target_str[i-1]:
        cnt2+=1

        #i-1,i,i+1 변경
        current_str2[i-1]=change(current_str2,i-1)
        if i<N:
            current_str2[i]=change(current_str2,i)
        if i+1<N:
            current_str2[i+1]=change(current_str2,i+1)


answer=float("inf")

if current_str1==target_str:
    answer=min(answer,cnt1)
if current_str2==target_str:
    answer=min(answer,cnt2)

if answer==float("inf"):
    print(-1)
else:
    print(answer)

    