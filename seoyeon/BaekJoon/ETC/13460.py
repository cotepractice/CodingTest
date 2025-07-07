#백준 #14499 주사위 굴리기
#19:26 - 20:11 

#동쪽
def right(i,j):
    return [i,j+1]

#서쪽
def left(i,j):
    return [i,j-1]
#북쪽
def up(i,j):
    return [i-1,j]

#남쪽
def down(i,j):
    return [i+1,j]

#주사위 돌리기
def change_dice(index):
    tmp_dice = [0 for _ in range(6)]
    if index==1:
        tmp_dice[0],tmp_dice[1],tmp_dice[2],tmp_dice[3],tmp_dice[4],tmp_dice[5] = dice[3],dice[1],dice[0],dice[5],dice[4],dice[2]
    elif index==2:
        tmp_dice[0],tmp_dice[1],tmp_dice[2],tmp_dice[3],tmp_dice[4],tmp_dice[5] = dice[2],dice[1],dice[5],dice[0],dice[4],dice[3]
    elif index==3:
        tmp_dice[0],tmp_dice[1],tmp_dice[2],tmp_dice[3],tmp_dice[4],tmp_dice[5] = dice[4],dice[0],dice[2],dice[3],dice[5],dice[1]
    elif index==4:
        tmp_dice[0],tmp_dice[1],tmp_dice[2],tmp_dice[3],tmp_dice[4],tmp_dice[5] = dice[1],dice[5],dice[2],dice[3],dice[0],dice[4]
    return tmp_dice

N,M,x,y,K = map(int,input().split()) #x,y는 주사위 위치
maps = [[0 for _ in range(M)] for _ in range(N)]
for n in range(N):
    maps[n]=list(map(int,input().split()))
k_lst = list(map(int,input().split()))


dice = [0 for _ in range(6)] #1,2,3,4,5,6 순서
answer = []
for k in k_lst:

    move_pos = [x,y]
    tmp_dice = [0 for _ in range(6)]
    if k==1:
        next_lst = right(move_pos[0],move_pos[1])
        tmp_dice = change_dice(1)
        if 0<=next_lst[0]<N and 0<=next_lst[1]<M:
            if maps[next_lst[0]][next_lst[1]]==0:
               maps[next_lst[0]][next_lst[1]]=tmp_dice[5]
            else:
                tmp_dice[5]=maps[next_lst[0]][next_lst[1]]
                maps[next_lst[0]][next_lst[1]]=0
            print(tmp_dice[0])
            move_pos = next_lst
            dice = tmp_dice
    elif k==2:
        next_lst = left(move_pos[0],move_pos[1])
        tmp_dice = change_dice(2)
        if 0<=next_lst[0]<N and 0<=next_lst[1]<M:
            if maps[next_lst[0]][next_lst[1]]==0:
                maps[next_lst[0]][next_lst[1]]=tmp_dice[5]
            else:
                tmp_dice[5]=maps[next_lst[0]][next_lst[1]]
                maps[next_lst[0]][next_lst[1]]=0
            print(tmp_dice[0])
            move_pos = next_lst
            dice = tmp_dice
    elif k==3:
        next_lst = up(move_pos[0],move_pos[1])
        tmp_dice = change_dice(3)
        if 0<=next_lst[0]<N and 0<=next_lst[1]<M:
            if maps[next_lst[0]][next_lst[1]]==0:
                maps[next_lst[0]][next_lst[1]]=tmp_dice[5]
            else:
                tmp_dice[5]=maps[next_lst[0]][next_lst[1]]
                maps[next_lst[0]][next_lst[1]]=0
            print(tmp_dice[0])
            move_pos = next_lst
            dice = tmp_dice
    elif k==4:
        next_lst = down(move_pos[0],move_pos[1])
        tmp_dice = change_dice(4)
        if 0<=next_lst[0]<N and 0<=next_lst[1]<M:
            if maps[next_lst[0]][next_lst[1]]==0:
                maps[next_lst[0]][next_lst[1]]=tmp_dice[5]
            else:
                tmp_dice[5]=maps[next_lst[0]][next_lst[1]]
                maps[next_lst[0]][next_lst[1]]=0
            print(tmp_dice[0])
            move_pos = next_lst
            dice = tmp_dice
    x,y = move_pos[0],move_pos[1]

