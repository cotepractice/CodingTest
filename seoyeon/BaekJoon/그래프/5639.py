#백준 #5639 이진검색트리

#전위 순환(루트,왼,오)한 결과가 주어질 때 후위 순회(왼,오,루트)한 결과
import sys
sys.setrecursionlimit(10 ** 6)

node = []
while True:
    try:
        node.append(int(input()))
    except:
        break


def tree(root_idx,last_idx):

    #종결조건
    if root_idx>last_idx:
        return 
        
    root = node[root_idx]

    #right_idx 탐색. 현재 root보다 큰 경우
    right_idx=root_idx+1

    while right_idx<=last_idx:
        if node[right_idx]>root:
            break
        right_idx+=1

    #왼쪽트리
    tree(root_idx+1,right_idx-1)

    #오른쪽트리
    tree(right_idx,last_idx)

    print(root)

tree(0,len(node)-1)