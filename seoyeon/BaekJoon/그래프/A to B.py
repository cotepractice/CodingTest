#백준 #16953 A->B
#그래프 문제
#0:40 
#b를 2로 나눈 경우를 list에 추가해 a에 연산을 한 결과가 list에 존재하면 해당 방식으로 연산

a, b = map(int, input().split())

lst = []

result_b = b
lst.append(b)

while (b%2 == 0 or str(b)[-1] == "1"):
    #print("b",b)
    #print("str_b",str(b)[-1])
    if (str(b) == "1"):
        lst.append(b)
        break
    if (str(b)[-1] == "1"):
        str_b = str(b)[:-1]
        b=int(str_b)
        lst.append(b)    
    if (b%2 == 0):
        lst.append(b//2)
        b = b//2

lst.sort()

#print("lst",lst)
check = -1
cnt = 0
while (True): 
    str_a = str(a)
    str_a += '1'
    #print("str_a",str_a, int(str_a) in lst)

    #연산
    if (int(str_a) in lst):
        a = int(str_a)
        cnt += 1
    else:
        a *= 2
        cnt += 1
    
    #print("a",a, a==b)

    #결과
    if (cnt == len(lst)):   #연산의 최솟값이므로 cnt가 lst의 크기보다 클 수 없음
        break
    if (a == result_b):
        check = 0
        cnt += 1
        print(cnt)
        break

if (check != 0):
    print(-1)