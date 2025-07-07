#백준 #22233 가희와 키워드
import sys

input = sys.stdin.readline

N, M = map(int,input().split())

words = {} #dictionary
for i in range(N):
    word = input().strip()
    words[word] = i

memos = [[] for _ in range(M)]
for i in range(M):
    memo_strip = input().strip()
    memo = list(memo_strip.split(','))
    for m in memo:
        if m in words:
            del words[m]

    print(len(words))
