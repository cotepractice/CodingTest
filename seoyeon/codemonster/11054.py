#백준 #11054 가장 긴 바이토닉 부분 수열

N = int(input())
A = list(map(int,input().split()))

max_n = -1
max_idx = []

#가장 큰 수의 인덱스 모두 탐색
#정답은 이중에 있음
for a in range(len(A)):
    if A[a]>max_n:
        max_n = A[a]
        max_idx = [a]
    elif A[a]==max_n:
        max_idx.append(a)

#1)처음 무조건 포함하는 경우
# 입력: 가장 작은 수(시작하는 수), 바이토닉 수열, 
# 변함: 시작하는 수
  # 만약 다음 수가 본인보다 크고 max_n보다 작은 경우 넣을지 말지 선택
  # 본인보다 작으면 그 수부터 시작할지 말지 선택
# 변하지 않음


left_max, right_max = -1,-1


#lst는 오름차순
#A는 인덱스 저장 리스트
def backtracking_left(end_idx,current_idx,lst):
    global left_max

    #print("current_idx",current_idx)
    #print("lst",lst)
    
    #종결 조건
    if current_idx+1==end_idx:
        #print("here")
        #print("LEFT",lst)
        left_max = max(left_max, len(lst))
        return

    first = A[lst[0]] #first는 가장 작은 수
    last = A[lst[-1]] #last는 list 중 가장 큰 수
    #print("HERE1",first,last)

    #1.다음 위치 인덱스 수가 최고 숫자와 동일한 경우 넣지 않음
    if A[current_idx+1]==A[end_idx] or A[current_idx+1]==first or A[current_idx+1]==last:
        backtracking_left(end_idx,current_idx+1,lst)

    #2.가장 작은 수 < 다음 위치 인덱스 수 => 넣거나 말거나
    if A[current_idx+1]>last:
        #print("HRE2")
        backtracking_left(end_idx,current_idx+1,lst+[current_idx+1]) #넣기
        backtracking_left(end_idx,current_idx+1,lst) #넣지않기

    #print("HRE3")
    #3.first보다 작은 경우, 무시하거나 해당 인덱스(current_idx+1)부터 다시 시작
    if A[current_idx+1]<first:
        #print("HERE4",first,A[current_idx])
        backtracking_left(end_idx,current_idx+1,lst) #해당 수만 넣지 않기
        backtracking_left(end_idx,current_idx+1,[current_idx+1]) #아예 바꾸기
        

def backtracking_right(end_idx,current_idx,lst):
    global right_max

    #종결 조건
    if current_idx+1==end_idx:
        #print("RIHGT",lst)
        right_max = max(right_max, len(lst))
        return

    first = A[lst[0]] #first는 가장 큰 수
    last = A[lst[-1]] #last는 list 중 가장 작은 수

    #1.다음 위치 인덱스 수가 최고 숫자와 동일한 경우 넣지 않음
    if A[current_idx+1]==first or A[current_idx+1]==first or A[current_idx+1]==last:
        backtracking_right(end_idx,current_idx+1,lst)

    #2.다음 위치 인덱스 수 < 가장 작은 수 => 넣거나 말거나
    if A[current_idx+1]<last:
        #print("HRE2")
        backtracking_right(end_idx,current_idx+1,lst+[current_idx+1]) #넣기
        backtracking_right(end_idx,current_idx+1,lst) #넣지않기
    
    #3.first보다 작은 경우, 무시하거나 해당 인덱스(current_idx+1)부터 다시 시작
    if A[current_idx+1]>first:
        #print("HERE4",first,A[current_idx])
        backtracking_right(end_idx,current_idx+1,[current_idx+1]) #아예 바꾸기
        backtracking_right(end_idx,current_idx+1,lst) #해당 수만 넣지 않기

result = 0
#하나씩 선택해 최대 수열의 길이 출력
for m_idx in max_idx:
    #print("START")
    #print("m_idx",m_idx)
    left_max, right_max = 0,0
    backtracking_left(m_idx, 0, [0])
    backtracking_right(N, m_idx, [m_idx])
    #print("left_max",left_max)
    #print("right_max",right_max)
    result = max(result, left_max+right_max)

print(result)