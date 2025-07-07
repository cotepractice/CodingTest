from itertools import combinations

def back_tracking(round):
    global answer
    #모든 라운드가 끝났을 때 승,무,패 횟수 모두 0이면 answer=1
    if round==15:
        answer=1
        #승,무,패 중 하나라도 0이 아니면 answer=0
        for i in res:
            if i.count(0)!=3:
                answer=0
                break
        return
    #t1,t2는 팀 의미
    t1,t2=game[round]
    
    #x,y는 승,무,패를 결정하는 인덱스
    for x,y in ((0,2),(1,1),(2,0)):
        if res[t1][x]>0 and res[t2][y]>0:
            res[t1][x]-=1 #t1
            res[t2][y]-=1 #t2
            back_tracking(round+1)
            res[t1][x]+=1 #다시복구
            res[t2][y]+=1

result=[]
game=list(combinations(range(6),2)) #경기 조합 game=[(0,1),(0,2),...]
for _ in range(4):
    temp=list(map(int,input().split()))
    res=[temp[i:i+3] for i in range(0,16,3)] #res=[[5,0,0],[0,5,0],...]. 팀0은 5승0무0패,팀1은0승5무0패
    answer=0
    back_tracking(0)
    result.append(answer)
print(*result)