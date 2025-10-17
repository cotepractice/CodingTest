#백준 #22251 빌런호석

#N층까지 존재
#K자리의 수 보임 Ex. K=4일때 501호는 0501
#디스플레이 LED 중 최소 1개 최대 P개 반전
#실제로 X층에 멈춰 있음

changes = [[0,4,3,3,4,3,2,3,1,2], [4,0,5,3,2,5,6,1,5,4], [3,5,0,2,5,4,3,4,2,3],
           [3,3,2,0,3,2,3,2,2,1], [4,2,5,3,0,3,4,3,3,2], [3,5,4,2,3,0,1,4,2,1],
           [2,6,3,3,4,1,0,5,1,2], [3,1,4,2,3,4,5,0,4,3], [1,5,2,2,3,2,1,4,0,1], 
           [2,4,3,1,2,1,2,3,1,0]]

#올바른 수가 보여지면서 

N,K,P,X = map(int,input().split())

X = str(X)
origin_n = len(X) #기존 자릿수

#1. str_X 생성: X 자릿수가 K보다 작으면 앞에 0 붙임
str_X = ""
if len(X)<K:
    for _ in range(K-len(X)):
        str_X += "0"
    str_X += X
else:
    str_X = X

#2. N층보다 작은 모든 층수 
possible = []
for i in range(1,N+1):
    possible.append(str(i))

#3. 층수 하나씩 꺼내서 K 자릿수로 최대 P개 바꿔서 가능한지
answer = 0
for p in possible:
    #4. str_p 생성
    # 이때 str_X와 str_p 모두 K 자릿수
    str_p = ""
    if len(p)<K:
        for _ in range(K-len(p)):
            str_p += "0"
        str_p += p
    else:
        str_p = p
    
    #5. str_X에서 str_p로 바꿀 수 있는지 확인
    count=P #바꿀 수 있는 LED 개수 P
    check=False
    #print("str_X",str_X,"str_p",str_p)
    # K 자릿수 모두 탐색
    diff=0
    for idx in range(K):
        if str_X[idx]!=str_p[idx]:
            #print("idx",idx)
            change_n=changes[int(str_X[idx])][int(str_p[idx])] #idx 자리 바꾸는 경우 바뀌는 LED 수
            diff+=change_n
            if change_n<=count:
                count-=change_n
            #바꿔야 하는데 부족해서 못 바꾸는 경우 check=True
            else:
                check=True
                break

    if check==False:
        answer += 1

#자기자신 빼야함 ! 바뀐게 아니므로
print(answer-1)