#백준 #1920 수 찾기
#정렬 문제
#00:42
#이분탐색 사용하는 것이 포인트. 사용하지 않으면 시간초과 발생

#1. 본인풀이 => 시간 초과 발생
import sys

input = sys.stdin.readline

n = int(input())

origin = list(map(int, input().split()))

m = int(input())

compare = list(map(int, input().split()))

origin.sort()

check = [0 for _ in range(m)]

for compare_idx in range(m):
    if compare[compare_idx] in origin:
        check[compare_idx] = 1

print(*check, sep="\n")

#2. 이분탐색 사용한 풀이 
import sys

input = sys.stdin.readline

n = int(input())

origin = list(map(int, input().split()))

m = int(input())

compare = list(map(int, input().split()))

origin.sort()

#이분탐색
for i in range(m):
    left = 0
    right = n-1
    mid = (left+right)//2
    check = 0

    while (left<=right):
        mid = (left+right)//2
        if (compare[i] == origin[mid]):
            check = 1
            print(1)
            break
        elif (compare[i] > origin[mid]):
            left = mid + 1
        elif (compare[i] < origin[mid]):
            right = mid -1

    if (check == 0):
        print(0)