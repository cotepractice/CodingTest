#백준 #19941 햄버거 분배
#시간복잡도 O(N*K)

#1초 -> 10^8. 0.5초 -> 10^8/2 => N^2 안 됨
#시간제한 0.5초. N<=20,000, K<=10. 
N, K = map(int, input().split()) #N:식탁의길이 K:햄버거선택할수있는거리

tables = list(input())

cnt = 0

for i in range(N):

    if tables[i]=="H":
        for j in range(i+1,i+K+1):  
            #j가 범위 내에 존재하는 경우만 탐색
            if j<0 or j>=N:
                continue
            if tables[j]=="P":
                cnt += 1
                tables[i]="X" #먹었으면 X로 변경
                tables[j]="X"
                break #하나 먹었으면 다음 i로 넘어감

    elif tables[i]=="P":
        for j in range(i+1,i+K+1):
            #j가 범위 내에 존재하는 경우만 탐색
            if j<0 or j>=N:
                continue
            if tables[j]=="H":
                cnt += 1
                tables[i]="X" #먹었으면 X로 변경
                tables[j]="X"
                break #하나 먹었으면 다음 i로 넘어감

print(cnt)