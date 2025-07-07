#백준 #10814 나이순 정렬
#정렬 문제

import sys

input = sys.stdin.readline

T = int(input())

lst = []

for i in range(T):
    age, name = input().split()
    age = int(age)

    lst.append((age,name))
        
lst.sort(key=lambda x:x[0])

for i in range(len(lst)):
    print(lst[i][0], lst[i][1])
