#https://www.hackerrank.com/challenges/valid-bst/problem

T = int(input())

#start_idx, end_idx 포함
#range_lst=[a,b]. a보다 커야 하고, b보다 작아야 함
#left인 경우 b 업데이트
#right인 경우 a 업데이트
#이 과정에서 현재 값이 범위 내 존재하지 않으면 바로 False return
def check(range_lst,current_lst):
    global answer

    #print("range_lst",range_lst)
    #print("current_lst",current_lst)

    #종결조건
    if len(current_lst)==0:
        return

    #BST 확인
    for c in current_lst:
        if c<range_lst[0] or c>range_lst[1]:
            answer=False
            return
    #right_idx 업데이트
    right_idx=len(current_lst)
    for i in range(len(current_lst)):
        if current_lst[i]>current_lst[0]:
            right_idx=i
            break

    #left
    check([range_lst[0],current_lst[0]], current_lst[1:right_idx])

    #right
    check([current_lst[0],range_lst[1]], current_lst[right_idx:])



for _ in range(T):
    N = int(input())
    lst=list(map(int,input().split()))
    answer = True

    #Binary Search Tree
    #Empty Tree: null
    #1. Left Subtree: Node보다 작은 값을 가져야 함
    #2. Right Subtree: Node보다 큰 값을 가져야 함
    right_idx=len(lst)
    for i in range(1,len(lst)):
        #print("i",i,'lst[i]',lst[i],lst[0],lst[i]>lst[0])
        if lst[i]>lst[0]:
            right_idx=i
            break
    #print("RIGHT",right_idx)
    check([-1*float("inf"),lst[0]], lst[1:right_idx])
    check([lst[0],float("inf")], lst[right_idx:len(lst)])

    if answer==True:
        print("YES")
    else:
        print("NO")