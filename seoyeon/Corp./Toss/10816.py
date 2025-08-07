N = int(input())
cards = list(map(int,input().split()))
M = int(input())
choose = list(map(int,input().split()))

cards_d = dict()

for c in cards:
    if c in cards_d:
        cards_d[c] += 1
    else:
        cards_d[c]=1

result = [0 for _ in range(M)]
for ch in range(M):
    if choose[ch] in cards_d:
        result[ch]=cards_d[choose[ch]]

print(*result)