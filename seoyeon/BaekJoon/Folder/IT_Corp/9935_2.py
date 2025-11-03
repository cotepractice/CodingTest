#백준 #9935 문자열 폭발

from collections import deque

sentence=list(input())
string=list(input())

# 1. 리스트에 넣기 
# 2. 해당 리스트 슬라이싱한 결과가 string이면 Q.pop()
Q=[]
for s in sentence:
    Q.append(s)

    if Q[len(Q)-len(string):len(Q)]==string:
        for _ in range(len(string)):
            Q.pop()

result=""
if len(Q)==0:
    print("FRULA")
else:
    #1. 아래와 같이 for문으로 진행하는 경우 시간초과 발생 
    #O(len(Q)^2)
    # for q in Q:
    #     result+=q
    # print(result)

    #2. 전체 한 번에 계산
    #O(len(Q))
    print(*Q,sep="")