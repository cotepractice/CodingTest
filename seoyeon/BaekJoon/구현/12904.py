#백준 #12904 A와B

S = input()
T = input()

#T->S
answer = 0
while True:
    if len(T)<=len(S):
        if T==S:
            answer=1
        break
    if T[-1]=="A":
        T = T[:-1]
    elif T[-1]=="B":
        T = T[:-1]
        T = T[::-1]

print(answer)