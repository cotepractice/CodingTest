def rotate_90(block):
    return [[y,-x] for x,y in block]

base_blocks = [[[0,0],[0,1],[0,2],[0,3]],
               [[0,0],[0,1],[1,1],[1,2]],
               [[0,0],[0,1],[0,2],[1,2]],
               [[0,0],[0,1],[0,2],[1,1]],
               [[0,0],[0,1],[1,0],[1,1]]
                ]

result = []
while True:
    N=int(input())
    if N==0:
        break

    boards = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        boards[i] = list(map(int,input().split()))

    blocks = set() #반복되는 것 제거

    for b in base_blocks:
        cnt = 0
        b1,b2,b3,b4 = b
        current=b
        #4번 회전 가능
        for _ in range(4):
            tmp = tuple(sorted((i,j) for i,j in current))
            blocks.add(tmp)
            current = rotate_90(current)       

    answer = -float("inf")
    for i in range(N):
        for j in range(N):
            for b in blocks:
                b1,b2,b3,b4 = b
                nx1,ny1 = i+b1[0],j+b1[1]
                nx2,ny2 = i+b2[0],j+b2[1]
                nx3,ny3 = i+b3[0],j+b3[1]
                nx4,ny4 = i+b4[0],j+b4[1]

                if 0<=nx1<N and 0<=nx2<N and 0<=nx3<N and 0<=nx4<N and 0<=ny1<N and 0<=ny2<N and 0<=ny3<N and 0<=ny4<N:
                    ans=boards[nx1][ny1]+boards[nx2][ny2]+boards[nx3][ny3]+boards[nx4][ny4]
                    answer = max(answer,ans)
    result.append(answer)

for i in range(len(result)):
    print(i+1,".",sep="",end=" ")
    print(result[i])