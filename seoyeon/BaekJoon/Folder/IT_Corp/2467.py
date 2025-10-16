#백준 #2467 용액
#20:30-20:47

#Divide and Conquer
N = int(input())
N_lst = list(map(int,input().split()))

s,e = 0,N-1
minimum = [float("inf"),-1,-1] #[차이,값1,값2] 

while s<e:
    #print("minimum:",minimum)
    #print("s,e",s,e)

    #현재 s,e 비교
    if abs(N_lst[s]+N_lst[e])<minimum[0]:
        minimum = [abs(N_lst[s]+N_lst[e]),N_lst[s],N_lst[e]]
    
    # 1. s 고정, s와 e-1의 합이 더 작으면 1) e 감소하고 2)minimum과 비교해 업데이트
    # s==e인 경우 종결
    # 2. s와 e-1의 합이 더 작지 않으면 while문 종료
    while True:
        if abs(N_lst[s]+N_lst[e-1])<abs(N_lst[s]+N_lst[e]):
            e -= 1
            if e==s:
                break
            if abs(N_lst[s]+N_lst[e])<minimum[0]:
                minimum = [abs(N_lst[s]+N_lst[e]),N_lst[s],N_lst[e]]
        else:
            break

    s+=1

print(minimum[1], minimum[2])