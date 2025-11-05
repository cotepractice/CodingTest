#백준 #1644 소수의 연속합
#16:40-17:05
#17:50-18:00

#1. 소수 구하기
#2. 소수로 dp 구하기
#3. Two Pointer로 dp 탐색해 N 구할 수 있는지 확인
# 가능하면 경우의 수 카운트

N = int(input())

#prime1: n 이하의 소수 계산. O(N^2)
# 소수란, 1과 자기 자신만을 인수로 가짐
# def prime(n):

#     p_lst=[] #소수

#     for i in range(2,n+1):
#         check=False
#         #나누어떨어지면 소수 아님
#         for pp in p_lst:
#             if i%pp==0:
#                 check=True
#         if check==False:
#             p_lst.append(i)
    
#     return p_lst

#prime2: O(nlog(logn))
def prime(n):
    p_lst=[]
    is_prime=[True for _ in range(n+1)]
    is_prime[0], is_prime[1]= False, False

    for i in range(2,n+1):
        if is_prime[i]==True:
            p_lst.append(i)

            j=2
            while (i*j)<n+1:
                is_prime[i*j]=False
                j+=1
    print(p_lst)
    return p_lst

#1. 소수 탐색
prime_lst = prime(N)

#2. 누적합 DP 생성
dp=[0 for _ in range(len(prime_lst)+1)]

for i in range(1,len(prime_lst)+1):
    dp[i]=dp[i-1]+prime_lst[i-1]

#3. Two Pointer로 탐색
start,end=0,0
current_s=0
cnt=0

#dp는 정렬되어 있고, 뒤로 갈수록 앞의 차이와 같거나 큼. O(N)
while start<=end:

    #현재 값이 N이면 cnt 증가, 다른 경우의 수 탐색-> start 증가, current_s 업데이트
    if current_s==N:
        cnt+=1
        start+=1
        current_s=dp[end]-dp[start]

    #현재 값이 N 초과이면 start 증가. current_s 업데이트
    elif current_s>N:
        start+=1
        current_s=dp[end]-dp[start]
    
    #현재 값이 N 미만이면 end 증가. current_s 업데이트
    #이때 current_s 업데이트하는데 범위를 벗어나면 종결. 더 진행해도 N 만들 수 없음
    elif current_s<N:
        end+=1
        if end==len(dp):
            break
        else:
            current_s=dp[end]-dp[start]
    
print(cnt)