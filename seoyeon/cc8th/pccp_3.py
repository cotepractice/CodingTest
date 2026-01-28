#https://school.programmers.co.kr/learn/courses/30/lessons/340211?language=python3

#1. 실패 코드
# [r,c]와 같은 좌표가 n개 존재. 각 포인트는 1~n까지 서로 다른 번호 가짐
# 로봇마다 정해진 경로 존재. 경로는 m개의 포인트로 구성되고, 로봇은 첫 포인트에서 시작해 순서대로 방문
# 운송 시스템에서 사용되는 로봇은 x대. 모든 로봇은 0초에 동시에 출발
#  1초마다 r 또는 c 중 하나가 1만큼 감소하거나 증가한 좌표로 이동 가능
# 이동 시 항상 최단 경로로 이동하며, 최단 경로가 여러 개인 경우 r 좌표가 먼저 변함
# 마지막 포인트에 도착한 로봇은 운송을 마치고 물류 센터를 벗어남

# 위 상황에서 같은 좌표에 로봇이 2개 이상 모이는 경우 충돌

# 현재 설정대로 로봇이 움직일 때 충돌 상황이 몇 번 일어나는지 알고 싶음
#  만약 어떤 시간에 여러 좌표에 충돌이 발생한다면 횟수 모두 더함

#입력
## points:운송포인트 n개 좌표 , routes: 운송 경로를 담은 배열

# dp로 풀려고 하였으나 시간초과 발생할 것 같아 list로 처리
from collections import deque,Counter

answer = 0
check = list()

# r좌표 먼저 이동 -> c좌표 이동
def dfs(dp,start,end,cnt):
    global check,answer
    
    #r 먼저 맞추기
    start_x,start_y = start[0],start[1]
    end_x,end_y = end[0],end[1]
    check.append((start_x,start_y,0))
    dp[start_x][start_y]=0
    #print("start",start_x,start_y,"end",end_x,end_y)
    
    cnt = 0
    while start_x!=end_x:
        #print("A",start_x,start_y,dp[start_x][start_y])
        if start_x<end_x:
            start_x+=1
            dp[start_x][start_y]=cnt+1

        else:
            start_x-=1
            dp[start_x][start_y]=cnt+1
            
        check.append((start_x,start_y,cnt+1))

        cnt+=1
        
    #c 맞추기
    while start_y!=end_y:
        #print("B",start_x,start_y,cnt)
        if start_y<end_y:
            start_y+=1
            dp[start_x][start_y]=cnt+1
        else:
            start_y-=1
            dp[start_x][start_y]=cnt+1
        
        check.append((start_x,start_y,cnt+1))
        
        cnt+=1
    #check.append((start_x,start_y,cnt+1))
    #print("Check",check,"answer",answer)
    return dp

def solution(points, routes):
    answer = 0
    
    #로봇의 수만큼
    #일단 10*10으로 진행 추후 100*100으로 업데이트
    dp = [[[float("inf") for _ in range(100)] for _ in range(100)] for _ in range(len(routes))]
    
    #1.routes를 통해 시작, 종료 좌표 계산
    for idx,route in enumerate(routes):
        start_idx,end_idx = route[0],route[1]
        start_idx-=1
        end_idx-=1
        
        start_x,start_y=points[start_idx][0]-1, points[start_idx][1]-1
        end_x,end_y=points[end_idx][0]-1, points[end_idx][1]-1
        
        #2. 시작 좌표에서 종료 좌표로 이동하는 거리 bfs로 계산해 dp 저장
        #print("idx",idx)
        dfs(dp[idx],[start_x,start_y],[end_x,end_y],0)
        #print("idx",idx)
        #print(dp[idx])
    
    #3. dp[val]에서 로봇의 개수만큼 돌며 같은 값을 가지는 dp 존재하는지 확인
    #print(check)
    counter = Counter(check)
    #print("counter",counter)
    
    for pos,count in counter.items():
        if count>=2:
            answer+=1
                    
    
    return answer

#2. 