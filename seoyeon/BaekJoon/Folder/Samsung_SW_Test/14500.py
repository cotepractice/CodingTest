# #백준 #14500 테트로미노
# 2:40
# "ㅗ" 제외한 블럭이 블럭 4개로 갈 수 있는 모든 경로!

# #2. ㅗ 제외 DFS로 탐색

# N,M = map(int,input().split()) #N:세로, M:가로 (4<=N,M<=500)
# boards = [[0 for _ in range(M)] for _ in range(N)]

# for i in range(N):
#     board = list(map(int,input().split()))
#     boards[i]=board

# visited=[[False for _ in range(M)] for _ in range(N)]
# maximum = 0
# #print("visited",visited)

# dir = [[1,0],[-1,0],[0,-1],[0,1]]

# # "ㅗ" 제외
# def dfs(x,y,tmp,cnt):
#     global maximum

#     if cnt==4:
#         maximum = max(maximum,tmp)
#         return
    
#     for dx,dy in dir:
#         nx = x+dx
#         ny = y+dy
#         #print("nx",nx,ny)
#         if 0<=nx<N and 0<=ny<M and visited[nx][ny]==False:
#             visited[nx][ny]=True
#             dfs(nx,ny,tmp+boards[nx][ny],cnt+1)
#             visited[nx][ny]=False

# # "ㅗ" 모양. [x,y]를 기준으로 상하좌우 탐색해 가장 큰 값으로 만듬 
# def fy(x,y):
#     global maximum

#     arr = []

#     for dx,dy in dir:
#         nx = x+dx
#         ny = y+dy
#         if 0<=nx<N and 0<=ny<M:
#             arr.append(boards[nx][ny])            

#     #4개면 가장 작은 값 제거
#     if len(arr)==4:
#         arr.sort(reverse=True)
#         arr.pop()
#         maximum = max(maximum, sum(arr)+boards[x][y])
    
#     elif len(arr)==3:
#         maximum = max(maximum, sum(arr)+boards[x][y])
#     return 


# #Bruteforce
# for i in range(N):
#     for j in range(M):
#         visited[i][j]=True
#         dfs(i,j,boards[i][j],1)
#         fy(i,j)
#         visited[i][j]=False

# print(maximum)


# from collections import deque

# N,M = map(int,input().split()) #N:세로, M:가로 (4<=N,M<=500)
# boards = [[0 for _ in range(M)] for _ in range(N)]

# for i in range(N):
#     board = list(map(int,input().split()))
#     boards[i]=board

# #회전, 대칭 진행
# base = [[[0,0],[0,1],[0,2],[0,3]], [[0,0],[0,1],[1,0],[1,1]], [[0,0],[1,0],[2,0],[2,1]], [[0,0],[1,0],[1,1],[2,1]], [[0,0],[0,1],[0,2],[1,1]]]
# all_tetromino = []

# # tetro1 = [[[0,0],[0,1],[0,2],[0,3]]]
# # tetro2 = [[[0,0],[0,1],[1,0],[1,1]]]
# # tetro3 = [[[0,0],[1,0],[2,0],[2,1]]]
# # tetro4 = [[[0,0],[1,0],[1,1],[2,1]]]
# # tetro5 = [[[0,0],[0,1],[0,2],[1,1]]]

# #회전
# # def rotate_90(lst):
# #     global all_tetromino 

# #     #lst 블럭으로 얻을 수 있는 모든 모양
# #     block_set = []
# #     block_set.append(lst)
#     #print("lst",lst)

#     #오른쪽으로 90도 회전 
#     #모양이 다른 경우 계속 Q에 넣어서 돌리기
#     # 3*3 board로 생각해 회전시키면 편함 !
#     # [1,2,3]. -> [7,4,1]         #1) [0,0]->[0,2]->[2,2]->[2,0] 
#     # [4,5,6].    [8,5,2]         #2) [0,1]->[1,2]->[2,1]->[1,2] 
#     # [7,8,9]     [9,6,3]

#     # cnt = 0
#     # #하나의 블럭. 4개 위치좌표 존재
#     # b = lst
#     # cnt += 1

#     # while cnt<3: 
#     #     rotate_lst = []
        
#     #     #bx,by는 처음 좌표
#     #     #rx,ry는 이동 후 좌표
#     #     for bx, by in b:
#     #         rx = by
#     #         ry = M-bx
#     #         if 0<=rx<N and 0<=ry<M:
#     #             rotate_lst.append([rx,ry])
#     #         print("rxrx",rx,ry)
#     #     #정렬해서 넣어야 중복 제거 가능
#     #     #Ex. [[0,0],[0,1],[0,2],[0,3]] = [[0,3],[0,2],[0,1],[0,0]]
#     #     rotate_lst.sort()
#     #     print("Rotate_lst",rotate_lst)
#     #     #좌표 4개가 모두 범위 내 존재하고, 이전 모양과 다른 경우 -> block_dict에 저장 + Q에 저장(이후 한 번 더 돌려봐야 함)
#     #     if len(rotate_lst)==4 and rotate_lst not in block_set:
#     #         block_set.append(rotate_lst)
#     #         b = rotate_lst

#     #     cnt += 1

#     # print("Block_set",block_set)

#     #대칭값
#     #block_dict에서 하나씩 뽑아 대칭
#     for l in block_set:
#         block_set = symmetry(block_set,l)
    
#     #하나씩 all_tetromino에 넣기
#     for block_d in block_set:
#         all_tetromino.append(block_d)

#     print("All_set",all_tetromino)

# # [[0,0],[0,1],[0,2],[0,3]] -> [[0,3],[0,2],[0,1],[0,0]]
# #[[0,0],[1,0],[2,0],[2,1]] -> [[0,1],[1,1],[2,1],[2,0]]
# def symmetry(block_set,lst):
#     symmetry_lst = []

#     for b_idx in range(len(lst)):
#         change_idx = abs(3-b_idx)

#         rx = lst[change_idx][0]
#         ry = lst[change_idx][1]
#         if 0<=rx<N and 0<=ry<M:
#             symmetry_lst.append([rx,ry])

#     #정렬해야 중복 제거 가능
#     symmetry_lst.sort()

#     if len(symmetry_lst)==4 and symmetry_lst not in block_set:
#         block_set.append(symmetry_lst)

#     return block_set


# for b in base:
#     rotate_90(b)

# # #시간복잡도 O(N*M*(8*4))
# #print("all_tetromino",all_tetromino)
# answer = 0
# for i in range(N):
#     for j in range(M):
#         #가능한 모든 블럭 탐색
#         n1,n2 = i,j
#         for one_block in all_tetromino:
#             ans = 0
#             cnt = 0
#             for b1,b2 in one_block:
#                 n1,n2 = i+b1,j+b2
#                 if n1<0 or n1>=N or n2<0 or n2>=M:
#                     continue
#                 cnt += 1
#                 ans += boards[n1][n2]
            
#             #4좌표 모두 범위 내 존재하면 칸의 수 계산
#             if cnt==4:
#                 answer = max(answer,ans)
        
# print(answer)            

# # 백준 14500 테트로미노
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
boards = [list(map(int, input().split())) for _ in range(N)]

# 기본 블럭 5개 (회전/대칭 전)
# 상대좌표 (0,0) 기준
base = [
    [[0,0],[0,1],[0,2],[0,3]],   # ㅡ
    [[0,0],[1,0],[0,1],[1,1]],   # ㅁ
    [[0,0],[1,0],[2,0],[2,1]],   # ㄴ
    [[0,0],[1,0],[1,1],[2,1]],   # ㄹ
    [[0,0],[0,1],[0,2],[1,1]]    # ㅗ
]

def normalize(block):
    min_x = min(x for x,y in block)
    min_y = min(y for x,y in block)
    #좌표들을 (0,0) 기준으로 이동 후 정렬
    norm = sorted([[x-min_x, y-min_y] for x,y in block])

    return tuple(map(tuple, norm))   # set에 넣기 위해 tuple로 변환

#왼쪽으로 90도 회전
def rotate(block):
    return [[y, -x] for x,y in block]

#y축 대칭
def symmetry(block):
    return [[x, -y] for x,y in block]

# 모든 블럭 좌표 구하기
all_tetromino = set()

for b in base:
    shapes = set()
    q = [b]

    while q:
        cur = q.pop()
        norm = normalize(cur)
        if norm in shapes:
            continue
        shapes.add(norm)

        # 회전
        q.append(rotate(cur))
        # 대칭
        q.append(symmetry(cur))

    # shapes 안에 이 블럭에서 만들 수 있는 모든 변형이 들어있음
    all_tetromino.update(shapes)

# 이제 모든 보드 위치에서 블럭 올려보기
answer = 0
for i in range(N):
    for j in range(M):
        for block in all_tetromino:
            s = 0
            ok = True
            for dx, dy in block:
                x, y = i+dx, j+dy
                if 0 <= x < N and 0 <= y < M:
                    s += boards[x][y]
                else:
                    ok = False
                    break
            if ok:
                answer = max(answer, s)

print(answer)