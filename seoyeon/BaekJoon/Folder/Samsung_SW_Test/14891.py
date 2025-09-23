#12시방향부터 시게방향 순서
#N극은 0, S극은 1
#양쪽과 맞닿는 부분은 인덱스 2, 6
from collections import deque

wheels = [[] for _ in range(4)]

for i in range(4):
    wheels[i] = list(input())

K = int(input())
#[회전시킨 톱니바퀴 인덱스, 방향]
#방향이 1인 경우 시계 방향, -1인 경우 반시계 방향
k_methods = [[] for _ in range(K)]

for k in range(K):
    x,dir=map(int,input().split())
    k_methods[k] = [x-1,dir]

#current_wheel이 dir 방향으로 회전
def rotate_circle(current_wheel,dir):
    global visited

    #시계방향으로 회전
    #맨 뒤 값을 맨 앞으로 넣기
    if dir==1:
        tmp = wheels[current_wheel][-1]
        del wheels[current_wheel][-1]
        wheels[current_wheel] = [tmp]+wheels[current_wheel]

    #반시계방향으로 회전
    #맨 앞 값을 맨 뒤로 넣기
    else:
        tmp = wheels[current_wheel][0]
        del wheels[current_wheel][0]
        wheels[current_wheel] = wheels[current_wheel]+[tmp]

#현재 바퀴 회전 > 양쪽 바퀴 확인해 회전 결정
def move(wheel_n,dir):
    global visited

    left,right = wheels[wheel_n][6], wheels[wheel_n][2]
    move_lst = [[wheel_n,dir]]

    #왼쪽 확인
    #방문처리, current_wheel과 current_dir 변경
    #move_lst에 넣은 후 한 번에 처리
    current_wheel = wheel_n
    current_dir = dir
    while True:
        if current_wheel-1<0:
            break
        if current_wheel-1>=0 and visited[current_wheel-1]==False and left!=wheels[current_wheel-1][2]:
            move_lst.append([current_wheel-1,current_dir*(-1)])
            visited[current_wheel-1]=True
            left = wheels[current_wheel-1][6]
            current_wheel -= 1
            current_dir *= (-1)
        else:
            break

    #오른쪽 확인
    current_wheel = wheel_n
    current_dir = dir
    while True:
        if current_wheel+1>=4:
            break
        if current_wheel+1<4 and visited[current_wheel+1]==False and right!=wheels[current_wheel+1][6]:
            move_lst.append([current_wheel+1,current_dir*(-1)])
            visited[current_wheel+1]=True
            right = wheels[current_wheel+1][2]
            current_wheel += 1
            current_dir *= (-1)
        else:
            break

    for wheel,d in move_lst:
        rotate_circle(wheel,d)

for i in range(K):
    visited = [False for _ in range(4)]
    move(k_methods[i][0], k_methods[i][1])

answer = 0
for i in range(4):
    if i==0 and wheels[0][0]=="1":
        answer += 1
    if i==1 and wheels[1][0]=="1":
        answer += 2
    if i==2 and wheels[2][0]=="1":
        answer += 4
    if i==3 and wheels[3][0]=="1":
        answer += 8

#마지막에 점수 계산
print(answer)