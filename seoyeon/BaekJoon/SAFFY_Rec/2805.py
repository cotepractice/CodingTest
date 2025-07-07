#백준 #2805 나무 자르기

N, M = map(int,input().split())

trees = list(map(int,input().split()))

start,end = 1, max(trees) #start,end는 최소, 최대 나무 길이

while start<=end:
    mid = (start+end)//2

    #mid 기준으로 벌목
    cut_N = 0
    for i in trees:
        if i > mid:
            cut_N += i-mid
    
    #cut_N으로 start,end 결정. 최대 높이 구해야 하므로 start 증가
    if cut_N >= M:
        start = mid + 1 #나무를 충분히 얻었으니 더 높은 높이도 가능한지 확인
    else:
        end = mid - 1 #나무가 부족하므로 높이 낮춤
        
print(end)