#백준 #5635 생일 
#정렬문제

import sys

input = sys.stdin.readline

n = int(input())
people = [0 for _ in range(n)]
for i in range(n):
    person = input().split()
    people[i] = person

people.sort(key=lambda x:(int(x[3]),int(x[2]),int(x[1])))

print(people[n-1][0])
print(people[0][0])