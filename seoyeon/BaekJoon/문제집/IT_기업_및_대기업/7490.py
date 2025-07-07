#백준 #7490 0 만들기
#완전탐색.DFS O(N). dfs:O(3^(N-1)).solv:O(N*2-1)

#가능한 경우
#1) +
#2) -
#3) 공백

#idx:현재 idx까지 연산 진행, n:종결, current_sum:현재 idx까지의 합, current_lst:answer
def dfs(idx,n,current_lst):
    if idx == n:
        answer.append(current_lst)
        return []
    
    #1. +
    tmp1 = current_lst[:]
    tmp1.append("+")
    tmp1.append(idx+1)
    dfs(idx+1,n,tmp1)

    #2. -
    tmp2 = current_lst[:]
    tmp2.append("-")
    tmp2.append(idx+1)
    dfs(idx+1,n,tmp2)

    #3. 공백
    tmp3 = current_lst[:]
    tmp3.append(" ")
    tmp3.append(idx+1)
    dfs(idx+1,n,tmp3)

def solv(lst):
    tmp = []
    current_n = ""

    for l in lst:
        if l == "+":
            tmp.append(int(current_n))
            tmp.append(l)
            current_n = ""
        elif l == "-":
            tmp.append(int(current_n))
            tmp.append(l)
            current_n = ""
        elif l == " ":
            pass
        else:
            current_n += str(l)
    tmp.append(int(current_n))
    
    sum = tmp[0]
    for t in range(1,len(tmp),2):
        if tmp[t]=="+":
            sum += tmp[t+1]
        elif tmp[t]=="-":
            sum -= tmp[t+1]
    #print("lst",lst,"sum",sum)
    if sum==0:
        return lst
    return -1

T = int(input())

for _ in range(T):
    N = int(input())
    answer = []
    result = []
    #1. dfs로 가능한 모든 리스트 탐색
    dfs(1,N,[1])
    #2. 리스트 연산
    for ans in answer:
        res = solv(ans)
        if res!=-1:
            result.append(res)
    result.sort()
    for r in result:
        expression = ""
        for idx in range(len(r)):
            expression+=str(r[idx])
        print(expression)
    print()
