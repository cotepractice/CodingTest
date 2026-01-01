#백준 #24337 가희와 탑

#입력 
# N:건물의 개수, a:가희가 볼 수 있는 건물 개수, b:단비가 볼 수 있는 건물 개수
#출력
# N개의 건물 높이 정보
# 사전순으로 가장 앞선 것
N, a, b = map(int,input().split())

#a,b 중 가장 큰 높이
max_h = max(a,b)

stack = []

#[1,2,3,...,(a-1), max_h, (b-1), ..., 1]
#1. 1~(a-1)
for i in range(1,a):
    stack.append(i)
#2. max(a,b)
stack.append(max_h)
#3. (b-1)~1
for j in range(b-1,0,-1):
    stack.append(j)

if len(stack)>N:
    print(-1)
else:
    #[핵심] 아래가 오름차순으로 정렬하는 방법!
    #첫 번째 건물 출력
    print(stack[0])
    #이후 부족한만큼 1 채움
    if (N-len(stack))>0:
        for _ in range(N-len(stack)):
            print(1,sep=" ",end=" ")
    #나머지 건물 출력
    print(*stack[1:],sep=" ")