#백준 #17144 미세먼지 안녕!
#구현문제
#17:05-18:20
#15:44-16:37
#미해결

# #1. 시간초과 발생
# import sys

# input = sys.stdin.readline

# r, c, t = map(int, input().split()) #세로 r, 가로 c, t초 지난 후의 결과 도출

# origin = [[0 for _ in range(c)] for _ in range(r)]
# area = [[0 for _ in range(c)] for _ in range(r)]
# circulator = [0, 0]

# for i in range(r):
#     origin[i] = list(map(int, input().split()))

# check = 0
# for i in range(r):
#     for j in range(c):
#         area[i][j] = origin[i][j]
#         if (origin[i][j] == -1):
#             circulator[check] = [i,j]
#             check += 1

# #for문
# #1. 확산
# dx = [0,0,-1,1]
# dy = [-1,1,0,0]

# for _ in range(t):
    
#     #1-1. 1초동안 확산
#     for i in range(r):
#         for j in range(c):
#             if (origin[i][j] > 0):
#                 cnt = 0
#                 side = 0
#                 for k in range(4):
#                     x = i+dx[k]
#                     y = j+dy[k]
#                     if (0<=x<r and 0<=y<c):
#                         if (origin[x][y] != -1):
#                             cnt += 1
#                             side = origin[i][j] // 5
#                             area[x][y] += side
#                 area[i][j] -= side*cnt   
    
#     #1-2. origin과 area 일치
#     for i in range(r):
#         for j in range(c):
#             origin[i][j] = area[i][j]

#     #2-1. 공기 청정기 가동
#     for l in range(2):
#         x, y = circulator[l]
#         start_x = x
#         start_y = y

#         #반시계방향
#         if (l == 0):
#             area[x][y+1] = 0    #공기청정기 바로 옆
#             y += 1
#             while y<c-1:
#                 y += 1
#                 prev = origin[x][y-1]
#                 area[x][y] = prev
            
#             while x>0:
#                 x -= 1
#                 prev = origin[x+1][y]
#                 area[x][y] = prev

#             while y>0:
#                 y -= 1
#                 prev = origin[x][y+1]
#                 area[x][y] = prev
            
#             while x<start_x:
#                 x += 1
#                 if (origin[x][y] != -1):
#                     prev = origin[x-1][y]
#                     area[x][y] = prev

#             while y<start_y:
#                 y += 1
#                 if (origin[x][y] != -1):
#                     prev = origin[x][y-1]
#                     area[x][y] = prev

#         #시계방향
#         else:
#             area[x][y+1] = 0    #공기청정기 바로 옆
#             y += 1
#             while y<c-1:
#                 y += 1
#                 prev = origin[x][y-1]
#                 area[x][y] = prev

#             while x<r-1:
#                 x += 1
#                 prev = origin[x-1][y]
#                 area[x][y] = prev

#             while y>0:
#                 y -= 1
#                 prev = origin[x][y+1]
#                 area[x][y] = prev
            
#             while x>start_x:
#                 x -= 1
#                 if (origin[x][y] != -1):
#                     prev = origin[x+1][y]
#                     area[x][y] = prev

#             while y<start_y:
#                 y += 1
#                 if (origin[x][y] != -1):
#                     prev = origin[x][y-1]
#                     area[x][y] = prev

#     #2-2. origin과 area 일치
#     for i in range(r):
#         for j in range(c):
#             origin[i][j] = area[i][j]

# #출력
# sum = 0
# for i in range(r):
#     for j in range(c):
#         if (origin[i][j] != -1):
#             sum += origin[i][j]
# print(sum)

#2. 
import sys

input = sys.stdin.readline

r, c, t = map(int, input().split()) #세로 r, 가로 c, t초 지난 후의 결과 도출

origin = [[0 for _ in range(c)] for _ in range(r)]
top_robot = 0
bottom_robot = 0

for i in range(r):
    origin[i] = list(map(int, input().split()))

#for문
#상 우 하 좌
dx = [-1,0,1,0]
dy = [0,1,0,-1]

#1. 확산
def spread():
    area = [[0 for _ in range(c)] for _ in range(r)]    #spread시 계산된 값을 저장하는 리스트

    for i in range(r):
        for j in range(c):
            if (origin[i][j] > 0):
                cnt = 0
                side = 0
                for k in range(4):
                    x = i+dx[k]
                    y = j+dy[k]
                    if (0<=x<r and 0<=y<c):
                        if (origin[x][y] != -1):
                            cnt += 1
                            side = origin[i][j] // 5
                            area[x][y] += side
                area[i][j] -= side*cnt   
    
    for i in range(r):
        for j in range(c):
            origin[i][j] += area[i][j]

def rotation():
    #위쪽 회전
    def top_rotation():
        d = 1   #dx,dy 계산시 index로 사용. d=1인 경우 dx,dy로 인해 오른쪽으로 이동
        before = 0  #가장 첫번째의 위치는 0, 이후에는 아래에서 swap 으로 변경한 값
        x, y = top_robot, 1 #공기 청정기 바로 옆부터 시작
        while True:
            ax = x+dx[d]
            ay = y+dy[d]
            if (ax == r or ay == c or ax == -1 or ay == -1):    #꼭짓점의 경우 방향 변경
                d = (d-1)%4
                continue
            if (x == top_robot and y == 0):
                break
            origin[x][y], before = before, origin[x][y] #이전 값을 before 변수로 저장
            x, y = ax, ay

    #아래쪽 회전
    def bottom_rotation():
        d = 1
        before = 0
        x, y =bottom_robot, 1
        while True:
            ax = x+dx[d]
            ay = y+dy[d]
            if (ax == r or ay == c or ax == -1 or ay == -1):    #현재 위치가 꼭짓점에 해당
                d = (d+1)%4 #top_rotation과 방향이 반대이므로 d값도 다름
                continue
            if (x == bottom_robot and y == 0):
                break
            origin[x][y], before = before, origin[x][y]
            x,y = ax,ay

    
    top_rotation()
    bottom_rotation()

#공기청정기 위치 찾기
for i in range(r):
    if origin[i][0] == -1:
        top_robot = i
        bottom_robot = i+1
        break

# print(top_robot)
#t초 반복
for _ in range(t):
    spread()
    rotation()

#출력
answer = 2  #공기청정기 -1 두개 계산
for i in range(r):
    for j in range(c):
        answer += origin[i][j]
print(answer)