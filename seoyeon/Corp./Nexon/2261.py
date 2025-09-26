#closest 알고리즘

N = int(input())
points = [[] for _ in range(N)]

for i in range(N):
    x,y = map(int,input().split())
    points[i]=[x,y]

sorted_x = sorted(points, key=lambda x:x[0])
sorted_y = sorted(points, key=lambda x:x[1])

def bruteforce(lst):
    ans = float("inf")

    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            ans = min(ans, (lst[i][0]-lst[j][0])**2+(lst[i][1]-lst[j][1])**2)
    return ans

#sorted_x와 sorted_y는 각각 x,y로 정렬된 [x,y] 좌표 쌍
def solv(sorted_x,sorted_y):
    #print("len(sorted_x)",len(sorted_x))
    
    if len(sorted_x)<=3:
        return bruteforce(sorted_x)

    #1. x<=mid_n
    mid_idx = len(sorted_x)//2
    mid_x = sorted_x[mid_idx][0]
    left_x = sorted_x[:mid_idx]
    right_x = sorted_x[mid_idx:]

    left_y = [p for p in sorted_y if p[0]<=mid_x]
    right_y = [p for p in sorted_y if p[0]>mid_x]

    #2. 왼쪽 또는 오른쪽에 존재하는 두 점 비교
    d_left = solv(left_x,left_y)
    d_right = solv(right_x,right_y)
    d = min(d_left,d_right)

    #3. 중간
    #mid_x와 현재 x의 제곱이 d 제곱보다 작아야함. 큰 경우 d보다 커져 정답이 될 수 없음
    #(x-x1)**2 + (y-y1)**2 = d**2
    #strip: 점들 좌표
    #즉, mid_x까지의 거리제곱이 d 이하인 좌표를 모두 탐색 후 그 중 2개씩 뽑아 거리 계산
    strip = [p for p in sorted_y if (p[0]-mid_x)**2<=d]
    for i in range(len(strip)):
        for j in range(i+1,len(strip)):
            #y좌표 제곱이 d제곱보다 크면 strip은 이제 더 큰 y만을 가지기 때문에 정답이 될 수 없음
            if (strip[i][1]-strip[j][1])**2 >= d:
                break
            d = min(d, (strip[i][0]-strip[j][0])**2+(strip[i][1]-strip[j][1])**2)
    
    return d

print(solv(sorted_x,sorted_y))