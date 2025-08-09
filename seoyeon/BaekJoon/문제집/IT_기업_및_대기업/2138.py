# #1. BackTracking
# #시간복잡도 O(2^N)+ 매번 next 복사해야해 메모리 초과 발생
# #i-1,i,i+1 전구 상태 바꾸기
# N = int(input())
# current = list(map(int,input()))
# last = list(map(int,input()))
# def convert(idx,next_lst):
#     if next_lst[idx]==0:
#         next_lst[idx]=1
#     else:
#         next_lst[idx]=0
#     return next_lst
# answer = -1

# def backtracking(current_i,cnt,current):
#     global answer
#     #print("current",current)
#     #print("current_i",current_i)

#     if current==last:
#         #print("here")
#         answer = cnt
#         return
#     if current_i==N:
#         return

#     #i번째 클릭하는 경우
#     next = current[:]
#     if current_i-1>=0:
#         next=convert(current_i-1,next)
#     next=convert(current_i,next)
#     if current_i+1<N:
#         next=convert(current_i+1,next)

#     backtracking(current_i+1,cnt+1,next)

#     #i번째 클릭하지 않는 경우
#     backtracking(current_i+1,cnt,current)

# backtracking(0,0,current)
# print(answer)

#2. Greedy Algorithm

N=int(input())
current = list(map(int,input()))
target = list(map(int,input()))

def convert(idx,lst):
    if 0<=idx<N:
        if lst[idx]==0:
            lst[idx]=1
        else:
            lst[idx]=0
    return lst

#i-1번째가 타겟과 일치하는지 확인
def greedy(current,target):
    cnt = 0
    for i in range(1,N):
        #같으면 누르지 않음
        if current[i-1]==target[i-1]:
            continue
        #다르면 누름
        else:
            cnt += 1
            for j in range(i-1,i+2):
                current = convert(j,current)
    if current==target:
        return cnt
    else:
        return float("inf")
    
#1.첫 번째 스위치를 누르지 않은 경우
ans1=greedy(current[:],target)

#2.첫 번째 스위치 누른 경우
current=convert(0,current)
current=convert(1,current)

ans2=greedy(current[:],target)

#ans2는 첫 번째 스위치 누른 경우도 추가해야 하므로 1 추가
ans = min(ans1,ans2+1)

if ans==float("inf"):
    print(-1)
else:
    print(ans)
