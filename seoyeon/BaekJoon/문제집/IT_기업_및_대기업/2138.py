N = int(input())
current = list(map(int,input()))
last = list(map(int,input()))

#BackTracking
#i-1,i,i+1 전구 상태 바꾸기
def convert(idx,next_lst):
    if next_lst[idx]==0:
        next_lst[idx]=1
    else:
        next_lst[idx]=0
    return next_lst
answer = -1

def backtracking(current_i,cnt,current):
    global answer
    #print("current",current)
    #print("current_i",current_i)

    if current==last:
        #print("here")
        answer = cnt
        return
    if current_i==N:
        return

    #i번째 클릭하는 경우
    next = current[:]
    if current_i-1>=0:
        next=convert(current_i-1,next)
    next=convert(current_i,next)
    if current_i+1<N:
        next=convert(current_i+1,next)

    backtracking(current_i+1,cnt+1,next)

    #i번째 클릭하지 않는 경우
    backtracking(current_i+1,cnt,current)

backtracking(0,0,current)
print(answer)