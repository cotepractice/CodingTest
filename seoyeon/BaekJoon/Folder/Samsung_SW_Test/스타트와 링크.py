#백준 #14889 스타트와 링크
#삼성 SW 역량 테스트 기출
#예상: 조합&구현, 알고리즘: 브루트포스&백트래킹

from itertools import combinations

#1. nC(n//2) 리스트 구하기
def combination(N):
    number_lst = [n for n in range(N)]
    origin = list()
    comparison = list()

    origin = list(combinations(number_lst, N//2))
    for o in origin:
        lst = list(set(number_lst) - set(o))
        comparison.append(lst)
    return origin, comparison

#2. for문으로 값의 차이 모두 구하기
#이때 list1과 list2는 이중 리스트가 아니라 리스트. list1: [1,3,6], list2: [2,4,5]
#반환: 차이
def diff(list1, list2):
    cnt = len(list1)    #list 개수
    gap = 0
    start_N = 0
    link_N = 0

    for i in range(cnt):
        for j in range(cnt):
            if (i!=j):
                start_N += power_graph[list1[i]-1][list1[j]-1]
                link_N += power_graph[list2[i]-1][list2[j]-1]
    gap = abs(start_N - link_N)
    return gap

#main
N = int(input())
power_graph = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    power_graph[i] = list(map(int, input().split()))

#Ex. list1 = [[1,2],[1,3],[1,4]]이면 list2 = [[3,4],[2,4],[2,3]]
list1, list2 = combination(N)

min = float('inf')
for k in range(len(list1)):
    gap = diff(list1[k], list2[k])
    if gap < min:
        min = gap

print(min)