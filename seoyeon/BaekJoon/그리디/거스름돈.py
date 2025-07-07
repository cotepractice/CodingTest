#백준 #14916 거스름돈
#그리디 문제

#1. 정답
n = int(input())

five = n//5
m = n-five*5
two = m//2
m -= two*2

if (m==0):
    print(five+two)
else:
    while True:
        five -= 1

        if (five==-1):
            print(-1)
            break

        m = n-five*5
        two = m//2
        m -= two*2
    
        if (m==0):
            print(five+two)
            break
        
        # if (five==0):
        #     print(-1)
        #     break

#2. 틀린코드
n = int(input())

five = n//5
m = n-five*5
two = m//2
m -= two*2

if (m==0):
    print(five+two)
else:
    while True:
        five -= 1

        m = n-five*5
        two = m//2
        m -= two*2
    
        if (m==0):
            print(five+two)
            break
        
        if (five==0):
            print(-1)
            break
