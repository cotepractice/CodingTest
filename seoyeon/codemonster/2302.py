#백준 #2302 극장좌석

#1. 14% 틀렸습니다.
#경우의 수를 단순히 current_len으로 계산. BUT 경우의 수는 피보나치 수열의 형태 
# N = int(input())
# M = int(input())

# vip_set = set()

# for m in range(M):
#     x = int(input())
#     x-=1
#     vip_set.add(x)

# current_len=0
# dp = [0 for _ in range(N)]

# #가능한 경우의 수 
# #1. 모두 제자리
# #2. 현재 인덱스 c와 이후 인덱스 c+1이 vip가 아닌 경우 1 증가
# for i in range(N):
#     current_len += 1

#     #vip_set인 경우 (직전까지의 길이-1)개의 경우의 수 존재
#     if i in vip_set:
#         dp[i]=current_len-1
#         current_len = 0
#         continue
#     #vip_set이 아니면서 N-1인 경우 current_len 만큼의 경우의 수 존재
#     elif i==N-1:
#         dp[i]=current_len

# ans = 1
# for k in dp:
#     if k!=0:
#         ans*=k

# print(ans)


#2. 
#경우의 수 피보나치 수열로 계산
N = int(input())
M = int(input())

vip_lst = []

for m in range(M):
    x = int(input())
    vip_lst.append(x)

dp = [0 for _ in range(N+1)] #경우의 수
dp[0]=1
dp[1]=1 #[1]

#1) DP 생성
#경우의 수는 dp[i]=dp[i-1]+dp[i-2]
#dp[i-1]: 자기 자리에 앉는 경우
#dp[i-2]: 옆 자리와 바꿔 앉는 경우
for i in range(2,N+1):
    dp[i]=dp[i-1]+dp[i-2]


#2) vip 좌석이 나올 때마다 계산
answer = 1
prev = 0

#vip가 존재하는 경우
if M>0:
    for m in range(M):
        #m번째 vip에서 가지는 경우의 수는 dp[vip가 아닌 좌석 개수]
        answer *= dp[vip_lst[m]-prev-1]
        prev = vip_lst[m]
    answer *= dp[N-prev]
#vip가 없는 경우
else:
    answer = dp[N]

print(answer)