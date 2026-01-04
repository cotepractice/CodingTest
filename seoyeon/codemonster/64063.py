#프로그래머스 #64063 호텔방배정

#1. 정확성 78.8, 효율성 0
def solution(k, room_number):
    N = len(room_number)
    answer = [0 for _ in range(N)]
    
    rooms = [i for i in range(1,k+1)]
    visited = set()
    
    for idx,r in enumerate(room_number):
        #배정할 수 있는 경우 
        if r not in visited:
            visited.add(r)
            answer[idx]=r
        else:
            for next in range(r+1,k+1):
                if next not in visited:
                    visited.add(next)
                    answer[idx]=next
                    break
    print(answer)
    
    return answer

#2. 정확성+효율성 100
import sys
sys.setrecursionlimit(10000) # 재귀 허용깊이 임의로 지정

def solution(k, room_number):
    rooms = dict() # {방번호: 바로 다음 빈방 번호}
    for num in room_number:
        chk_in = find_emptyroom(num,rooms)
    return list(rooms.keys())

def find_emptyroom(chk, rooms):
    #빈 방인 경우
    if chk not in rooms:
        rooms[chk] = chk+1 
        return chk 
    #빈 방이 아닌 경우 재귀로 탐색
    empty = find_emptyroom(rooms[chk], rooms) # 재귀함수 호출
    rooms[chk] = empty+1 # (배정된 방+1)을 부모노드로 변경
    return empty # 새로 찾은 빈 방
