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

#현재 바퀴 회전 > 양쪽 바퀴 확인해 회전 결정
#반시계 방향이 popleft()
def move(wheel_n,dir,visited):
    print("wheel_n,dir",wheel_n,dir)
    #방문처리

    #visited[wheel_n]=True
    #양쪽 바퀴 확인
    left,right = wheels[wheel_n][6], wheels[wheel_n][2]
    #print("leftright",left,right)
    #왼쪽 확인
    if wheel_n==0:
        pass
    else:
        #print("HERE1",wheels[wheel_n-1][2])
        #방향 다르면 반시계 방향 회전
        if visited[wheel_n-1]==False and wheels[wheel_n-1][2]!=left:
            #현재 톱니바퀴가 시계방향. 왼쪽 바퀴는 반시계 방향
            #맨 앞 원소 맨 뒤에 넣기
            #print("LEFT")
            if dir==1:
                #print("Turn Clock Dir")
                #print("BEFORE",wheels[wheel_n-1])
                tmp = wheels[wheel_n-1][0]
                del wheels[wheel_n-1][0]
                wheels[wheel_n-1].append(tmp)
                #print("After",wheels[wheel_n-1])
                visited[wheel_n-1] = True
                move(wheel_n-1,-1,visited)
            #현재 톱니바퀴가 반시계방향. 왼쪽 바퀴는 시계 방향
            #맨 뒤 원소 맨 앞으로 빼기
            else:
                #print("Turn Reverse Clock Dir")
                #print("BEFORE",wheels[wheel_n-1])
                tmp = wheels[wheel_n-1][-1]
                del wheels[wheel_n-1][-1]
                wheels[wheel_n-1] = [tmp] + wheels[wheel_n-1]
                #print("After",wheels[wheel_n-1])
                visited[wheel_n-1] = True
                move(wheel_n-1,1,visited)

    #오른쪽 확인
    if wheel_n==3:
        pass
    else:
        #print("HERE2",wheels[wheel_n+1])
        #print(wheels[wheel_n+1][6]!=right)
        #방향 다르면 반시계 방향 회전
        if visited[wheel_n+1]==False and wheels[wheel_n+1][6]!=right:
            #print("RIGHT")
            #현재 톱니바퀴가 시계방향. 왼쪽 바퀴는 반시계 방향
            #맨 앞 원소 맨 뒤에 넣기
            if dir==1:
                #print("Turn Clock Dir")
                #print("BEFORE",wheels[wheel_n+1])
                tmp = wheels[wheel_n+1][0]
                del wheels[wheel_n+1][0]
                wheels[wheel_n+1].append(tmp)
                #print("After",wheels[wheel_n+1])
                visited[wheel_n+1] = True
                move(wheel_n+1,-1,visited)
            #현재 톱니바퀴가 반시계방향. 왼쪽 바퀴는 시계 방향
            #맨 뒤 원소 맨 앞으로 빼기
            else:
                #print("Turn Reverse Clock Dir")
                #print("BEFORE",wheels[wheel_n+1])
                tmp = wheels[wheel_n+1][-1]
                del wheels[wheel_n+1][-1]
                wheels[wheel_n+1] = [tmp] + wheels[wheel_n+1]
                #print("After",wheels[wheel_n+1])
                visited[wheel_n+1] = True
                move(wheel_n+1,1,visited)


    if visited[wheel_n]!=True:
        #현재 바퀴 회전
        if dir==1:
            tmp = wheels[wheel_n][-1]
            del wheels[wheel_n][-1]
            wheels[wheel_n] = [tmp] + wheels[wheel_n]
        else:
            tmp = wheels[wheel_n][0]
            del wheels[wheel_n][0]
            wheels[wheel_n].append(tmp)

for i in range(K):
    visited = [False for _ in range(4)]
    #print("i",i)
    print("k_methods[0]",k_methods[0])
    move(k_methods[i][0], k_methods[i][1], visited)

    # for i in range(4):
    #     print(*wheels[i])

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