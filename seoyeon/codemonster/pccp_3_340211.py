# [PCCP 기출문제 3번] 충돌위험 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/340211

#운송 시스템 규칙
# 1. [r,c] 2차원 좌표로 나타낼 수 있는 n개의 포인트 존재
# 2. 로봇마다 정해진 운송 경로 존재. 운송 경로는 m개 포인트로 구성되고 로봇은 첫 포인트에서 시작해 할당된 포인트를 순서대로 방문
# 3. 운송 시스템에 사용되는 로봇은 x대. 모든 로봇은 0초에 동시에 출발. 1초마다 r 좌표와 c 좌표 중 하나가 1만큼 감소 or 증가
# 4. 다음 포인트 이동 시 최단 경로가 여러 개인 경우 r 좌표가 변하는 이동을 먼저 
# 같은 좌표에 로봇이 2대 이상 모인다면 "충돌할 가능성이 있는 위험 상황"으로 판단
# 위험 상황이 총 몇 번 발생하는지 탐색

def move(points,route):
    
    #경로에 따라 시작, 종료 시점 다름
    #t를 통해 시간에 따라 겹치는지 확인
    t = 0
    all_lst = []
    #print("move")
    for r in range(len(route)-1):
        #print("Here is r",r, route)
        start=points[route[r]-1]
        end=points[route[r+1]-1]
        
        start_x, start_y = start[0]-1,start[1]-1
        end_x, end_y = end[0]-1,end[1]-1
        
        if r==0:
            all_lst.append([start_x,start_y,0])
        #move_lst = [[start_x,start_y,0]]
        
        #r 먼저 이동
        while start_x!=end_x:
            if start_x<end_x:
                start_x+=1
            else:
                start_x-=1
            t += 1
            all_lst.append([start_x,start_y,t])
            

        #c 이동
        while start_y!=end_y:
            if start_y<end_y:
                start_y+=1
            else:
                start_y-=1
            t += 1
            all_lst.append([start_x,start_y,t])
        #print("move_lst",move_lst)

    #print("all_lst",all_lst)
    # for kk in range(len(all_lst)):
    #     print(all_lst[kk])
    
    return all_lst

def check(lst):
    answer = 0
    buckets = set() #경로 저장
    check_buckets = set() #위험 상황 발생 체크 여부
    #print("lst",lst)
    for x,y,t in lst:
        #print("current",(x,y,t))
        if (x,y,t) not in buckets:
            buckets.add((x,y,t))
            continue
        elif (x,y,t) not in check_buckets:
            #print("here",(x,y,t))
            check_buckets.add((x,y,t))
            answer += 1
    
    return answer

    

#points: , routes: 운송경로
def solution(points, routes):
    all_lst = []
    #로봇마다의 이동 경로 
    for route in routes:
        move_lst = move(points,route)
        all_lst.extend(move_lst)
    
    answer = check(all_lst)
    #print("answer",answer)
    return answer


solution([[2, 2], [2, 3], [2, 7], [6, 6], [5, 2]], [[2, 3, 4, 5], [1, 3, 4, 5]])