#백준10828 스택
#자료구조: stack => deque
#deque 사용해 시간 줄이기
#input = sys.stdin.readline
#m=input().strip() 하지 않으면 시간 초과 발생 
#sys.stdin.readline은 입력마다 데이터를 버퍼에 저장하고, input()은 엔터가 입력될 때까지 기다렸다가 받아서 유니코드로 변환해 버퍼에 저장
#strip()은 개행 제거를 위해 사용
#아래를 보면 python의 input()의 속도가 매우 느림을 알 수 있음 <https://www.acmicpc.net/blog/view/56>
#추가적으로 삼성코테 기준으로 sys모듈은 제한이 있고, queue와 deque는 사용 가능

from collections import deque
import sys

n = int(input())

q = deque()

for i in range(n):
    input = sys.stdin.readline
    m = input().strip()
    if (m[:4] == 'push'):
        q.append(int(m[5:]))
    elif (m == 'top'):
        if not q:
            print(-1)
        else:
            print(q[-1])
    elif (m == 'pop'):
        if not q:
            print(-1)
        else:
            print(q.pop())
    elif (m == 'size'):
        print(len(q))
    elif (m == 'empty'):
        if not q:
            print(1)
        else:
            print(0)
