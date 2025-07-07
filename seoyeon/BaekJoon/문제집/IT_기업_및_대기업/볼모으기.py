#백준 #17615 볼 모으기

N = int(input())

balls = input()
#1. 서브태스크 1 성공! 15점
#balls = list(input())
# s_color = ""
# e_color = ""

# ans = [0,0] #Blue, Red 순서
# #뒤에서부터 탐색

# prev_color = balls[N-1]
# check = 0
# for i in range(N-2,-1,-1):
#     if balls[i]!=prev_color:
#         ans[0] += 1
#         if check == 0:
#             check = 1
#     else:
#         if check==1:
#             ans[1] += 1
    
# print(min(ans))

#2. 서브태스크 모두 성공! 100점
ans = []
#좌우에 뭉쳐있는 공들 제거한 후 남은 색 카운트
#1. Red 공을 오른쪽으로 넘기는 경우
strip_ball = balls.rstrip("R")
ans.append(strip_ball.count("R"))

#2. Blue 공을 오른쪽으로 넘기는 경우
strip_ball = balls.rstrip("B")
ans.append(strip_ball.count("B"))

#3. Red 공을 왼쪽으로 넘기는 경우
strip_ball = balls.lstrip("R")
ans.append(strip_ball.count("R"))

#4. Blud 공을 왼쪽으로 넘기는 경우
strip_ball = balls.lstrip("B")
ans.append(strip_ball.count("B"))

print(min(ans))