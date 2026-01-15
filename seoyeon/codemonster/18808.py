#백준 #18808 스티커 붙이기

import sys
input = sys.stdin.readline

# 스티커 90도 회전
def rotate_by_90(sticker_board):
    r, c = len(sticker_board), len(sticker_board[0])
    rotated_sticker_board = [[0] * r for _ in range(c)]
    for i in range(c):
        for j in range(r):
            rotated_sticker_board[i][j] = sticker_board[r-j-1][i]
    
    return rotated_sticker_board

# 현재 위치에 붙일 수 있는지 없는지 확인
def is_attachable(x, y, sticker_board):
    r, c = len(sticker_board), len(sticker_board[0])
    for i in range(r):
        for j in range(c):
            if sticker_board[i][j] == 1 and notebook[x+i][y+j] == 1:
                return False
    
    return True

# 현재 위치에 스티커 붙임
def attach(x, y, sticker_board):
    r, c = len(sticker_board), len(sticker_board[0])

    for i in range(r):
        for j in range(c):
            if sticker_board[i][j] == 1:
                notebook[x+i][y+j] = 1


if __name__ == '__main__':
    n, m, k = map(int, input().split())
    notebook = [[0] * m for _ in range(n)]
    stickers = [{} for _ in range(n)]
	
    # 스티커 정보는 딕셔너리로 관리
    for i in range(k):
        r, c = map(int, input().split())
        stickers[i]['r'], stickers[i]['c'] = r, c
        stickers[i]['sticker_board'] = [list(map(int, input().split())) for _ in range(r)]

    for i in range(k):
        s_n, s_m = stickers[i]['r'], stickers[i]['c']
        current_sticker = stickers[i]['sticker_board']
        rotation_cnt = 0

        while rotation_cnt < 4:
        	# 현재 스티커의 크기가 노트북 범위를 벗어나면 회전
            if s_n > n or s_m > m:
                s_n, s_m, current_sticker = s_m, s_n, rotate_by_90(current_sticker)

                continue
            
            # 벗어나지 않는다면 붙일 수 있는지 확인
            is_attached = False
            
            for i in range(n - s_n + 1):
                for j in range(m - s_m + 1):
                    if is_attachable(i, j, current_sticker):
                        attach(i, j, current_sticker)
                        is_attached = True
                        break
                
                # 두 번째 for문 break
                if is_attached:
                    break
                    
            # while문 break
            if is_attached:
                break
            
            else:
                s_n, s_m, current_sticker = s_m, s_n, rotate_by_90(current_sticker)
                rotation_cnt += 1

    ans = 0
    for i in range(n):
        for j in range(m):
            if notebook[i][j] == 1:
                ans += 1

    print(ans)