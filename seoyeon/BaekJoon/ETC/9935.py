#백준 #9935 문자열 폭발

from collections import deque

strings = input()
bomb = list(input())

stack = []

for s in strings:
    stack.append(s)
    
    if stack[len(stack)-len(bomb):len(stack)]==bomb:
        for k in range(len(bomb)):
            stack.pop()
if len(stack)==0:
    print("FRULA")
else:
    print(*stack,sep="")