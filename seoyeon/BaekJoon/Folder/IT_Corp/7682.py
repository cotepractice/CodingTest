#백준 #7682 틱택토
#22:20-23:35

#valid 조건
#X 또는 O가 가로,세로,대각선 중 하나 성공하면 즉시 게임 종료
#1)X가 성공해 종료하는 경우, X개수가 O개수보다 1 커야함 -> valid
#2)O가 성공해 종료하는 경우, X개수와 O개수가 같아야 함 -> valid
#board가 다 찬 경우, valid
# X개수가 O 개수보다 1 커야 함

while True:

    sentence = input()

    #종결조건
    if sentence == "end":
        break
    
    boards = [[-1,-1,-1] for _ in range(3)]

    #1. boards 정의
    for i in range(9):
        x=i//3
        y=i%3

        boards[x][y]=sentence[i]

    #2. 가로,세로,대각선 개수 카운트
    # X 기준으로!
    o_cnt=0 
    x_cnt=0

    row_x = [0,0,0]
    column_x = [0,0,0]
    cross_x = [0,0] #[왼쪽위에서 오른쪽아래 대각선, 오른쪽위에서 왼쪽아래 대각선]

    row_o = [0,0,0]
    column_o = [0,0,0]
    cross_o = [0,0]

    for i in range(3):
        for j in range(3):
            #X 카운트
            if boards[i][j]=="X":
                row_x[i]+=1
                column_x[j]+=1
                x_cnt+=1
                if i==j==1:
                    cross_x[0]+=1
                    cross_x[1]+=1
                    continue
                if i==j:
                    cross_x[0]+=1
                if i==2-j:
                    cross_x[1]+=1
            #O 카운트
            elif boards[i][j]=="O":
                row_o[i]+=1
                column_o[j]+=1
                o_cnt+=1
                if i==j==1:
                    cross_o[0]+=1
                    cross_o[1]+=1
                    continue
                if i==j:
                    cross_o[0]+=1
                if i==2-j:
                    cross_o[1]+=1
            

    #3. 빙고 확인
    # row, column, cross 모두 확인
    X_cnt = 0 #빙고개수(x_cnt와 다름)
    O_cnt = 0 #빙고개수(o_cnr와 다름)
    for i in range(3):
        if row_o[i]==3:
            O_cnt+=1
        if row_x[i]==3:
            X_cnt+=1
    for i in range(3):
        if column_o[i]==3:
            O_cnt+=1
        if column_x[i]==3:
            X_cnt+=1
    for i in range(2):
        if cross_o[i]==3:
            O_cnt+=1
        if cross_x[i]==3:
            X_cnt+=1

    #둘 다 빙고인 경우, invalid
    if X_cnt>=1 and O_cnt>=1:
        print("invalid")
        continue
    
    #1)valid인 경우1
    # X_cnt 빙고일 때 x_cnt=o_cnt+1
    if X_cnt>=1:
        if x_cnt==o_cnt+1:
            print("valid")
            continue
    #O_cnt 빙고일 때 x_cnt=o_cnt
    elif O_cnt>=1:
        if x_cnt==o_cnt:
            print("valid")
            continue
    
    #2)valid인 경우2
    # 둘 다 빙고 아닐 때 보드가 가득차면 valid
    else:
        if x_cnt+o_cnt==9 and x_cnt==o_cnt+1:
            print("valid")
            continue
    
    #그외 모두 invalid
    print("invalid")



#valid 조건
#X 또는 O가 가로,세로,대각선 중 하나 성공하면 즉시 게임 종료
#1)X가 성공해 종료하는 경우, X개수가 O개수보다 1 커야함 -> valid
#2)O가 성공해 종료하는 경우, X개수와 O개수가 같아야 함 -> valid
#board가 다 찬 경우, valid
# X개수가 O 개수보다 1 커야 함