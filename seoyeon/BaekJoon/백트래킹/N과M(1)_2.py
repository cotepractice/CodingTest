#백준 #15649 N과 M(1)

N, M = map(int, input().split())

nums = [i for i in range(N+1)]

# def backtracking(i,lst, cnt):
#     print("i",i,"lst",lst,"cnt",cnt)
#     if i>=N:
#         return
#     if cnt == M:
#         print(*lst)
#         return
#     elif cnt > M:
#         return 
#     #lst에 넣지 않는 경우
#     backtracking(i+1,lst,cnt)
    
#     #lst에 넣기
#     print("i",lst)
#     lst.append(i)
#     backtracking(i+1,lst,cnt+1)

def backtracking(lst,cnt):
    if cnt==M:
        print(*lst)
        return

    for i in range(1,N+1):   
        if i not in lst:
            #i 추가한 경우
            lst.append(i)
            backtracking(lst,cnt+1) 
            #i 추가하지 않는 경우 -> return되어 돌아온 이후 다음 for문을 돌 때에는 현재의 i가 포함되지 않음
            lst.pop()
            
backtracking([],0)