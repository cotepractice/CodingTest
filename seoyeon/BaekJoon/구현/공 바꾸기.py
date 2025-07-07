#백준10813 공 바꾸기
#구현

n, m = map(int, input().split())
bascket = [(i+1) for i in range(n)]

for k in range(m):
    i, j = map(int, input().split())
    bascket[i-1], bascket[j-1] = bascket[j-1], bascket[i-1]

print(*bascket)