import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline().split())

table = [sys.stdin.readline().split() for _ in range(N)]
final = [[0] * M for _ in range(N)]  # 빈 이차원 배열 생성 N * M 사이즈
deq_box = deque()  # 빈 데크 박스 생성

# 몇 겺으로 되어 있는지 -> 결국 몇 번 루프를 돌아야 하는지
loops = min(N, M) // 2  # 가장 작은 수의 절반 만큼 겹이 쌓임
for i in range(loops):
    deq_box.clear()
    # 돌리기 전의 1차원 deq 생성 - 위 오른쪽 아래 왼쪽 순서로 넣어준다
    deq_box.extend(table[i][i : M - i])  # 위
    deq_box.extend([row[M - i - 1] for row in table[i + 1 : N - i - 1]])  # 오
    deq_box.extend(table[N - i - 1][i : M - i][::-1])  # 아래
    deq_box.extend([row[i] for row in table[i + 1 : N - i - 1]][::-1])  # 왼

    deq_box.rotate(-R)

    # 생성된 deq_box 의 맨 처음 거를 빼서 final 에 하나씩 담는다 - 위 오른쪽 아래 왼쪽 순서로
    # i 가 0 이면..
    for j in range(i, M - i):  # 위 (0,0)(0,1)(0,M)
        final[i][j] = deq_box.popleft()
    for j in range(i + 1, N - i - 1):  # 오른쪽 (1, 오른쪽 맨 끝)
        final[j][M - i - 1] = deq_box.popleft()
    for j in range(M - i - 1, i - 1, -1):  # 아래 (오른쪽 맨 아래,,)
        final[N - i - 1][j] = deq_box.popleft()
    for j in range(N - i - 2, i, -1):
        final[j][i] = deq_box.popleft()

for i in final:
    print(*i)