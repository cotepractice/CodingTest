import sys

input=sys.stdin.readline

N=int(input())

S = dict()
for _ in range(N):
    sentence = input().strip()
    if sentence=="all":
        S = dict()
        for i in range(1,21):
            S[str(i)]=0
        continue
    elif sentence=="empty":
        S = dict()
        continue
    
    command, x = sentence.split(" ")

    if command=="add":
        if x not in S:
            S[x]=0
    elif command=="remove":
        if x in S:
            del S[x]
    elif command=="check":
        if x in S:
            print(1)
        else:
            print(0)
    elif command=="toggle":
        if x in S:
            del S[x]
        else:
            S[x]=0