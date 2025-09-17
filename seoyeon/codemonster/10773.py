#10773 제로

K = int(input())

stack = []

for k in range(K):
    x = int(input())
    
    if x!=0:
        stack.append(x)
    else:
        stack.pop()

print(sum(stack))