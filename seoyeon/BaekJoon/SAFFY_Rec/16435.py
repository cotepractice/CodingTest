#백준 #16435 스네이크버드

N, L = map(int,input().split())

h_lst = list(map(int,input().split()))

h_lst.sort()

cur_L = L

for h in h_lst:
    if h<=cur_L:
        cur_L += 1
    else:
        break

print(cur_L)