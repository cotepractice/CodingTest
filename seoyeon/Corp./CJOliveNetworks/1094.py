#백준 #1094 막대기

#17:00-17:17

from collections import deque
x = int(input())

sticks = [64]

while True:
    sum = 0
    min_stick = float("inf")
    for stick in sticks:
        sum += stick
        min_stick = min(min_stick,stick)
    sticks.sort()
    if sum > x:
        slice_length = min_stick//2
        if sum-slice_length>=x:
            del sticks[0]
            sticks.append(slice_length)
        else:
            del sticks[0]
            sticks.append(slice_length)
            sticks.append(slice_length)
    result = 0
    for stick in sticks:
        result += stick
    if result==x:
        print(len(sticks))
        break
        