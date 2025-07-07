#백준 11399
#정렬문제
#ATM

import sys

input = sys.stdin.readline

n = int(input())

lst = list(map(int,input().split()))
lst.sort()

sum = 0
for i in range(n):
    for k in range(i+1):
        sum += lst[k]

print(sum)