#백준 #14888 연산자 끼워넣기
#16:55-

N = int(input())

A_lst = list(map(int,input().split()))
#[덧셈개수,뺄셈개수,곱셈개수,나눗셈개수]
operator = list(map(int,input().split()))

#출력: 만들 수 있는 식의 결과가 최대인 것과 최소인 것
maximum, minimum = -float("inf"), float("inf")


def bruteforce(idx,ans,operator):
    global maximum, minimum
    
    #종결 조건
    if idx==N-1:
        maximum = max(maximum, ans)
        minimum = min(minimum, ans)
        return

    #계산: 다음 값까지
    #덧셈
    if operator[0]>0:
        operator[0] -= 1
        bruteforce(idx+1,ans+A_lst[idx+1],operator)
        operator[0] += 1 #복구
    #뺄셈
    if operator[1]>0:
        operator[1] -= 1
        bruteforce(idx+1,ans-A_lst[idx+1],operator)
        operator[1] += 1 #복구
    #곱셈
    if operator[2]>0:
        operator[2] -= 1
        bruteforce(idx+1,ans*A_lst[idx+1],operator)
        operator[2] += 1 #복구
    #나눗셈
    if operator[3]>0:
        operator[3] -= 1
        if ans>0:
            bruteforce(idx+1,ans//A_lst[idx+1],operator)
        else:
            tmp = -1*ans
            tmp = tmp//A_lst[idx+1]
            tmp *= -1
            bruteforce(idx+1,tmp,operator)
        operator[3] += 1 #복구 
    

bruteforce(0,A_lst[0],operator)
print(maximum)
print(minimum)