#https://school.programmers.co.kr/learn/courses/30/lessons/340212
#[PCCP]2번/퍼즐 게임 챌린지

#시간복잡도 O(max(diffs) * N) = O(100,000 * 300,000) -> 시간초과발생
#n개의 퍼즐 풀어야 함
#숙련도에 따라 퍼즐 풀 때 틀리는 횟수가 바뀌게 됨
#diff:퍼즐 난이도, time_cur:현재 퍼즐 소요 시간, time_prev:이전 퍼즐 소요시간, level:숙련도

#로직
# if diff<=level: time_cur만큼의 시간 사용
# if diff>level: diff-level 번 틀림
#   ((diff-level) + time_prev ) * time_cur + time_cur
#    현재 퍼즐 틀릴 때마다 소요되는 시간 + 이전 퍼즐 다시 풀기 (절대 틀리지 않음)

#전체 제한 시간 limit 정해져 있음
#제한 시간 내 퍼즐을 모두 해결하기 위한 숙련도의 최솟값 구하기


#1. 46.2/100

import sys

input = sys.stdin.readline

answer = 0
def solv(N,diffs,times,limit,level):
    global answer
    
    ans = 0
    
    #로직
    for i in range(N):
        
        #diff<=level인 경우
        if diffs[i]<=level:
            ans += times[i]
        #diff>level인 경우
        #diffs[0]이 항상 1이기 때문에 가능
        else:
            ans += (times[i-1] + times[i]) * (diffs[i]-level) + times[i]

    if ans<=limit:
        return True
    
    return False
    
def solution(diffs, times, limit):
    global answer
    
    #최대 숙련도는 diffs
    max_level = max(diffs)
    N = len(diffs)
    #숙련도
    for level in range(1,max_level+1):
        ans = solv(N,diffs, times, limit, level)
        if ans:
            answer = level
            break
    
    return answer

#2. 이분탐색. 95.1/100

import sys

input = sys.stdin.readline

def solv(N,diffs,times,limit,level):

    ans = 0
    
    #로직
    for i in range(N):
        
        #1. diff<=level인 경우, dp 업데이트  
        if diffs[i]<=level:
            ans += times[i]
        #2. diff>level인 경우
        #diffs[0]이 항상 1이기 때문에 가능
        else:
            ans += (times[i-1] + times[i]) * (diffs[i]-level) + times[i]
        
        #3. 조기 탈출. for문을 다 돌지 않아도 limit을 초과하는 경우 조기 종료
        if ans>limit:
            return float("inf")
            
    return level
    
#이분탐색
def solution(diffs, times, limit):
    answer = float("inf")
    
    #최대 숙련도는 diffs
    left = 1
    right = max(diffs)
    N = len(diffs)
    
    while left<=right:
        #mid가 level 의미
        mid = (left+right)//2
        
        #종결조건
        if mid==1:
            break
        
        ans = solv(N,diffs,times,limit,mid)
        #print("ans",ans)
        #level이 answer보다 작은 경우 최솟값 탐색: 더 작은 값 탐색
        if ans<answer:
            answer=ans
            right = mid-1
        #level이 answer보다 큰 경우 level 높이기
        elif ans==float("inf"):  
            left = mid+1
        #ans==answer인 경우는 더 진행할 필요 없음
        elif ans==answer:
            break 
        
    return answer

#3. 2에서 if mid==1 코드 제거

import sys

input = sys.stdin.readline

def solv(N,diffs,times,limit,level):

    ans = 0
    
    #로직
    for i in range(N):
        
        #1. diff<=level인 경우, dp 업데이트  
        if diffs[i]<=level:
            ans += times[i]
        #2. diff>level인 경우
        #diffs[0]이 항상 1이기 때문에 가능
        else:
            ans += (times[i-1] + times[i]) * (diffs[i]-level) + times[i]
        
        #3. 조기 탈출. for문을 다 돌지 않아도 limit을 초과하는 경우 조기 종료
        if ans>limit:
            return float("inf")
            
    return level
    
#이분탐색
def solution(diffs, times, limit):
    answer = max(diffs)
    
    #최대 숙련도는 diffs
    left = 1
    right = max(diffs)
    N = len(diffs)
    
    while left<=right:
        #mid가 level 의미
        mid = (left+right)//2
        
        ans = solv(N,diffs,times,limit,mid)
        #print("ans",ans)
        #level이 answer보다 작은 경우 최솟값 탐색: 더 작은 값 탐색
        if ans<answer:
            answer=ans
            right = mid-1
        #level이 answer보다 큰 경우 level 높이기
        else:
            left = mid+1
        
        
    return answer