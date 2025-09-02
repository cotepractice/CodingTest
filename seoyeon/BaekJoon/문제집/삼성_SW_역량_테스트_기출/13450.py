#백준 #13460 구슬탈출2
#구현
#20:30-21:50


N,M = map(int,input().split())
boards = [[] for _ in range(N)] # ".":빈칸, "#":공이이동할 수 없는 장애물 또는 벽, "0":구멍, "R":빨간구슬위치, "B":파란구슬위치

rx,ry,bx,by,hx,hy = -1,-1,-1,-1,-1,-1
for i in range(N):
    lst = list(input())
    boards[i]=lst
    for j in range(M):
        if boards[i][j]=="R":
            rx,ry = i,j
        elif boards[i][j]=="B":
            bx,by = i,j
        elif boards[i][j]=="O":
            hx,hy = i,j

#이동 동작
#왼쪽,오른쪽,위,아래로 기울이기
#최소 몇 번만에 빨간 구슬을 빼낼 수 있는지. 파란 구슬은 빼낼 수 없음
#10번 이하로 빼낼 수 없으면 -1 출력

# R -> 0으로 이동
# 1)빨간 구슬 좌표와 구멍의 좌표 비교
# 2)위치에 따라 상하좌우로 이동

answer = -1
#print("rx,ry,hx,hy",rx,ry,hx,hy)
def up(rx,ry,bx,by,hx,hy):
    result = 0 #0이면 이동은 가능, 1이면 아예 종료, -1이면 아예 이동 불가능
    
    #rx,bx 비교해 더 작은 값 먼저 이동(위로 이동하므로)
    #1)빨간구슬 먼저 이동
    if rx<bx:
        #1-1)빨간구슬 이동
        while True:
            rx -= 1
            if rx==hx and ry==hy:
                result = 1
            if rx<0 or boards[rx][ry]!=".":
                break
            
        #1-2)파란구슬 이동
        while True:
            bx -= 1
            if bx==hx and by==hy:
                result = -1
            if bx<0 or boards[bx][by]!=".":
                break
            

    #2)파란구슬 먼저 이동
    else:
        #2-1)파란구슬 이동
        while True:
            bx -= 1
            if bx==hx and by==hy:
                result = -1
            if bx<0 or boards[bx][by]!=".":
                break
            

        #2-2)빨간구슬 이동
        if result!=-1:
            while True:
                rx -= 1
                if rx==hx and ry==hy:
                    result = 1
                if rx<0 or boards[rx][ry]!=".":
                    break
                

    return [result,rx,ry,bx,by]

def down(rx,ry,bx,by,hx,hy):
    result = 0 #0이면 이동은 가능, 1이면 아예 종료, -1이면 아예 이동 불가능
    
    #rx,bx 비교해 더 작은 값 먼저 이동(위로 이동하므로)
    #1)빨간구슬 먼저 이동
    if rx>bx:
        #1-1)빨간구슬 이동
        while True:
            rx += 1
            if rx==hx and ry==hy:
                result = 1
            if rx>N or boards[rx][ry]!=".":
                break
            
        #1-2)파란구슬 이동
        while True:
            bx += 1
            if bx==hx and by==hy:
                result = -1
            if bx>N or boards[bx][by]!=".":
                break
            

    #2)파란구슬 먼저 이동
    else:
        #2-1)파란구슬 이동
        while True:
            bx += 1
            if bx==hx and by==hy:
                result = -1
            if bx>N or boards[bx][by]!=".":
                break
            

        #2-2)빨간구슬 이동
        if result!=-1:
            while True:
                rx += 1
                if rx==hx and ry==hy:
                    result = 1
                if rx>N or boards[rx][ry]!=".":
                    break
                

    return [result,rx,ry,bx,by]

def left(rx,ry,bx,by,hx,hy):
    result = 0 #0이면 이동은 가능, 1이면 아예 종료, -1이면 아예 이동 불가능
    
    #rx,bx 비교해 더 작은 값 먼저 이동(위로 이동하므로)
    #1)빨간구슬 먼저 이동
    if ry<by:
        #1-1)빨간구슬 이동
        while True:
            ry -= 1
            if rx==hx and ry==hy:
                result = 1
            if ry<0 or boards[rx][ry]!=".":
                break
            
        #1-2)파란구슬 이동
        while True:
            by -= 1
            if bx==hx and by==hy:
                result = -1
            if by<0 or boards[bx][by]!=".":
                break
            

    #2)파란구슬 먼저 이동
    else:
        #2-1)파란구슬 이동
        while True:
            by -= 1
            #print("blue",by)
            if bx==hx and by==hy:
                result = -1
            if by<0 or boards[bx][by]!=".":
                break

        #2-2)빨간구슬 이동
        if result!=-1:
            #print("ddddddd")
            while True:
                ry -= 1
                if rx==hx and ry==hy:
                    result = 1
                if ry<0 or boards[rx][ry]!=".":
                    break

    #print("result",result,rx,ry,bx,by)
    return [result,rx,ry,bx,by]

def right(rx,ry,bx,by,hx,hy):

    result = 0 #0이면 이동은 가능, 1이면 아예 종료, -1이면 아예 이동 불가능
    
    #rx,bx 비교해 더 작은 값 먼저 이동(위로 이동하므로)
    #1)빨간구슬 먼저 이동
    if ry>by:
        #1-1)빨간구슬 이동
        while True:
            ry += 1
            if rx==hx and ry==hy:
                result = 1
            if ry>N or boards[rx][ry]!=".":
                break
        #1-2)파란구슬 이동
        while True:
            by += 1
            if bx==hx and by==hy:
                result = -1
            if by>N or boards[bx][by]!=".":
                break

    #2)파란구슬 먼저 이동
    else:
        #2-1)파란구슬 이동
        while True:
            by += 1
            if bx==hx and by==hy:
                result = -1
            if by>N or boards[bx][by]!=".":
                break

        #2-2)빨간구슬 이동
        if result!=-1:
            #print("HHHHHHHHHHHDJFHDJFJD")
            while True:
                ry += 1
                #print("INSIDE rxry",rx,ry,"hyhy",hx,hy)
                if rx==hx and ry==hy:
                    #print("WOWOWOOWOWOWO")
                    result = 1
                if ry>N or boards[rx][ry]!=".":
                    break

    return [result,rx,ry,bx,by]

def dfs(rx,ry,bx,by,hx,hy,cnt):
    global answer

    if cnt==2:
        return

    #위치에 따라 구멍좌표 -> 빨간구슬 좌표로 이동
    #위로 이동
    if rx>hx:
        #print("up","cnt",cnt,"rx,ry",rx,ry)
        lst = up(rx,ry,bx,by,hx,hy)
        #빨간색만 들어간 경우
        if lst[0]==1:
            answer = cnt
            return
        #파란색에는 안 들어간 경우, 다음 이어가도 됨
        elif lst[0]==0:
            rxx,ryy, bxx,byy = lst[1],lst[2],lst[3],lst[4]
            dfs(rxx,ryy,bxx,byy,hx,hy,cnt+1)
    #아래로 이동
    if rx<hx:
        #print("down","cnt",cnt,"rx,ry",rx,ry)
        lst = down(rx,ry,bx,by,hx,hy)
        #빨간색만 들어간 경우
        if lst[0]==1:
            answer = cnt
            return
        #파란색에는 안 들어간 경우, 다음 이어가도 됨
        elif lst[0]==0:
            rxx,ryy, bxx,byy = lst[1],lst[2],lst[3],lst[4]
            dfs(rxx,ryy,bxx,byy,hx,hy,cnt+1)
    #왼쪽으로 이동
    if ry>hy:
        #print("left","cnt",cnt,"rx,ry",rx,ry)
        lst = left(rx,ry,bx,by,hx,hy)
        #빨간색만 들어간 경우
        if lst[0]==1:
            answer = cnt
            return
        #파란색에는 안 들어간 경우, 다음 이어가도 됨
        elif lst[0]==0:
            rxx,ryy, bxx,byy = lst[1],lst[2],lst[3],lst[4]
            dfs(rxx,ryy,bxx,byy,hx,hy,cnt+1)
    #오른쪽으로 이동
    if ry<hy:
        #print("right","cnt",cnt,"rx,ry",rx,ry)
        lst = right(rx,ry,bx,by,hx,hy)
        #빨간색만 들어간 경우
        if lst[0]==1:
            answer = cnt
            return
        #파란색에는 안 들어간 경우, 다음 이어가도 됨
        elif lst[0]==0:
            rxx,ryy, bxx,byy = lst[1],lst[2],lst[3],lst[4]
            dfs(rxx,ryy,bxx,byy,hx,hy,cnt+1)

dfs(rx,ry,bx,by,hx,hy,0)
print(answer+1)
