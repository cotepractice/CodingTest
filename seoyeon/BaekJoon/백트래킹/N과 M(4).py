import copy

N, M = map(int, input().split())
lst = []

def compute(lst,min):
    lstCopy = copy.deepcopy(lst)
    if len(lst) == M:
        print(*lst)
        return
    for i in range(min,N+1):
        lstCopy.append(i)
        compute(lstCopy,i)
        lstCopy = copy.deepcopy(lst)

for i in range(1,N+1):
    lst = [i]
    compute(lst,i)