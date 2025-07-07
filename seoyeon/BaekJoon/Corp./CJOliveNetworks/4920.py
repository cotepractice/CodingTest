#백준 #4920 테트리스 게임
#13:24-15:00

from collections import deque

def rotate_90(block):
    # 블록 내 좌표를 90도 회전: (x, y) → (y, -x)
    return [[y, -x] for x, y in block]

answer_lst = [] #+) 결과값을 즉시 출력하지 않고 저장할 리스트 필요
while True:
    N = int(input()) 
    if N==0: #+) 아래에서 따로 처리하는 경우 두 번 입력받아야 하므로 ValueError 발생
        break

    answer = -1*float("inf") #+) 값이 음수가 들어올 수 있음
    boards = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        boards[i] = list(map(int,input().split()))

    # 각 줄별로 1,2,3,4,5번째 블럭의 기본값 + 회전값
    # ㅣ, Z, ㄱ, ㅜ, ㅁ
    base_blocks=[[[0,0],[0,1],[0,2],[0,3]],
            [[0,0],[0,1],[1,1],[1,2]],
            [[0,0],[0,1],[0,2],[1,2]],
            [[0,0],[0,1],[1,1],[0,2]],
            [[0,0],[0,1],[1,0],[1,1]]]
    
    # #사용가능한 모든 blocks
    blocks = set()
    #base_blocks 회전
    for base in base_blocks: #base: [[0,0],[0,1],[0,2],[0,3]]
        current = base 
        for _ in range(4):  # 회전 0도, 90도, 180도, 270도
            # tuple 사용 이유: set()에는 list를 넣을 수 없음. list는 mutable, tuple은 unmutable
            # sorted 사용 이유:좌표값은 같고 순서가 다른 경우 하나의 모양으로 인지해야함 
            normalized = tuple(sorted((x, y) for x, y in current)) 
            blocks.add(normalized)
            current = rotate_90(current)
            
    for x in range(N):
        for y in range(N):
            for block in blocks:
                b1,b2,b3,b4=block
                nx1,ny1 = x+b1[0],y+b1[1]
                nx2,ny2 = x+b2[0],y+b2[1]
                nx3,ny3 = x+b3[0],y+b3[1]
                nx4,ny4 = x+b4[0],y+b4[1]
                if 0<=nx1<N and 0<=nx2<N and 0<=nx3<N and 0<=nx4<N and 0<=ny1<N and 0<=ny2<N and 0<=ny3<N and 0<=ny4<N:
                    ans = boards[nx1][ny1] + boards[nx2][ny2] + boards[nx3][ny3] + boards[nx4][ny4]
                    answer = max(answer,ans)
    answer_lst.append(answer)

for i in range(len(answer_lst)):
    print(i+1,".",sep="",end=" ")
    print(answer_lst[i])