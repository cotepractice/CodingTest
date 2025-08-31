#백준 #22251 빌런 호석

from collections import defaultdict

#N:가장 위층, K:자릿수, P: LED 최대 P개 반전 가능,X:
N, K, P, X = map(int,input().split())
answer = []

#최소 1개~최대 P개 반전
#켜진 부분을 끄고 꺼진 부분 켜기
#반전 이후 올바른 수가 보여지면서 1이상 N이하가 되도록 바꿔 헷갈리게 할 예정

#출력:실제로 X층에 멈춰있을 때 호석이가 반전시킬 수 있는 LED 경우의 수

#1)바꿔야할 LED 개수
n_dict = defaultdict(list)

#0,1,2,3,4,5,6,7,8,9로 변할 때 바꿔야 하는 LED 개수
n_dict[0]=[0,4,3,3,4,3,2,3,1,2] 
n_dict[1]=[4,0,5,3,2,5,6,1,5,4]
n_dict[2]=[3,5,0,2,5,4,3,4,2,3]
n_dict[3]=[3,3,2,0,3,2,3,2,2,1]
n_dict[4]=[4,2,5,3,0,3,4,3,3,2]
n_dict[5]=[3,5,4,2,3,0,1,4,2,1]
n_dict[6]=[2,6,3,3,4,1,0,5,1,2]
n_dict[7]=[3,1,4,2,3,4,5,0,4,3]
n_dict[8]=[1,5,2,2,3,2,1,4,0,1]
n_dict[9]=[2,4,3,1,2,1,2,3,1,0]


#3)X에서 반전한 수가 *디스플레이가 P개 이하인지 확인
#idx 자릿수 반전
def dfs(current_n,display_n,idx):
    global answer
    
    #1.종결조건
    if idx==K:
        answer.append(int(current_n))
        return 
    
    #2.current_n의 idx 자릿수 전환
    lst = n_dict[int(current_n[idx])]
    # current_n[idx]를 0~9로 변환
    for l in range(10):
        # display_n 바꿀 수 있는 디스플레이 개수에 해당해야 하고, idx 번째 수를 lst[l]로 변환
        if lst[l]<=display_n:
            next_n = ""
            for c in range(len(current_n)):
                if c==idx:
                    next_n += str(l)
                    continue
                next_n += current_n[c]

            dfs(next_n,display_n-lst[l],idx+1)

#2. 자릿수에 맞게 X 변환 
XX = ""

#X 글자수
cnt = 0
for k in str(X):
    cnt+=1
if cnt<K:
    diff = K-cnt
    XX = "0"*diff
XX += str(X) 

dfs(str(XX),P,0)

#3) 1 이상 N 이하인지 확인+동일한 숫자가 아닌지 확인
result = []
for a in answer:
    if 1<=a<=N and a!=X:
        result.append(a)
print(len(result))