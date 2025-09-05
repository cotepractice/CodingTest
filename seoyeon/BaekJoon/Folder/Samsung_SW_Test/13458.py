#백준 #13458 시험 감독
#2:28-2:40

N = int(input()) #N:시험장
A = list(map(int,input().split())) #A:각 시험장의 응시자 수
B,C = map(int,input().split()) #B:총감독이 감시할 수 있는 응시자 수, C:부감독이 감시할 수 있는 응시자 수

#총감독과 부감독
#총감독은 감시할 수 있는 응시자 수가 B명, 부감독은 감시할 수 있는 응시자 수가 C명
#각 시험장에는 총감독관은 오직 1명, 부감독긍 여러 명 있어야 함
#각 시험장마다 응시자 모두를 감시해야 함. 이때 필요한 감독관 수의 최솟값

#출력: 필요한 감독관 수의 최솟값
answer = N

for n in A:
    student = n-B

    if student>0:
        m=student//C
        if student%C!=0:
            m+=1
        answer += m
        
print(answer)