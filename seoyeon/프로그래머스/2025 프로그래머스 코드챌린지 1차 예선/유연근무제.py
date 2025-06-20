#schedules:출근 희망 시각, timelogs: 직원의 일주일 출근 시간, startday: 이벤트 시작 요일(1:월,2:화,..,7:일)
def solution(schedules, timelogs, startday):
    answer = 0
    
    n = len(schedules)
    check_time = []
    
    #1.check_time 설정
    for s in schedules:
        s += 10
        check_time.append(s)
    print(check_time)
    
    #2.토요일, 일요일은 필요 X
    except_day = {}
    if startday==1:
        except_day={5,6} #5,6번째 인덱스는 신경 X. for m in range(len(timelogs))에 사용하므로 0~6
    elif startday==2:
        except_day={4,5}
    elif startday==3:
        except_day={3,4}
    elif startday==4:
        except_day={2,3}
    elif startday==5:
        except_day={1,2}
    elif startday==6:
        except_day={0,1}
    elif startday==7:
        except_day=[0,6]
        
    
    #3.check_time 이내에 도착했는지 확인
    for m in range(len(timelogs)):
        check = 0
        for k in range(7):
            if k in except_day:
                continue
            if timelogs[m][k]<=check_time[m]:
                check += 1
        if check==5:
            answer += 1
        
    
    return answer