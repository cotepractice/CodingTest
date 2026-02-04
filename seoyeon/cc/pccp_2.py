#https://school.programmers.co.kr/learn/courses/30/lessons/340212
#[PCCP]2번/퍼즐 게임 챌린지

#1. 46.2/100
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