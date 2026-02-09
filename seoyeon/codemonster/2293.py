#백준 #2293 동전1

N,K = map(int,input().split())

coins = [0 for _ in range(N)] #동전 종류
costs = [0 for _ in range(K+1)] #가치의 합.costs[k]는 k원이 되는 경우의 수

for n in range(N):
    coins[n]=int(input())

coins.sort()

costs[0]=1


# #아래 로직의 경우 겹칠 수 있음. 동전의 순서만 다르고 구성은 같은 경우를 여러 번 카운트
# #i원이 되는 경우의 수 탐색
# for i in range(1,K+1):
#     #동전 하나씩 확인 
#     for coin in coins:
#         if i-coin>=0 and costs[i-coin]>0:
#             costs[i]+=costs[i-coin]
    
#     print("i",costs[i])

#아래와 같이 coin for문을 앞에 작성해 중복 방지
for coin in coins:
    for i in range(1,K+1):
        if i-coin>=0:
            costs[i]+=costs[i-coin]

print(costs[K])
