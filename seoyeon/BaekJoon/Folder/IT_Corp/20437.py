#백준 #20437 문자열 게임2
#17:30-18:05
#시간복잡도 O(T*N). T:최대100,N:W 길이로, 최대 10,000

from collections import defaultdict

T = int(input())

answer1, answer2 = float("inf"),-float("inf")

#가장 짧고 가장 긴 길이로 answer1, answer2 업데이트
def solve(lst):
    global answer1,answer2
    
    for i in range(len(lst)-K+1):
        ans = lst[i+K-1]-lst[i]
        answer1 = min(answer1,ans)
        answer2 = max(answer2,ans)

for _ in range(T):
    answer1, answer2 = float("inf"),-float("inf")

    W = list(input()) #알파벳 소문자로 이루어진 문자열
    K = int(input()) #어떤문자를 정확히 K개 포함하는 가장 짧은 연속 문자열의 길이

    #1.문자열에 해당하는 인덱스 dict에 저장
    dict = defaultdict(list)
    for idx in range(len(W)):
        
        if W[idx] in dict:
            dict[W[idx]].append(idx)

        else:
            dict[W[idx]] = [idx]

    #2.dict 리스트 길이가 K보다 크거나 같은 경우 solve
    for w in dict:
        lst = dict[w]
        if len(lst)>=K:
            solve(lst)
    
    #3.둘 중 하나라도 없으면 -1 출력, 그렇지 않은 경우 정답 출력
    if answer1==float("inf") or answer2==-float("inf"):
        print(-1)
    else:
        print(answer1+1,answer2+1)