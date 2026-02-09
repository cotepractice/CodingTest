p, m = map(int, input().split())
people = []
for i in range(p):
    lv, id = input().split()
    people.append([int(lv), id])

rooms = []

for lv, id in people:
    flag = False
    for i in range(len(rooms)):
        if len(rooms[i][1]) == m:
            continue
        
        # 들어갈 수 있는 방이 있으면 입장
        if rooms[i][0] - 10 <= lv <= rooms[i][0] + 10:
            flag = True
            rooms[i][1].append([lv, id])
            break
            
    # 대기방에 들어 갈 수 없으면 새로운 방 생성
    if not flag:
        rooms.append([lv, [[lv, id]]])

# 방이 생성된 시간 순서로 출력
for i in range(len(rooms)):
    if len(rooms[i][1]) == m:
        print('Started!')
        tmp_ids = sorted(rooms[i][1], key=lambda x: x[1])
        for j in range(m):
            print(*tmp_ids[j])
    else:
        print('Waiting!')
        tmp_ids = sorted(rooms[i][1], key=lambda x: x[1])
        for j in range(len(tmp_ids)):
            print(*tmp_ids[j])