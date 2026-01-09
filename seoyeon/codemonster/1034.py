#배ㄱ준 #1034 램프

#열 관련
# 각 열의 아래에는 스위치가 달려있는데, 이 스위치를 누를 때마다 그 열에 있는 램프의 상태가 바뀜
# 켜저있는 램프는 꺼지고, 꺼져있는 램프는 켜짐
#행 관련
# 램프가 모두 켜져 있을 때 그 행은 켜져있다고 함

#스위치를 K 번 누름. 서로 다른 스위치 K개를 누르지 않아도 됨
# 켜져 있는 행을 최대로 하려고 함

N,M = map(int,input().split())
lamps = [[0 for _ in range(M)] for _ in range(N)]

for n in range(N):
    lamps[n] = list(input())

K = int(input()) #스위치 누르는 횟수
max_cnt = 0

#한 행에 0의 개수 카운트
lamp_off_cnt = [0] * N
for row in range(N):
    off_cnt = 0
    for col in range(M):
        if lamps[row][col] == '0':
            off_cnt += 1
    lamp_off_cnt[row] = off_cnt

#자기자신 제외하고 가능한 경우의 수 
def get_same_row_cnt(row):
    result = 0
    for another_row in range(N):
        if another_row != row and lamps[another_row] == lamps[row]:
            result += 1
    return result

answer = 0
#lamp_off_cnt를 돌며 K보다 작으면서 동시에 짝홀수가 동일한 경우에만 K번 눌러 스위치 소모 가능
for row in range(N):
    if lamp_off_cnt[row] <= K and lamp_off_cnt[row] % 2 == K % 2:
        #자기자신과 처음부터 자기자신과 동일한 row의 수 탐색해 answer 업데이트
        answer = max(answer, 1 + get_same_row_cnt(row))

print(answer)

#아래와 같이 해결하는 경우 시간초과 발생
# can_k = K%M
# if M!=1 and can_k==0:
#     can_k=M

# answer = 0

# def change(lst,idx):
#     for i in range(N):
#         if lst[i][idx]=="0":
#             lst[i][idx]=1
#         else:
#             lst[i][idx]=0
#     #print("lst",lst)
#     return lst

# def check(lst):
#     ans = 0
#     for i in range(N):
#         current = 0
#         for j in range(M):
#             current += int(lst[i][j])
#         if current==M:
#             #print("i,j",i,j)
#             ans += 1
#     return ans

# #print("can",can_k)
# def solv(lst,idx,change_cnt):
#     global answer
#     #종결조건
#     if change_cnt==can_k:
#         answer = max(answer, check(lst))
#         return
#     if idx>=M:
#         return
#     #1) 누르지 않는 경우
#     solv(lst,idx+1,change_cnt)

#     #2) 누르는 경우
#     tmp_lst = change(copy.deepcopy(lst),idx)
#     solv(copy.deepcopy(tmp_lst),idx,change_cnt+1)
#     solv(copy.deepcopy(tmp_lst),idx+1,change_cnt+1)

# solv(lights,0,0)
# print(answer)