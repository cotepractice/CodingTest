#백준 #10799 쇠막대기

sentence = list(input())

#dp는 해당 위치에 존재하는 쇠막대기 개수. 시작 위치에 dp 1 한 후 마지막에 총 개수는 dp의 합
dp = [0 for _ in range(len(sentence))] 

prev_bar = 0 #현재까지 존재하는 쇠막대기 개수
prev_light = False #직전이 레이저였는지 유무
for i in range(len(sentence)-1):
    #직전이 레이저인 경우 prev_bar를 감소시키면 안 되므로 continue
    if prev_light==True:
        prev_light = False
        continue
    if sentence[i]=="(" and sentence[i+1]==")":
        dp[i] = prev_bar
        prev_light = True
        continue
    if sentence[i]=="(":
        dp[i] = 1
        prev_bar += 1
    else:
        prev_bar -= 1
    prev_light = False
print(sum(dp))