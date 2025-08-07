#[토스 NEXT] 2022년 코딩테스트 기출문제
#멋쟁이 숫자

s = input() # 0<=s.length<1,000

#이분탐색?

i = 0
result = -1

while i<=len(s)-2:
    current = s[i]
    for j in range(i+1,len(s)):
        if s[j]==current and s[j+1]==current:
            result = max(result,int(current))
            i+=3
            break
        elif s[j]==current and s[j+1]!=current:
            i+=2
            break
        else:
            i+=1
            break

if result==-1:
    print(-1)
else:
    print(int(str(result)*3),sep="")
