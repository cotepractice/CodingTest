# 백준 #14502 연구소
# 15:54-16:12
# 20:55-

# BFS로 가능한 모든 경우의 수에 wall을 직접 설치하고 안전 영역 탐색 
from collections import deque
import copy,sys

input = sys.stdin.readline

N,M = map(int,input().split())
boards = [[-1 for _ in range(M)] for _ in range(N)]


for i in range(N):
    board = list(map(int,input().split()))
    boards[i] = board

answer = 0


#바이러스는 상하좌우 인접한 빈 칸으로 퍼질 수 있음
#벽을 반드시 3개 새로 세워야 함
#0:빈 칸, 1:벽, 2:바이러스

def check(board):
    global answer 

    ans = 0
    for i in range(N):
        for j in range(M):
            if board[i][j]==0:
                ans += 1

    answer = max(answer,ans)

def spread(board):

    Q = deque()
    tmp_board = copy.deepcopy(board)

    dir = [[0,1],[0,-1],[1,0],[-1,0]]

    #바이러스 위치
    for i in range(N):
        for j in range(M):
            if tmp_board[i][j]==2:
                Q.append([i,j])

    #확산
    while Q:
        x,y = Q.popleft()
        for dx,dy in dir:
            nx = x+dx
            ny = y+dy
            if 0<=nx<N and 0<=ny<M and tmp_board[nx][ny]==0:
                tmp_board[nx][ny]=2
                Q.append([nx,ny])

    check(tmp_board)


#bruteforce로 3개 위치 체크
def build(board,cnt):
    
    if cnt==3:
        spread(board)
        return 

    for ni in range(N):
        for nj in range(M):
            if board[ni][nj]==0:
                #건물 세우기
                board[ni][nj]=1
                build(board,cnt+1)
                #건물 부수기
                board[ni][nj]=0
                
build(boards,0)
print(answer)
