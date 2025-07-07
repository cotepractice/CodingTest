#백준 #1644 소수의연속합

N = int(input())

dp = [False for _ in range(N+1)] #소수인 경우 True

#소수
lst = []

#소수 계산
for i in range(2,N+1): #Check1.N까지가 아니라 N+1까지해야 자기자신이 소수인 경우도 처리 가능
    if dp[i]==False:
        dp[i]=True
        lst.append(i)
    else:
        continue
    
    current = i
    while current<N+1: #Check2.N까지가 아니라 N+1까지 해야 마지막 수의 소수 판별 가능
        dp[current]=True
        current+=i

#lst는 정렬되어 있으므로 투포인터 사용
start,end = 0,0
sum = 0
answer = 0
while end<len(lst)+1:
    sum = 0
    for i in range(start,end):
        sum += lst[i]

    #N인 경우 다음 경우의 수 탐색
    if sum==N:
        answer += 1
        start += 1
        continue

    #N보다 작은 경우 end 증가
    if sum < N:
        end += 1
    #N보다 큰 경우 start 증가
    elif sum > N:
        start += 1

print(answer)