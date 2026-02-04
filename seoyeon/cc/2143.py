#백준 #2143 두 배열의 합

#시간복잡도 O(max(n^2, m^2))
T = int(input())
n = int(input())
A_lst = list(map(int,input().split()))
m = int(input())
B_lst = list(map(int,input().split()))


#가능한 부 배열의 합 개수. a_dict[1]=2: 합쳐서 1이 되는 부배열의 개수 2개 
a_dict = dict()
b_dict = dict()

#a_dict 계산
for i in range(n):
    s=0
    for j in range(i,n):
        s+=A_lst[j]
        if s in a_dict:
            a_dict[s]+=1
        else:
            a_dict[s]=1

#b_dict 계산
for i in range(m):
    s=0
    for j in range(i,m):
        s+=B_lst[j]
        if s in b_dict:
            b_dict[s]+=1
        else:
            b_dict[s]=1

answer=0

for val in a_dict.keys():
    if T-val in b_dict:
        answer += (b_dict[T-val]*a_dict[val])
print(answer)