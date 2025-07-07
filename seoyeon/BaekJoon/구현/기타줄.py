#백준 #1049 기타줄
#구현문제

n,m = map(int, input().split())

piece6 = [0 for _ in range(m)]
piece1 = [0 for _ in range(m)]
min_price = [0 for _ in range(m)]

for i in range(m):
    a, b = map(int, input().split())

    piece6[i] = a
    piece1[i] = b

piece6.sort()
piece1.sort()

a = piece6[0]
b = piece1[0]
#print("a,b",a,b)

#1.나누어질때까지는 모둠으로 구매하고 남은건 낱개로 구매
result1 = 0
result1 += a * (n//6)   #모둠으로 구매
n1 = n - (n//6)*6
result1 += b*n1     #남은건 낱개로 구매

#2. 모두 모둠으로 구매
result2= 0
result2 = a * ((n//6) + 1)

#3. 모두 낱개로 구매
result3 = n*b

#print("result1,2,3",result1, result2, result3)
result = min(result1,result2,result3)
print(result)