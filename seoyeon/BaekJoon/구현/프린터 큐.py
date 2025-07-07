#백준1966 프린터 큐
#구현

from collections import deque

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    
    check = deque(0 for _ in range(n))
    check[m] = 1

    queue = deque(map(int, input().split()))
    cnt = 0

    while True:
        max_v = max(queue)
        v = queue[0]
        c = check[0]

        if (v != max_v):
            word = queue.popleft()
            ch = check.popleft()
            queue.append(word)
            check.append(ch)
        if (v == max_v and c != 1):
            queue.popleft()
            check.popleft()
            cnt += 1
        if (v == max_v and c == 1):
            print(cnt+1)
            break
