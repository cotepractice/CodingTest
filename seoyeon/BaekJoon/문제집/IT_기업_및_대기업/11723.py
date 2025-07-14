#11723 집합
#PyPy3

import sys

input = sys.stdin.readline

N = int(input())

S = dict()

for _ in range(N):
    inp = input().rstrip() #하나씩 입력받기 때문에 .rstrip() 처리 필요

    if inp=="empty":
        S = dict()
        continue
    elif inp=="all":
        S = dict()
        for i in range(1,21): #str형으로 넣어야 함.int로 넣으면 아래에 x=int(x)로 변환
            S[str(i)]=0
        continue
    else:
        cal, x = inp.split()


    if cal == "add":
        if x not in S:
            S[x]=0
    
    elif cal == "remove":
        if x in S:
            del S[x]
    
    elif cal == "check":
        if x in S:
            print(1)
        else:
            print(0)
    
    elif cal == "toggle":
        if x in S:
            del S[x]
        else:
            S[x]=0
    
