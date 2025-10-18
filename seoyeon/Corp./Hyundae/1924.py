#백준 #1924 2007년

days = [31,28,31,30,31,30,31,31,30,31,30,31]

x,y = map(int,input().split())

date = 0
#이전 달까지의 수
for i in range(x-1):
    date+=days[i]

#현재 날짜까지의 수
date+=y
date-=1

if date%7==0:
    print("MON")
elif date%7==1:
    print("TUE")
elif date%7==2:
    print("WED")
elif date%7==3:
    print("THU")
elif date%7==4:
    print("FRI")
elif date%7==5:
    print("SAT")
elif date%7==6:
    print("SUN")
