from collections import deque,defaultdict

#O(1)
boards_dict = defaultdict(list)
speak = []

for i in range(5):
    lst = list(map(int,input().split()))
    for j in range(5):
        boards_dict[lst[j]]=[i,j]

for i in range(5):
    lst = list(map(int,input().split()))
    for l in lst:
        speak.append(l)

column=[0 for _ in range(5)]
row=[0 for _ in range(5)]
cross=[0 for _ in range(2)]

Q = deque(speak)
bingo=0
cnt=0
result=25
while Q:
    k = Q.popleft()
    cnt+=1

    x,y = boards_dict[k]

    #가로세로
    column[x]+=1
    row[y]+=1
    #대각선
    if x==y:
        cross[0]+=1
        #빙고확인
        if cross[0]==5:
            bingo+=1
    if x==5-y-1:
        cross[1]+=1
        #빙고확인
        if cross[1]==5:
            bingo+=1

    #빙고 확인
    if column[x]==5:
        bingo+=1
    if row[y]==5:
        bingo+=1

    if bingo>=3:
        result = cnt
        break

print(result)