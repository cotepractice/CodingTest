x = int(input())

sticks = []
sticks.append(64)

while True:
    sum = 0
    for stick in sticks:
        sum += stick
        
    if sum==x:
        break
    sticks.sort()
    if sum>x:
        smallest = sticks[0]
        del sticks[0]

        half = smallest//2
        if sum-half>=x:
            sticks.append(half)
        else:
            sticks.append(half)
            sticks.append(half)

print(len(sticks))